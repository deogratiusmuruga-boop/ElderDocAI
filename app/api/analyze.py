import os

from fastapi import APIRouter, HTTPException

from app.services.analysis_service import analyze_document

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/analyze/{document_id}")
async def analyze_uploaded_document(document_id: str):
    """
    Analyze a processed document.
    The API route only receives the request and returns the response.
    """

    processed_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")

    if not os.path.exists(processed_path):
        raise HTTPException(
            status_code=404,
            detail="Processed document not found."
        )

    try:
        result = analyze_document(processed_path, document_id)
        return {
            "success": True,
            "message": "Document analyzed successfully.",
            **result
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(exc)}"
        )
