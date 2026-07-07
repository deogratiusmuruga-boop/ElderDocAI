from fastapi import APIRouter, HTTPException

from app.services.terminology_service import explain_term

router = APIRouter()


@router.get("/explain-term")
async def explain_term_endpoint(term: str):
    """
    Return a simple explanation for a difficult term.
    """

    if not term or not term.strip():
        raise HTTPException(
            status_code=400,
            detail="Term cannot be empty."
        )

    try:
        return {
            "success": True,
            **explain_term(term),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Term explanation failed: {str(exc)}"
        )
