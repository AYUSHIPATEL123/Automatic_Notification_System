import sqlite3

DB_PATH = 'database/learning.db'

conn  = sqlite3.connect(DB_PATH)

cursor = conn.cursor()


cursor.execute("""
            SELECT category,title FROM TASKS LIMIT 10;
"""
)

for row in cursor.fetchall():
    print(row)
    
conn.commit()
conn.close()
