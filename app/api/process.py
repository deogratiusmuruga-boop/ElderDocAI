import os

from fastapi import APIRouter, HTTPException

from app.services.document_processor import process_document

router = APIRouter()

UPLOAD_FOLDER = "uploaded_documents"


@router.post("/process/{document_id}")
async def process_uploaded_document(document_id: str):
    """
    Process an uploaded document:
    - Locate the uploaded file
    - Extract text
    - Clean the text
    - Save it to processed_documents/
    """

    # Find the uploaded file using its UUID
    matching_files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if f.startswith(document_id)
    ]

    if not matching_files:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        matching_files[0]
    )

    try:
        result = process_document(file_path)

        return {
            "success": True,
            "message": "Document processed successfully.",
            **result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )