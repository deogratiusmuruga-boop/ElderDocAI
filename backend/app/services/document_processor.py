import os

from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text

PROCESSED_FOLDER = "processed_documents"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def process_document(file_path: str):

    extension = os.path.splitext(file_path)[1].lower()

    if extension != ".pdf":
        raise ValueError("Unsupported document type.")

    # Extract
    extracted_text = extract_text_from_pdf(file_path)

    # Clean
    cleaned_text = clean_text(extracted_text)

    # Same UUID as uploaded file
    document_id = os.path.splitext(os.path.basename(file_path))[0]

    output_path = os.path.join(
        PROCESSED_FOLDER,
        f"{document_id}.txt"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    return {
        "document_id": document_id,
        "processed_file": output_path,
        "text_length": len(cleaned_text),
        "status": "processed"
    }