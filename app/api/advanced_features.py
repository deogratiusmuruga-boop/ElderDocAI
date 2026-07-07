import os

from fastapi import APIRouter, HTTPException

from app.services.ocr_service import extract_text_with_ocr
from app.services.reminder_service import generate_reminders
from app.services.retrieval_service import vector_store

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/ocr/{document_id}")
async def ocr_document(document_id: str):
    """
    Run a lightweight OCR placeholder for a processed document path.
    """

    file_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Processed document not found.")

    return {"success": True, "ocr_text": extract_text_with_ocr(file_path)}


@router.post("/index-document/{document_id}")
async def index_document(document_id: str):
    """
    Index processed document text into a simple retrieval store.
    """

    file_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Processed document not found.")

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    vector_store.add_document(document_id, text)

    return {"success": True, "document_id": document_id, "chunks_indexed": len(vector_store._documents[document_id])}


@router.post("/retrieve")
async def retrieve(query: str):
    """
    Retrieve relevant chunks from the simple vector store.
    """

    if not query or not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    return {"success": True, "results": vector_store.search(query)}


@router.post("/reminders")
async def reminders(payload: dict):
    """
    Generate reminder candidates from extracted text.
    """

    text = payload.get("text", "")
    if not isinstance(text, str) or not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    return {"success": True, "reminders": generate_reminders(text)}
