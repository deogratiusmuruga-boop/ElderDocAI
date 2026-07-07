import fitz  # PyMuPDF


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a digital PDF.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text