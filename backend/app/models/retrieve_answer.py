from pydantic import BaseModel


class RetrieveAnswerRequest(BaseModel):
    query: str