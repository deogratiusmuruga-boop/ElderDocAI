import re


def generate_reminders(text: str) -> list[dict]:
    """
    Extract simple reminder candidates from text such as dates and deadlines.
    """

    reminders = []
    for match in re.finditer(r"\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}\b", text, re.IGNORECASE):
        reminders.append({
            "text": match.group(0),
            "type": "date",
        })

    return reminders
