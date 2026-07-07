from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="ElderDocAI",
    description="AI-powered document understanding service for elderly users.",
    version="0.1.0",
)

app.include_router(upload_router)


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