def build_action_dashboard(analysis: dict) -> dict:
    """
    Build a priority-aware, elderly-friendly dashboard from analysis data.
    The layout adapts to the content of any document instead of assuming fixed time buckets.
    """

    def normalize_items(items):
        if not items:
            return []
        if isinstance(items, list):
            return [str(item) for item in items if str(item).strip()]
        return [str(items)]

    actions = normalize_items(analysis.get("important_actions"))
    dates = normalize_items(analysis.get("important_dates"))
    warnings = normalize_items(analysis.get("warnings"))
    appointments = normalize_items(analysis.get("appointments"))
    medications = normalize_items(analysis.get("medications"))
    contacts = normalize_items(analysis.get("contacts"))
    follow_up_questions = normalize_items(analysis.get("follow_up_questions"))

    sections = []

    if actions or warnings or appointments:
        sections.append({
            "title": "What You Need to Know First",
            "icon": "🔴",
            "items": [
                {"text": item, "priority": "high"}
                for item in actions[:3]
            ] + [
                {"text": item, "priority": "critical"}
                for item in warnings[:3]
            ] + [
                {"text": item, "priority": "high"}
                for item in appointments[:3]
            ],
        })

    if dates or appointments:
        sections.append({
            "title": "Upcoming Dates",
            "icon": "📅",
            "items": [
                {"text": item, "priority": "medium"}
                for item in dates[:4]
            ] + [
                {"text": item, "priority": "medium"}
                for item in appointments[:4]
            ],
        })

    if medications:
        sections.append({
            "title": "Medicines",
            "icon": "💊",
            "items": [
                {"text": item, "priority": "medium"}
                for item in medications[:4]
            ],
        })

    if warnings:
        sections.append({
            "title": "Important Warnings",
            "icon": "⚠",
            "items": [
                {"text": item, "priority": "critical"}
                for item in warnings[:4]
            ],
        })

    if contacts:
        sections.append({
            "title": "Useful Contacts",
            "icon": "📞",
            "items": [
                {"text": item, "priority": "medium"}
                for item in contacts[:4]
            ],
        })

    if follow_up_questions:
        sections.append({
            "title": "You Can Ask Me",
            "icon": "💬",
            "items": [
                {"text": item, "priority": "low"}
                for item in follow_up_questions[:4]
            ],
        })

    if not sections:
        sections.append({
            "title": "Document Summary",
            "icon": "📄",
            "items": [
                {"text": analysis.get("simple_summary") or "No additional details available.", "priority": "medium"}
            ],
        })

    plain_text_lines = ["📄 Your Document Has Been Analyzed"]
    for section in sections:
        plain_text_lines.append(section["title"])
        for item in section["items"]:
            plain_text_lines.append(f"- {item['text']}")

    return {
        "title": "Priority-Aware Dashboard",
        "sections": sections,
        "plain_text": "\n".join(plain_text_lines),
    }
