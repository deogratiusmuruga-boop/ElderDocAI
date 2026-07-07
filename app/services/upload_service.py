import os
import uuid
import shutil
from fastapi import UploadFile

# Folder where uploaded files will be stored
UPLOAD_FOLDER = "uploaded_documents"

# Create folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_file(file: UploadFile):
    """
    Save an uploaded file and return metadata.
    """

    # Get file extension (.pdf, .jpg, etc.)
    extension = os.path.splitext(file.filename)[1]

    # Generate unique filename
    document_id = str(uuid.uuid4())
    stored_filename = f"{document_id}{extension}"

    # Full path
    file_path = os.path.join(UPLOAD_FOLDER, stored_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "document_id": document_id,
        "original_filename": file.filename,
        "stored_filename": stored_filename,
        "file_path": file_path,
        "content_type": file.content_type,
    }