import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'news_pulse.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database successfully initialized!")

def save_news(articles):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    saved_count = 0
    for article in articles:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO news (title, link, description)
                VALUES (?, ?, ?)
            ''', (article['title'], article['link'], article['description']))
            
            if cursor.rowcount > 0:
                saved_count += 1
        except Exception as e:
            print(f"Error saving data: {e}")
            
    conn.commit()
    conn.close()
    print(f"Successfully saved {saved_count} new articles to the database.")
