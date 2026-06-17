import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

DB_PATH = "database/learning.db"

conn  = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

options = Options()

options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

url = r"https://stahlkitchens.com/blogs/news/10-basic-cutting-techniques#:~:text=Most%20likely%20considered,%2C%20and%20brunoise."

driver.get(url)
sleep(5)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")


driver.close()

added = 0

chhoping_cat = soup.find_all("h3")

print(chhoping_cat)
for cat in chhoping_cat:

    if len(cat) >= 1:
        
        description=cat.get_text()

        if len(description) < 2:
            continue

        try:

            conn.execute("""
                INSERT INTO TASKS(
                        category,
                        title,
                        description,
                        source 
                        )
                        VALUES(
                        ?,?,?,?
                        ) 
                        """,(
                            "Chhopping",
                            f"THIS WEEK'S {added} CHHOPPING CATEGORY IS: ",
                            description,
                            url
                        ))

            added += 1

            if added == 19:
                break

        except sqlite3.IntegrityError as e:
            pass 


conn.commit()
conn.close()


print(f"{added} chopping data added")
