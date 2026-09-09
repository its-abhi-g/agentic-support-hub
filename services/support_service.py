from database.case_service import (
    create_case,
    update_response,
    create_escalation
)

from rag.retriever import retrieve_best_match
from services.llm_service import generate_response

import random


def classify_product(question):

    question = question.lower()

    codex_keywords = [
        "codex",
        "coding assistant",
        "code generation",
        "debugging",
        "developer tool",
        "install codex",
        "coding ai",
        "ai coding",
        "code ai",
        "programming assistant",
        "developer assistant",
        "code intelligence",
        "ai intelligence"
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


def process_question(question):

    product = classify_product(question)

    case_id = generate_case_id()

    create_case(
        case_id,
        product,
        question
    )

    article = retrieve_best_match(question)

    confidence = round(
        article["score"],
        3
    )

    # Low confidence → Escalate
    if confidence < 0.40:

        create_escalation(
            case_id,
            f"Low confidence match: {confidence}"
        )

        return {
            "case_id": case_id,
            "product": product,
            "article": article["title"],
            "response":
                "This issue requires human review. "
                "The request has been escalated.",
            "confidence": confidence,
            "escalated": True
        }

    # High confidence → AI answer
    ai_response = generate_response(
        question,
        article["content"],
        case_id
    )

    update_response(
        case_id,
        ai_response
    )

    return {
        "case_id": case_id,
        "product": product,
        "article": article["title"],
        "response": ai_response,
        "confidence": confidence,
        "escalated": False
    }