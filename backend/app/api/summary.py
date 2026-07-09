from fastapi import APIRouter, HTTPException

from app.services.document_summary_service import build_document_status

router = APIRouter()


@router.post("/summary-status")
async def summary_status(payload: dict):
    """
    Build a friendly UI status summary from the analysis payload.
    """

    try:
        analysis = payload.get("analysis", payload)
        return {
            "success": True,
            **build_document_status(analysis),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Summary status generation failed: {str(exc)}"
        )
