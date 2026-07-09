def prioritize_items(analysis: dict) -> dict:
    """
    Rank extracted items into urgency bands for elderly-friendly presentation.
    """

    urgent_items = []
    important_items = []
    informational_items = []

    for item in analysis.get("warnings") or []:
        urgent_items.append({"type": "warning", "text": str(item)})

    for item in analysis.get("important_actions") or []:
        urgent_items.append({"type": "action", "text": str(item)})

    for item in analysis.get("appointments") or []:
        urgent_items.append({"type": "appointment", "text": str(item)})

    for item in analysis.get("medications") or []:
        important_items.append({"type": "medication", "text": str(item)})

    if analysis.get("important_actions"):
        for item in analysis.get("important_actions") or []:
            if isinstance(item, str) and "medicine" in item.lower():
                important_items.append({"type": "medication", "text": str(item)})

    for item in analysis.get("important_dates") or []:
        important_items.append({"type": "date", "text": str(item)})

    for item in analysis.get("simple_summary") or []:
        informational_items.append({"type": "summary", "text": str(item)})

    if analysis.get("simple_summary") and isinstance(analysis.get("simple_summary"), str):
        informational_items.append({"type": "summary", "text": str(analysis.get("simple_summary"))})

    return {
        "urgent": urgent_items,
        "important": important_items,
        "informational": informational_items,
        "summary_text": "\n".join(
            [f"🔴 {item['text']}" for item in urgent_items[:5]]
            + [f"🟡 {item['text']}" for item in important_items[:5]]
            + [f"🟢 {item['text']}" for item in informational_items[:5]]
        ),
    }
