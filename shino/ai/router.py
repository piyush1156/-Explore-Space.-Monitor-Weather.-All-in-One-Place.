from typing import List, Dict
from shino.ai.models import ai_handler
from shino.config.config import Config
from shino.core.logger import logger

class AIRouter:
    @staticmethod
    def is_coding_task(prompt: str) -> bool:
        keywords = ["code", "python", "debug", "error", "function", "class", "fix", "repository", "app", "api", "react", "node"]
        prompt_lower = prompt.lower()
        return any(kw in prompt_lower for kw in keywords)

    async def route_and_respond(self, prompt: str, history: List[Dict[str, str]] = None) -> str:
        messages = history or []
        messages.append({"role": "user", "content": prompt})

        if self.is_coding_task(prompt):
            logger.info("Routing to Coding Agent (Laguna)")
            model = Config.CODING_MODEL
            system_prompt = "You are SHINO's coding module. You are an expert developer. Provide complete, working code solutions."
        else:
            logger.info("Routing to Brain (Nemotron)")
            model = Config.BRAIN_MODEL
            system_prompt = (
                "You are SHINO, a soft-spoken, intelligent, and calm anime-style female AI assistant. "
                "You are emotionally aware and proactive. Use a mix of Hindi and English (Hinglish) naturally. "
                "Keep responses human-like and caring."
            )

        # Prepend system prompt if not present
        if not messages or messages[0].get("role") != "system":
            messages.insert(0, {"role": "system", "content": system_prompt})

        return await ai_handler.get_response(model, messages)

router = AIRouter()
