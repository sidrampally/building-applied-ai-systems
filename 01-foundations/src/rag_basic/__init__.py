"""
RAG Basic - Core components for Retrieval-Augmented Generation

This module provides the foundational components for building RAG systems:
- SentenceTransformerEmbedder: For generating text embeddings
- FAISSVectorStore: For storing and searching vector embeddings
- LLMClient: For interacting with LLM providers
"""

from .embedder import SentenceTransformerEmbedder
from .faiss_store import FAISSVectorStore
from .llm_client import LLMClient

__all__ = [
    "SentenceTransformerEmbedder",
    "FAISSVectorStore", 
    "LLMClient"
]

__version__ = "1.0.0"
