import json
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

with open(
    "documents/knowledge_seed.json",
    "r",
    encoding="utf-8"
) as file:
    articles = json.load(file)

for article in articles:

    sql = """
    INSERT INTO knowledge
    (title, product, content)
    VALUES (%s,%s,%s)
    """

    values = (
        article["title"],
        article["product"],
        article["content"]
    )

    cursor.execute(sql, values)

connection.commit()

print("Knowledge articles loaded successfully.")