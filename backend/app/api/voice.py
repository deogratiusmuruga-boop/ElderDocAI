import os

from fastapi import APIRouter, HTTPException

from app.services.voice_service import build_voice_ready_text

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.get("/voice/{document_id}")
async def get_voice_ready_text(document_id: str):
    """
    Return a simple, speech-friendly text version of the processed document.
    """

    processed_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")

    if not os.path.exists(processed_path):
        raise HTTPException(
            status_code=404,
            detail="Processed document not found."
        )

    try:
        voice_text = build_voice_ready_text(processed_path)
        return {
            "success": True,
            "document_id": document_id,
            "voice_ready_text": voice_text,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Voice text generation failed: {str(exc)}"
        )
