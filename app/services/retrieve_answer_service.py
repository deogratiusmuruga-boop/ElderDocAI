import ollama

MODEL_NAME = "llama3.2:3b"
from app.services.retrieval_service import vector_store


def retrieve_and_answer(query: str):
    """
    Retrieve the most relevant document chunks and generate
    a grounded answer using Llama.
    """

    # Retrieve top matching chunks
    results = vector_store.search(query)

    if not results:
        return {
            "answer": "I couldn't find any relevant information in the indexed documents.",
            "sources": []
        }

    # Combine retrieved chunks into evidence
    evidence = "\n\n".join(
        item["chunk"]
        for item in results
    )

    # Build grounded prompt
    prompt = f"""
You are ElderDocAI, an AI assistant designed for elderly users.

Answer ONLY using the evidence below.

If the evidence does not contain the answer,
say:

"I could not find that information in the uploaded document."

Do NOT invent information.

Explain the answer using simple language.

====================
Evidence
====================

{evidence}

====================
Question
====================

{query}

====================
Answer
====================
"""

    # Ask Llama
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    return {
        "answer": answer,
        "sources": results
    }