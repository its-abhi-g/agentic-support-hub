from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sample_text = """
User must submit Codex App Request Form.
"""

embedding = model.encode(sample_text)

print("Embedding Length:", len(embedding))