import requests
import os
from typing import List, Dict, Optional, Union
from dotenv import load_dotenv

load_dotenv()

class PerplexityAPI:
    BASE_URL = "https://api.perplexity.ai/chat/completions"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('PERPLEXITY_API_KEY')
        if not self.api_key:
            raise ValueError("Perplexity API key is required")
    
    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "llama-3.1-sonar-small-128k-online",
        max_tokens: int = 1024,
        temperature: float = 0.2,
        top_p: float = 0.9,
        return_citations: bool = True,
        search_domain_filter: Optional[List[str]] = None,
        return_images: bool = False,
        return_related_questions: bool = False,
        search_recency_filter: str = "month",
        top_k: int = 0,
        stream: bool = False,
        presence_penalty: float = 0,
        frequency_penalty: float = 1
    ) -> Dict:
        """
        Send a chat completion request to Perplexity API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use for completion
            ... (other parameters match API options)
            
        Returns:
            API response as dictionary
        """
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "return_citations": return_citations,
            "search_domain_filter": search_domain_filter or ["perplexity.ai"],
            "return_images": return_images,
            "return_related_questions": return_related_questions,
            "search_recency_filter": search_recency_filter,
            "top_k": top_k,
            "stream": stream,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty
        }

        response = requests.post(
            self.BASE_URL,
            json=payload,
            headers=self._get_headers()
        )
        
        response.raise_for_status()
        return response.json()

    def simple_completion(
        self,
        user_message: str,
        system_message: str = "Be precise and concise.",
        **kwargs
    ) -> Dict:
        """
        Simplified method for single message completions.
        
        Args:
            user_message: The user's input message
            system_message: Optional system message
            **kwargs: Additional parameters to pass to chat_completion
            
        Returns:
            API response as dictionary
        """
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        return self.chat_completion(messages, **kwargs)['choices'][0]['message']['content']

perplexity = PerplexityAPI()
print(perplexity.simple_completion("what is the values and mission of doordash?"))