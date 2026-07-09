def build_voice_ready_text(processed_file_path: str) -> str:
    """
    Read the processed text and return a clean, speech-friendly version.
    """

    with open(processed_file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()

    if not text:
        return "No text available."

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " ".join(lines)
