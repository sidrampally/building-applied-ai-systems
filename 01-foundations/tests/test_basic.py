import pytest
import numpy as np
from src.rag_basic.embedder import SentenceTransformerEmbedder
from src.rag_basic.faiss_store import FAISSVectorStore
from src.rag_basic.llm_client import LLMClient

class TestRAGComponents:
    """Basic tests for RAG components"""
    
    def test_embedder_initialization(self):
        """Test that the embedder can be initialized"""
        embedder = SentenceTransformerEmbedder()
        assert embedder.model_name == "sentence-transformers/all-MiniLM-L6-v2"
        assert embedder.model is not None
    
    def test_embedding_generation(self):
        """Test that embeddings can be generated"""
        embedder = SentenceTransformerEmbedder()
        texts = ["Hello world", "This is a test"]
        embeddings = embedder.embed_texts(texts)
        
        assert len(embeddings) == 2
        assert all(isinstance(emb, np.ndarray) for emb in embeddings)
        assert all(len(emb) > 0 for emb in embeddings)
    
    def test_vector_store_initialization(self):
        """Test that the vector store can be initialized"""
        store = FAISSVectorStore(index_path="./test_index", dimension=384)
        assert store.dimension == 384
        assert store.index is not None
    
    def test_vector_store_add_and_search(self):
        """Test adding documents and searching"""
        store = FAISSVectorStore(index_path="./test_index", dimension=384)
        embedder = SentenceTransformerEmbedder()
        
        # Add documents
        documents = ["Document 1", "Document 2", "Document 3"]
        embeddings = embedder.embed_texts(documents)
        store.add_documents(documents, embeddings)
        
        # Search
        query = "Document 1"
        query_embedding = embedder.embed_single_text(query)
        results = store.search(query_embedding, k=2)
        
        assert len(results) > 0
        assert "text" in results[0]
        assert "score" in results[0]
        assert "metadata" in results[0]
    
    def test_llm_client_initialization(self):
        """Test that LLM client can be initialized (without API key)"""
        # This test will fail if no API key is provided, which is expected
        with pytest.raises(ValueError):
            LLMClient(provider="openai", api_key=None)

if __name__ == "__main__":
    pytest.main([__file__])
