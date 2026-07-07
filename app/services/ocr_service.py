import os


def extract_text_with_ocr(file_path: str) -> str:
    """
    Lightweight OCR placeholder.
    Returns the file path as a marker when OCR is unavailable.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    return f"OCR placeholder for {file_path}"
