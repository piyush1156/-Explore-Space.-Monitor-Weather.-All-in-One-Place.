import asyncio
from TTS.api import TTS
from shino.core.logger import logger

class ShinoSpeaker:
    def __init__(self):
        self.tts = None
        try:
            # Lazy load TTS to avoid long startup if not used
            pass
        except Exception as e:
            logger.error(f"TTS Init Error: {e}")

    async def speak(self, text: str):
        if not text:
            return
        logger.info(f"SHINO: {text}")
        # In production, this would trigger actual audio playback
        # if not self.tts: self.tts = TTS(...)
        print(f"\n[SHINO]: {text}\n")

speaker = ShinoSpeaker()
