from fastapi import FastAPI

from app.api.analyze import router as analyze_router
from app.api.advanced_features import router as advanced_features_router
from app.api.ask import router as ask_router
from app.api.conversation import router as conversation_router
from app.api.confidence import router as confidence_router
from app.api.cross_check import router as cross_check_router
from app.api.dashboard import router as dashboard_router
from app.api.grounded_answer import router as grounded_answer_router
from app.api.prioritization import router as prioritization_router
from app.api.session_conversation import router as session_conversation_router
from app.api.summary import router as summary_router
from app.api.terminology import router as terminology_router
from app.api.upload import router as upload_router
from app.api.process import router as process_router
from app.api.voice import router as voice_router
app = FastAPI(
    title="ElderDocAI",
    description="AI-powered document understanding service for elderly users.",
    version="0.1.0",
)

app.include_router(upload_router)
app.include_router(process_router)
app.include_router(analyze_router)
app.include_router(ask_router)
app.include_router(conversation_router)
app.include_router(session_conversation_router)
app.include_router(grounded_answer_router)
app.include_router(summary_router)
app.include_router(dashboard_router)
app.include_router(confidence_router)
app.include_router(cross_check_router)
app.include_router(terminology_router)
app.include_router(prioritization_router)
app.include_router(advanced_features_router)
app.include_router(voice_router)

@app.get("/")
async def root():
    return {
        "project": "ElderDocAI",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
