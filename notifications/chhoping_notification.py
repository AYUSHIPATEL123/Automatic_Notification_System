import sqlite3
from plyer import notification
import random

DB_PATH = "database/learning.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
            SELECT id,title,description FROM TASKS WHERE category = "Chhopping" AND show_count <= 2;
""")

data = cursor.fetchall()

if not data:
    print("data of Chhopping is not available")
    conn.close()
    exit()

chopping_data = random.choice(data)

notification.notify(
    title=chopping_data[1],
    message=chopping_data[2],
    timeout=200
)
print(chopping_data[0])
cursor.execute("""
            UPDATE TASKS SET show_count = show_count + 1 WHERE id = ? 
""",(chopping_data[0],)
)

conn.commit()
conn.close()