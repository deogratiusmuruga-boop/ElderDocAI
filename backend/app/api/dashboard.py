from fastapi import APIRouter, HTTPException

from app.services.action_dashboard_service import build_action_dashboard

router = APIRouter()


@router.post("/action-dashboard")
async def action_dashboard(payload: dict):
    """
    Build a simple action dashboard from the analysis payload.
    """

    try:
        analysis = payload.get("analysis", payload)
        return {
            "success": True,
            **build_action_dashboard(analysis),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Action dashboard generation failed: {str(exc)}"
        )
