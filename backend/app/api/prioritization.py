from fastapi import APIRouter, HTTPException

from app.services.prioritization_service import prioritize_items

router = APIRouter()


@router.post("/prioritize")
async def prioritize(payload: dict):
    """
    Rank analysis items by urgency for elderly-friendly presentation.
    """

    try:
        analysis = payload.get("analysis", payload)
        return {
            "success": True,
            **prioritize_items(analysis),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Prioritization failed: {str(exc)}"
        )
