# core/indexer.py (updated)
import sqlite3
from datetime import datetime

conn = sqlite3.connect('data/leaks.db', check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS leaks
                      (id INTEGER PRIMARY KEY, email TEXT, url TEXT, timestamp TEXT,
                      UNIQUE(email, url))''')  # Prevent duplicates
    conn.commit()

def store_leaks(results):
    for email in results['emails']:
        try:
            cursor.execute("INSERT OR IGNORE INTO leaks (email, url, timestamp) VALUES (?, ?, ?)",
                           (email, results['url'], datetime.now().isoformat()))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    conn.commit()