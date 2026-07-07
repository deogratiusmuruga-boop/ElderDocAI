from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.upload_service import save_uploaded_file

router = APIRouter()


ALLOWED_TYPES = [
    "application/pdf",
    "image/jpeg",
    "image/png",
]


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document.
    """

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, JPG, and PNG files are allowed.",
        )

    result = save_uploaded_file(file)

    return {
        "status": "uploaded successfully",
        **result
    }