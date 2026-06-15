import sqlite3
from plyer import notification
import random

DB_PATH =  "database/learning.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
                SELECT id,title,description FROM TASKS WHERE category = "Shortcuts" AND show_count <= 2;
""")

data = cursor.fetchall()

if not data:
    print("No shortcuts available.")
    conn.close()
    exit()

# print(data)
short_cut  = random.choice(data)

notification.notify(
    title = "Today's Shortcut",
    message = f" {short_cut[1]} : {short_cut[2]}",
    timeout = 200
)


cursor.execute("""
                UPDATE TASKS SET show_count = show_count + 1 WHERE id = ?
""",
(short_cut[0],)
)

conn.commit()
conn.close()

