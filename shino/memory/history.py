import sqlite3
from typing import List, Dict
from shino.config.config import Config

class ConversationHistory:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_PATH)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def add_message(self, role: str, content: str):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO history (role, content) VALUES (?, ?)', (role, content))
        self.conn.commit()

    def get_recent(self, limit=10) -> List[Dict[str, str]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT role, content FROM history ORDER BY timestamp DESC LIMIT ?', (limit,))
        rows = cursor.fetchall()
        return [{"role": row[0], "content": row[1]} for row in reversed(rows)]

history_db = ConversationHistory()
