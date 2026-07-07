import os

from fastapi import APIRouter, HTTPException

from app.services.conversation_service import ask_with_context

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/conversation/{document_id}")
async def conversation(document_id: str, question: str, history: list | None = None):
    """
    Answer a question using the processed document and prior conversation turns.
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
        result = ask_with_context(processed_path, question, history or [])
        return {
            "success": True,
            "document_id": document_id,
            **result,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Conversation answering failed: {str(exc)}"
        )
