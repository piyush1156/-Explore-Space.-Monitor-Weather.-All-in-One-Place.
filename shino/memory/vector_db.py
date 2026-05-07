import chromadb
from chromadb.config import Settings
from shino.config.config import Config
from shino.core.logger import logger

class VectorMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=Config.CHROMA_DB_DIR)
        self.collection = self.client.get_or_create_collection(name="shino_memory")

    def add_memory(self, text: str, metadata: dict = None):
        try:
            self.collection.add(
                documents=[text],
                metadatas=[metadata] if metadata else [{"source": "conversation"}],
                ids=[f"id_{self.collection.count()}"]
            )
        except Exception as e:
            logger.error(f"Error adding to vector memory: {e}")

    def search_memory(self, query: str, n_results=3):
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results
            )
            return results['documents'][0] if results['documents'] else []
        except Exception as e:
            logger.error(f"Error searching vector memory: {e}")
            return []

vector_memory = VectorMemory()
