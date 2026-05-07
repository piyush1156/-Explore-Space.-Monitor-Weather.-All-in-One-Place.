import os
from shino.ai.models import ai_handler
from shino.config.config import Config
from shino.core.logger import logger
from shino.utils.helpers import run_command

class CodingAgent:
    def __init__(self):
        self.model = Config.CODING_MODEL

    async def generate_code(self, prompt: str):
        system_prompt = (
            "You are a master coding agent. Generate production-ready code. "
            "Return only the code block if possible, or clear file-based instructions."
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        return await ai_handler.get_response(self.model, messages)

    def write_to_file(self, filepath: str, content: str):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w") as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Failed to write file {filepath}: {e}")
            return False

coding_agent = CodingAgent()
