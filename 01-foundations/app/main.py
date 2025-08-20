from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")))
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="RAG Foundations API",
    description="A minimal RAG (Retrieval-Augmented Generation) system",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class EmbedRequest(BaseModel):
    texts: List[str]
    metadata: Optional[List[Dict[str, Any]]] = None

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class AnswerRequest(BaseModel):
    question: str
    context: List[str]
    search_results: Optional[List[Dict[str, Any]]] = None

class EmbedResponse(BaseModel):
    message: str
    count: int

class SearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    query: str

class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]
    question: str

# Global variables (in production, use proper dependency injection)
vector_store = None
embedder = None
llm_client = None

@app.on_event("startup")
async def startup_event():
    """Initialize components on startup"""
    global vector_store, embedder, llm_client
    
    logger.info("Initializing RAG system components...")
    
    # Initialize components (will be implemented in src/rag_basic/)
    try:
        from src.rag_basic.embedder import SentenceTransformerEmbedder
        from src.rag_basic.faiss_store import FAISSVectorStore
        from src.rag_basic.llm_client import LLMClient
        
        # Initialize embedder
        embedder = SentenceTransformerEmbedder(
            model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        )
        
        # Initialize vector store
        vector_store = FAISSVectorStore(
            index_path=os.getenv("VECTOR_INDEX_PATH", "./data/faiss_index"),
            dimension=384  # all-MiniLM-L6-v2 dimension
        )
        
        # Initialize LLM client
        llm_client = LLMClient(
            provider=os.getenv("LLM_PROVIDER", "openai"),
            model=os.getenv("LLM_MODEL", "gpt-4"),
            api_key=os.getenv("LLM_API_KEY")
        )
        
        logger.info("RAG system components initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize RAG components: {e}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "RAG Foundations API",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.post("/embed", response_model=EmbedResponse)
async def embed_documents(request: EmbedRequest):
    """Embed documents into the vector store"""
    try:
        if not vector_store or not embedder:
            raise HTTPException(status_code=500, detail="Vector store not initialized")
        
        # Generate embeddings
        embeddings = embedder.embed_texts(request.texts)
        
        # Store in vector database
        metadata = request.metadata or [{"source": f"doc_{i}"} for i in range(len(request.texts))]
        vector_store.add_documents(request.texts, embeddings, metadata)
        
        logger.info(f"Embedded {len(request.texts)} documents")
        
        return EmbedResponse(
            message=f"Successfully embedded {len(request.texts)} documents",
            count=len(request.texts)
        )
        
    except Exception as e:
        logger.error(f"Error embedding documents: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search", response_model=SearchResponse)
async def search_documents(request: SearchRequest):
    """Search for relevant documents"""
    try:
        if not vector_store or not embedder:
            raise HTTPException(status_code=500, detail="Vector store not initialized")
        
        # Embed the query
        query_embedding = embedder.embed_texts([request.query])[0]
        
        # Search for similar documents
        results = vector_store.search(query_embedding, k=request.top_k)
        
        logger.info(f"Search completed for query: {request.query}")
        
        return SearchResponse(
            results=results,
            query=request.query
        )
        
    except Exception as e:
        logger.error(f"Error searching documents: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/answer", response_model=AnswerResponse)
async def generate_answer(request: AnswerRequest):
    """Generate an answer using RAG"""
    try:
        if not llm_client:
            raise HTTPException(status_code=500, detail="LLM client not initialized")
        
        # Create context from retrieved documents
        context = "\n\n".join(request.context)
        
        # Generate answer using LLM
        prompt = f"""Based on the following context, answer the question. If the context doesn't contain enough information to answer the question, say so.

Context:
{context}

Question: {request.question}

Answer:"""
        
        answer = await llm_client.generate(prompt)
        
        # Extract sources from search results metadata
        sources = []
        if request.search_results:
            for result in request.search_results:
                metadata = result.get('metadata', {})
                source = metadata.get('source', f"document_{result.get('index', 'unknown')}")
                sources.append(source)
        else:
            # Fallback to generic source names if no search results provided
            sources = [f"source_{i}" for i in range(len(request.context))]
        
        logger.info(f"Generated answer for question: {request.question}")
        
        return AnswerResponse(
            answer=answer,
            sources=sources,
            question=request.question
        )
        
    except Exception as e:
        logger.error(f"Error generating answer: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "components": {
            "vector_store": vector_store is not None,
            "embedder": embedder is not None,
            "llm_client": llm_client is not None
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", "8000")),
        reload=os.getenv("DEBUG", "true").lower() == "true"
    )
