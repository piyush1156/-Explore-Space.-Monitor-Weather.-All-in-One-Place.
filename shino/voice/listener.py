import asyncio
import numpy as np
from faster_whisper import WhisperModel
from shino.core.logger import logger
from shino.config.config import Config

class ShinoListener:
    def __init__(self, model_size="base"):
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")
        self.is_listening = False

    async def listen(self):
        self.is_listening = True
        logger.info("SHINO listener started.")
        while self.is_listening:
            # This would be connected to sounddevice in a real desktop environment
            await asyncio.sleep(1)

    def transcribe_file(self, audio_path):
        segments, _ = self.model.transcribe(audio_path, beam_size=5)
        return " ".join([s.text for s in segments])

listener = ShinoListener()
