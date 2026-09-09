import os
import json
import mysql.connector
import numpy as np

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_best_match(question):

    question_vector = model.encode(question)

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            title,
            product,
            content,
            embedding
        FROM knowledge
        """
    )

    records = cursor.fetchall()

    best_score = -1
    best_match = None

    for row in records:

        embedding = np.array(
            json.loads(row[3])
        )

        score = cosine_similarity(
            [question_vector],
            [embedding]
        )[0][0]

        if score > best_score:

            best_score = score
            best_match = {
                "title": row[0],
                "product": row[1],
                "content": row[2],
                "score": score
            }

    cursor.close()
    connection.close()

    return best_match