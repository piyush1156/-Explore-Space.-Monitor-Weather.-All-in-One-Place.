import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "mock_key")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")

    # AI Models
    BRAIN_MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
    CODING_MODEL = "poolside/laguna-m.1:free"

    # System Settings
    SHINO_NAME = os.getenv("SHINO_NAME", "SHINO")
    DEBUG = os.getenv("DEBUG_MODE", "True").lower() == "true"

    # Voice Settings
    WAKE_WORDS = ["shino", "hey shino"]
    INACTIVITY_TIMEOUT = 20  # seconds

    # Memory Settings
    DB_PATH = "shino_memory.db"
    CHROMA_DB_DIR = "chroma_db"

    # UI/Interaction
    LANGUAGE_HINDI_ENGLISH = True
