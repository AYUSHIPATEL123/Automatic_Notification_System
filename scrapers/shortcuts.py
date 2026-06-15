from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


DB_PATH =  "database/learning.db"

options = Options()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

url  = "https://www.computerhope.com/shortcut.htm"

driver.get(url)

time.sleep(5)



# headers = {
#     "User-Agent": (
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/137.0.0.0 Safari/537.36"
#     )

# }

# response = requests.get(url,headers=headers)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

added = 0

driver.quit()

rows  = soup.find_all("tr")
title = soup.find_all("h1")[0].get_text(strip=True)

for row in rows:

    cols = row.find_all('td')

    if len(cols) >= 2:
        shortcut  = cols[0].get_text(strip=True)
        description = cols[1].get_text(strip=True)

        if len(shortcut) < 2:
            continue


        try:

            cursor.execute("""
                INSERT INTO tasks(
                        category,
                        title,
                        description,
                        source
                          
                           )
                        VALUES(
                           ?,?,?,?
                           )    
                    """,(
                        "Shortcuts",
                        shortcut,
                        description,
                        url
                    ))
            
            added += 1
            
        except sqlite3.IntegrityError as e:
            pass    

conn.commit()
conn.close()

print(f"{added} shortcuts added.")













# print(soup.title.text)
# print(html[:1000])
# print(soup.prettify()[:10000])
# tables = soup.find_all('table')
# print(len(tables))
# print(tables[0].prettify()[:2000])
# for row in tables[0].find_all(['tr']):
#     cols = [c.get_text(strip=True) for c in row.find_all(["th",'td'])]
#     print(cols)





