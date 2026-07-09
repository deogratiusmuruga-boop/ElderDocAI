COMMON_TERMS = {
    "hypertension": "High blood pressure.",
    "benign": "Not cancer.",
    "malignant": "Cancerous.",
    "diagnosis": "A doctor’s explanation of what illness a person has.",
    "prognosis": "The expected course of an illness.",
    "medication": "Medicine used to treat an illness.",
    "appointment": "A planned meeting with a doctor or clinic.",
    "symptom": "A sign that you may be feeling unwell.",
    "treatment": "Care given to help someone get better.",
    "inflammation": "Swelling and irritation in the body.",
}


def explain_term(term: str) -> dict:
    """
    Return a simple explanation for a difficult term.
    """

    normalized = (term or "").strip().lower()
    explanation = COMMON_TERMS.get(normalized)

    if explanation:
        return {
            "term": term,
            "explanation": explanation,
            "found": True,
        }

    return {
        "term": term,
        "explanation": "No simple explanation is available yet.",
        "found": False,
    }
