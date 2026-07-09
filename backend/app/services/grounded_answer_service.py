import os

import ollama

MODEL_NAME = "llama3.2:3b"


def answer_with_source(processed_file_path: str, question: str):
    """
    Answer a question using the processed document and include the supporting sentence.
    """

    with open(processed_file_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    prompt = f"""
You are a careful assistant for elderly users.
Answer the question using ONLY the information in the provided document.
If the answer is not clearly stated, say that clearly.
Return valid JSON with this structure:

{{
  "answer": "",
  "source_sentence": ""
}}

Document:
{document_text}

Question:
{question}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    payload = response["message"]["content"]

    if isinstance(payload, str):
        import json

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
