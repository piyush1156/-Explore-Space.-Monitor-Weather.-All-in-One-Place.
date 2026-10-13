import asyncio
from typing import List, Dict, Any
from openai import AsyncOpenAI
from shino.config.config import Config
from shino.core.logger import logger

class AIModelHandler:
    def __init__(self):
        self.client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=Config.OPENROUTER_API_KEY,
        )

    async def get_response(self, model: str, messages: List[Dict[str, str]], **kwargs) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling AI model {model}: {e}")
            return "Maaf kijiye, main abhi process nahi kar paa rahi hoon."

ai_handler = AIModelHandler()
