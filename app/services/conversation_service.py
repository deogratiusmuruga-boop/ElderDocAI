import json

import ollama

MODEL_NAME = "llama3.2:3b"


def ask_with_context(processed_file_path: str, question: str, history: list):
    """
    Answer a question using the processed document and prior conversation turns.
    """

    with open(processed_file_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    conversation_context = ""
    if history:
        conversation_context = "\n".join(
            f"User: {entry.get('question', '')}\nAssistant: {entry.get('answer', '')}"
            for entry in history
            if isinstance(entry, dict)
        )

    prompt = f"""
You are a careful assistant for elderly users.
Answer the question using ONLY the information in the provided document.
Use the conversation history to resolve follow-up questions, but do not invent facts.
If the answer is not clearly stated, say that clearly.
Return valid JSON with this structure:

{{
  "answer": "",
  "source_sentence": ""
}}

Document:
{document_text}

Conversation history:
{conversation_context}

Question:
{question}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    payload = response["message"]["content"]

    if isinstance(payload, str):
        try:
            parsed = json.loads(payload)
        except json.JSONDecodeError:
            parsed = {"answer": payload, "source_sentence": ""}
    else:
        parsed = payload

    return {
        "answer": parsed.get("answer", ""),
        "source_sentence": parsed.get("source_sentence", ""),
    }
