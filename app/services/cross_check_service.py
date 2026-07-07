import re


def cross_check_analysis(analysis: dict, document_text: str) -> dict:
    """
    Verify extracted facts against the source document text.
    Returns a copy of the analysis with a verified flag for each field item.
    """

    if not isinstance(document_text, str):
        return analysis

    normalized_text = document_text.lower()
    verified_analysis = dict(analysis)

    for field in ["important_actions", "important_dates", "medications", "appointments", "contacts", "warnings", "follow_up_questions"]:
        if field in verified_analysis:
            items = verified_analysis[field]
            verified_items = []
            for item in items:
                if isinstance(item, dict):
                    value = item.get("value") or item.get("text") or item.get("date") or ""
                    label = str(value).strip()
                else:
                    label = str(item).strip()

                if label:
                    verified = bool(re.search(re.escape(label.lower()), normalized_text))
                else:
                    verified = False

                if isinstance(item, dict):
                    entry = dict(item)
                    entry["verified"] = verified
                    verified_items.append(entry)
                else:
                    verified_items.append({
                        "value": label,
                        "verified": verified,
                    })
            verified_analysis[field] = verified_items

    return verified_analysis
