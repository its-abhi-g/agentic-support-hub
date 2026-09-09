import ollama


def generate_response(question, article, case_id):

    prompt = f"""
You are an HCL OpenAI Support Assistant.

Use ONLY the knowledge below.

User Question:
{question}

Knowledge Article:
{article}

Case ID:
{case_id}

Instructions:
1. Use ONLY the information present in the Knowledge Article.
2. Never add websites, links, approvals, timelines or steps that are not explicitly mentioned.
3. If information is missing, say:
   "The knowledge article does not provide additional details."
4. Mention the Case ID.
5. Keep response concise and professional.
6. Do not assume or invent facts.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]