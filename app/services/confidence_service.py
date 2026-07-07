def attach_confidence(items, default_confidence=0.85):
    """
    Convert a list of strings into a list of objects with confidence scores.
    """

    if not items:
        return []

    if isinstance(items, list):
        result = []
        for item in items:
            if isinstance(item, dict):
                entry = dict(item)
                entry.setdefault("confidence", default_confidence)
                result.append(entry)
            else:
                result.append({
                    "value": str(item),
                    "confidence": default_confidence,
                })
        return result

    return []


def build_confidence_annotated_analysis(analysis: dict) -> dict:
    """
    Annotate key analysis fields with confidence scores.
    """

    annotated = dict(analysis)

    for field in ["important_actions", "important_dates", "medications", "appointments", "contacts", "warnings", "follow_up_questions"]:
        if field in annotated:
            annotated[field] = attach_confidence(annotated[field])

    return annotated
