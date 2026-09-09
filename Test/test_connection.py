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

""" Test connection 

    if connection.is_connected():
        print("✅ Database connected successfully!")

except Exception as e:
    print("❌ Error:", e)

"""

cursor = connection.cursor()

query = """
INSERT INTO cases
(case_id, product, category, status, question)
VALUES (%s,%s,%s,%s,%s)
"""

values = (
    "CASE-001",
    "Codex",
    "Access",
    "Open",
    "I cannot access Codex"
)

cursor.execute(query, values)

connection.commit()

print("✅ Case inserted successfully!")