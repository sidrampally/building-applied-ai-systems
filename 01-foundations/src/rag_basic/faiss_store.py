import faiss
import numpy as np
import pickle
import os
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class FAISSVectorStore:
    """FAISS-based vector store for document embeddings"""
    
    def __init__(self, index_path: str = "./data/faiss_index", dimension: int = 384):
        """
        Initialize FAISS vector store
        
        Args:
            index_path: Path to store the FAISS index and metadata
            dimension: Dimension of the embedding vectors
        """
        self.index_path = index_path
        self.dimension = dimension
        self.documents: List[str] = []
        self.metadata: List[Dict[str, Any]] = []
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        
        # Initialize or load FAISS index
        self._initialize_index()
        
        logger.info(f"FAISS vector store initialized at {index_path}")
    
    def _initialize_index(self):
        """Initialize or load the FAISS index"""
        index_file = f"{self.index_path}.faiss"
        metadata_file = f"{self.index_path}.pkl"
        
        if os.path.exists(index_file) and os.path.exists(metadata_file):
            # Load existing index
            try:
                self.index = faiss.read_index(index_file)
                
                with open(metadata_file, 'rb') as f:
                    data = pickle.load(f)
                    self.documents = data.get('documents', [])
                    self.metadata = data.get('metadata', [])
                
                logger.info(f"Loaded existing FAISS index with {len(self.documents)} documents")
                
            except Exception as e:
                logger.warning(f"Failed to load existing index: {e}. Creating new index.")
                self._create_new_index()
        else:
            # Create new index
            self._create_new_index()
    
    def _create_new_index(self):
        """Create a new FAISS index"""
        # Create a flat index for exact search
        self.index = faiss.IndexFlatIP(self.dimension)  # Inner product for cosine similarity
        self.documents = []
        self.metadata = []
        logger.info(f"Created new FAISS index with dimension {self.dimension}")
    
    def add_documents(self, documents: List[str], embeddings: List[np.ndarray], 
                     metadata: Optional[List[Dict[str, Any]]] = None):
        """
        Add documents and their embeddings to the vector store
        
        Args:
            documents: List of document texts
            embeddings: List of document embeddings
            metadata: Optional list of metadata for each document
        """
        if len(documents) != len(embeddings):
            raise ValueError("Number of documents must match number of embeddings")
        
        if metadata and len(metadata) != len(documents):
            raise ValueError("Number of metadata items must match number of documents")
        
        # Normalize embeddings for cosine similarity
        normalized_embeddings = []
        for emb in embeddings:
            norm = np.linalg.norm(emb)
            if norm > 0:
                normalized_emb = emb / norm
            else:
                normalized_emb = emb
            normalized_embeddings.append(normalized_emb)
        
        # Convert to numpy array
        embeddings_array = np.array(normalized_embeddings).astype('float32')
        
        # Add to FAISS index
        self.index.add(embeddings_array)
        
        # Store documents and metadata
        self.documents.extend(documents)
        if metadata:
            self.metadata.extend(metadata)
        else:
            self.metadata.extend([{"source": f"doc_{i}"} for i in range(len(documents))])
        
        # Save index and metadata
        self._save_index()
        
        logger.info(f"Added {len(documents)} documents to vector store")
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Dict[str, Any]]:
        """
        Search for similar documents
        
        Args:
            query_embedding: Query embedding vector
            k: Number of results to return
            
        Returns:
            List of dictionaries containing document text, metadata, and similarity score
        """
        if self.index.ntotal == 0:
            return []
        
        # Normalize query embedding
        norm = np.linalg.norm(query_embedding)
        if norm > 0:
            normalized_query = query_embedding / norm
        else:
            normalized_query = query_embedding
        
        # Convert to numpy array
        query_array = np.array([normalized_query]).astype('float32')
        
        # Search
        scores, indices = self.index.search(query_array, min(k, self.index.ntotal))
        
        # Format results
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx < len(self.documents):
                results.append({
                    "text": self.documents[idx],
                    "metadata": self.metadata[idx],
                    "score": float(score),
                    "index": int(idx)
                })
        
        logger.info(f"Search returned {len(results)} results")
        return results
    
    def _save_index(self):
        """Save the FAISS index and metadata to disk"""
        try:
            # Save FAISS index
            faiss.write_index(self.index, f"{self.index_path}.faiss")
            
            # Save metadata
            with open(f"{self.index_path}.pkl", 'wb') as f:
                pickle.dump({
                    'documents': self.documents,
                    'metadata': self.metadata
                }, f)
            
            logger.info(f"Saved FAISS index and metadata to {self.index_path}")
            
        except Exception as e:
            logger.error(f"Failed to save index: {e}")
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector store"""
        return {
            "total_documents": len(self.documents),
            "index_size": self.index.ntotal,
            "embedding_dimension": self.dimension,
            "index_path": self.index_path
        }
    
    def clear(self):
        """Clear all documents from the vector store"""
        self._create_new_index()
        self._save_index()
        logger.info("Cleared all documents from vector store")
