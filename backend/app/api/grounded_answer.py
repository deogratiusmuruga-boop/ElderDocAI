import os

from fastapi import APIRouter, HTTPException

from app.services.grounded_answer_service import answer_with_source

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/grounded-answer/{document_id}")
async def grounded_answer(document_id: str, question: str):
    """
    Return an answer plus the supporting sentence from the processed document.
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
        result = answer_with_source(processed_path, question)
        return {
            "success": True,
            "document_id": document_id,
            **result,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Grounded answer generation failed: {str(exc)}"
        )
