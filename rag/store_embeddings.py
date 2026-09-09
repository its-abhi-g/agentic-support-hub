import os
import json
import mysql.connector

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

cursor.execute(
    "SELECT id, content FROM knowledge"
)

records = cursor.fetchall()

for record in records:

    article_id = record[0]
    content = record[1]

    vector = model.encode(content)

    vector_json = json.dumps(
        vector.tolist()
    )

    update_query = """
    UPDATE knowledge
    SET embedding=%s
    WHERE id=%s
    """

    cursor.execute(
        update_query,
        (
            vector_json,
            article_id
        )
    )

connection.commit()

print("Embeddings stored successfully.")


''' this script will do the following:
Read all knowledge records
Generate Embedding
Store Embedding in DB  ''' 