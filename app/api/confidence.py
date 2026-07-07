from fastapi import APIRouter, HTTPException

from app.services.confidence_service import build_confidence_annotated_analysis

router = APIRouter()


@router.post("/confidence-analysis")
async def confidence_analysis(payload: dict):
    """
    Annotate analysis payload fields with confidence scores.
    """

    try:
        analysis = payload.get("analysis", payload)
        return {
            "success": True,
            "analysis": build_confidence_annotated_analysis(analysis),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Confidence annotation failed: {str(exc)}"
        )
