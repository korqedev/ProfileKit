import sqlite3
from pathlib import Path

DB_PATH = Path("profilekit.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            display_name TEXT,
            bio TEXT,
            status TEXT,
            avatar_path TEXT
        )
    """)

    conn.commit()
    conn.close()
