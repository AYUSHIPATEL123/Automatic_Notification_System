import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "learning.db"


def get_conn():
    return sqlite3.connect(DB_PATH)

def create_table():

    conn = get_conn()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category Text NOT NULL,
            title TEXT NOT NULL,  
            description TEXT NOT NULL,
            source TEXT,
            show_count INTEGER DEFAULT 0,
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(category,title)             
                   ) 
"""        
    )

    conn.commit()

    conn.close()

if __name__  == "__main__":
    create_table()

    print("database created successfully.....")
