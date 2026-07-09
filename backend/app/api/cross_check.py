import os

from fastapi import APIRouter, HTTPException

from app.services.cross_check_service import cross_check_analysis

router = APIRouter()

PROCESSED_FOLDER = "processed_documents"


@router.post("/cross-check-analysis/{document_id}")
async def cross_check_analysis_endpoint(document_id: str, payload: dict):
    """
    Verify extracted analysis items against the processed document text.
    """

    processed_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.txt")

    if not os.path.exists(processed_path):
        raise HTTPException(
            status_code=404,
            detail="Processed document not found."
        )

    try:
        with open(processed_path, "r", encoding="utf-8") as file:
            document_text = file.read()

        analysis = payload.get("analysis", payload)
        verified_analysis = cross_check_analysis(analysis, document_text)

        return {
            "success": True,
            "document_id": document_id,
            "analysis": verified_analysis,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Cross-check analysis failed: {str(exc)}"
        )
