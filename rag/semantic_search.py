import os
import json
import mysql.connector
import numpy as np

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables
load_dotenv()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# User question
question = input("Ask question: ")

# Generate question embedding
question_vector = model.encode(question)

# Database connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

# Fetch knowledge articles
cursor.execute("""
    SELECT
        id,
        title,
        product,
        content,
        embedding
    FROM knowledge
""")

records = cursor.fetchall()

results = []

# Calculate similarity for every article
for row in records:

    article_id = row[0]
    title = row[1]
    product = row[2]
    content = row[3]
    embedding_json = row[4]

    embedding = np.array(
        json.loads(embedding_json)
    )

    score = cosine_similarity(
        [question_vector],
        [embedding]
    )[0][0]

    results.append({
        "id": article_id,
        "title": title,
        "product": product,
        "content": content,
        "score": score
    })

# Sort highest score first
results.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Best match
best_match = results[0]

print("\n" + "=" * 60)
print("BEST MATCH")
print("=" * 60)

print(f"Title      : {best_match['title']}")
print(f"Product    : {best_match['product']}")
print(f"Similarity : {best_match['score']:.3f}")

print("\nContent:")
print(best_match["content"])

print("\n" + "=" * 60)
print("TOP 5 RESULTS")
print("=" * 60)

for idx, result in enumerate(results[:5], start=1):

    print(
        f"{idx}. "
        f"{result['title']} "
        f"(Score: {result['score']:.3f})"
    )

# Close DB connection
cursor.close()
connection.close()