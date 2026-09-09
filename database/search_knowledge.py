import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

keyword = input("Enter search term: ")

query = """
SELECT title, content
FROM knowledge
WHERE content LIKE %s
"""

cursor.execute(
    query,
    (f"%{keyword}%",)
)

results = cursor.fetchall()

for row in results:
    print("\nTITLE:", row[0])
    print("CONTENT:", row[1])
