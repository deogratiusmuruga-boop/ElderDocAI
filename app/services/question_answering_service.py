import os

import ollama

MODEL_NAME = "llama3"


def answer_question(processed_file_path: str, question: str):
    """
    Answer a question strictly from the processed document text.
    """

    with open(processed_file_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    prompt = f"""
You are a careful assistant for elderly users.
Answer the question using ONLY the information in the provided document.
If the answer is not clearly stated in the document, say that clearly.
Do not use general knowledge.

Document:
{document_text}

Question:
{question}

Return a short, clear answer.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response["message"]["content"]

    return {
        "answer": answer,
        "source": "processed_text",
    }
