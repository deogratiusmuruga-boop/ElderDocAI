from pydantic import BaseModel
from typing import List


class ConversationRequest(BaseModel):
    question: str
    history: List[dict] = []
