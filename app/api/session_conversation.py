import os

from fastapi import APIRouter, HTTPException

from app.services.conversation_service import ask_with_context
from app.services.session_store import session_store

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/session-conversation/{document_id}/{session_id}")
async def session_conversation(document_id: str, session_id: str, question: str):
    """
    Answer a question using the processed document and the stored conversation history.
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
        history = session_store.get_history(session_id)
        result = ask_with_context(processed_path, question, history)
        session_store.append_turn(
            session_id,
            question,
            result.get("answer", ""),
            result.get("source_sentence", ""),
        )
        return {
            "success": True,
            "document_id": document_id,
            "session_id": session_id,
            **result,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Session conversation failed: {str(exc)}"
        )
