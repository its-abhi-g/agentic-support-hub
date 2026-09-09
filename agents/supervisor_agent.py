from rag.retriever import retrieve_best_match
from services.llm_service import generate_response
from database.case_service import (
    create_case,
    update_response
)


import random


def classify_product(question):

    question = question.lower()

    codex_keywords = [
        "codex",
        "coding assistant",
        "code generation",
        "debugging",
        "developer tool",
        "install codex"
    ]

    api_keywords = [
        "api",
        "api key",
        "developer api",
        "platform"
    ]

    chatgpt_keywords = [
        "chatgpt",
        "chat gpt",
        "enterprise"
    ]

    partner_keywords = [
        "partner u",
        "partneru",
        "training"
    ]

    if any(word in question for word in codex_keywords):
        return "Codex"

    if any(word in question for word in api_keywords):
        return "OpenAI API"

    if any(word in question for word in chatgpt_keywords):
        return "ChatGPT"

    if any(word in question for word in partner_keywords):
        return "Partner U"

    return "Unknown"


def generate_case_id():

    return f"CASE-{random.randint(10000,99999)}"


question = input(
    "Ask Question: "
)

product = classify_product(question)

case_id = generate_case_id()

create_case(
    case_id,
    product,
    question
)

article = retrieve_best_match(question)

ai_response = generate_response(
    question,
    article["content"],
    case_id
)

update_response(
    case_id,
    ai_response
)


print("\n" + "=" * 60)

print("CASE CREATED")

print("=" * 60)

print("Case ID :", case_id)

print("Product :", product)

print()

print("Knowledge Article:")
print(article["title"])


print()

print("AI RESPONSE")

print("-" * 60)

print(ai_response)

print()

print(
    "Confidence:",
    round(article["score"], 3)
)
