import re


def clean_text(text: str) -> str:
    """
    Clean extracted text by removing unnecessary whitespace.
    """

    # Replace multiple spaces with one
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()