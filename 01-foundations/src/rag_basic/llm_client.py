import openai
import anthropic
import os
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class LLMClient:
    """Client for interacting with LLM providers"""
    
    def __init__(self, provider: str = "openai", model: str = "gpt-4", api_key: Optional[str] = None):
        """
        Initialize LLM client
        
        Args:
            provider: LLM provider ("openai" or "anthropic")
            model: Model name to use
            api_key: API key for the provider
        """
        self.provider = provider.lower()
        self.model = model
        self.api_key = api_key or os.getenv(f"{provider.upper()}_API_KEY")
        
        if not self.api_key:
            raise ValueError(f"API key required for {provider}")
        
        # Initialize provider-specific client
        if self.provider == "openai":
            self.client = openai.OpenAI(api_key=self.api_key)
        elif self.provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        
        logger.info(f"Initialized {provider} client with model {model}")
    
    async def generate(self, prompt: str, max_tokens: Optional[int] = None, 
                      temperature: Optional[float] = None) -> str:
        """
        Generate text using the LLM
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text
        """
        try:
            if self.provider == "openai":
                return await self._generate_openai(prompt, max_tokens, temperature)
            elif self.provider == "anthropic":
                return await self._generate_anthropic(prompt, max_tokens, temperature)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
                
        except Exception as e:
            logger.error(f"Error generating text with {self.provider}: {e}")
            raise
    
    async def _generate_openai(self, prompt: str, max_tokens: Optional[int] = None, 
                              temperature: Optional[float] = None) -> str:
        """Generate text using OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens or int(os.getenv("MAX_TOKENS", "1000")),
                temperature=temperature or float(os.getenv("TEMPERATURE", "0.1"))
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    async def _generate_anthropic(self, prompt: str, max_tokens: Optional[int] = None, 
                                 temperature: Optional[float] = None) -> str:
        """Generate text using Anthropic"""
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens or int(os.getenv("MAX_TOKENS", "1000")),
                temperature=temperature or float(os.getenv("TEMPERATURE", "0.1")),
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            logger.error(f"Anthropic API error: {e}")
            raise
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model"""
        return {
            "provider": self.provider,
            "model": self.model,
            "max_tokens": int(os.getenv("MAX_TOKENS", "1000")),
            "temperature": float(os.getenv("TEMPERATURE", "0.1"))
        }
