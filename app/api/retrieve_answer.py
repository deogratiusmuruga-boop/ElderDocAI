from fastapi import APIRouter, HTTPException

from app.models.retrieve_answer import RetrieveAnswerRequest
from app.services.retrieve_answer_service import retrieve_and_answer
from pydantic import BaseModel


class RetrieveAnswerRequest(BaseModel):
    query: str
router = APIRouter()


@router.post("/retrieve-answer")
async def retrieve_answer(request: RetrieveAnswerRequest):

    try:
        result = retrieve_and_answer(request.query)

        return {
            "success": True,
            **result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )