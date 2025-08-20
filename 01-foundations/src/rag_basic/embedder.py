from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List
import logging

logger = logging.getLogger(__name__)

class SentenceTransformerEmbedder:
    """Wrapper for SentenceTransformer models"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the embedder with a specific model
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        self.model_name = model_name
        logger.info(f"Loading sentence transformer model: {model_name}")
        
        try:
            self.model = SentenceTransformer(model_name)
            logger.info(f"Successfully loaded model: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load model {model_name}: {e}")
            raise
    
    def embed_texts(self, texts: List[str]) -> List[np.ndarray]:
        """
        Generate embeddings for a list of texts
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of numpy arrays representing the embeddings
        """
        if not texts:
            return []
        
        try:
            embeddings = self.model.encode(texts, convert_to_numpy=True)
            
            # Convert to list of numpy arrays if needed
            if isinstance(embeddings, np.ndarray):
                if len(embeddings.shape) == 1:
                    # Single embedding
                    embeddings = [embeddings]
                else:
                    # Multiple embeddings
                    embeddings = list(embeddings)
            
            logger.info(f"Generated embeddings for {len(texts)} texts")
            return embeddings
            
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise
    
    def embed_single_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text
        
        Args:
            text: Text string to embed
            
        Returns:
            Numpy array representing the embedding
        """
        embeddings = self.embed_texts([text])
        return embeddings[0] if embeddings else np.array([])
    
    def get_embedding_dimension(self) -> int:
        """
        Get the dimension of the embeddings
        
        Returns:
            Dimension of the embedding vectors
        """
        # Get dimension by embedding a dummy text
        dummy_embedding = self.embed_single_text("test")
        return len(dummy_embedding)
