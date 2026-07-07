import os

from fastapi import APIRouter, HTTPException

from app.services.question_answering_service import answer_question

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/ask/{document_id}")
async def ask_document_question(document_id: str, question: str):
    """
    Answer a question about a processed document using the extracted text.
    """

    processed_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")

    if not os.path.exists(processed_path):
        raise HTTPException(
            status_code=404,
            detail="Processed document not found."
        )

    if not question or not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        result = answer_question(processed_path, question)
        return {
            "success": True,
            "document_id": document_id,
            **result,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Question answering failed: {str(exc)}"
        )
