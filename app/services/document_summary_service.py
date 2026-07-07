def build_document_status(analysis: dict) -> dict:
    """
    Turn structured analysis into a friendly status summary for the UI.
    """

    document_type = str(analysis.get("document_type", "Document")).strip() or "Document"
    purpose = str(analysis.get("purpose", "")).strip()
    urgency = str(analysis.get("urgency", "Low")).strip() or "Low"
    warnings = analysis.get("warnings") or []
    medications = analysis.get("medications") or []
    appointments = analysis.get("appointments") or []
    actions = analysis.get("important_actions") or []

    confidence = "High" if document_type and purpose else "Medium"
    if warnings:
        confidence = "High"

    summary_lines = [
        f"{document_type}",
        f"Confidence: {confidence}",
    ]

    if medications:
        summary_lines.append("Contains: ✓ Medication")
    if appointments:
        summary_lines.append("Contains: ✓ Appointment")
    if actions:
        summary_lines.append("Contains: ✓ Action")
    if warnings:
        summary_lines.append("Contains: ✓ Warning")

    return {
        "document_type": document_type,
        "purpose": purpose,
        "urgency": urgency,
        "confidence": confidence,
        "status_text": "\n".join(summary_lines),
        "has_medications": bool(medications),
        "has_appointments": bool(appointments),
        "has_actions": bool(actions),
        "has_warnings": bool(warnings),
    }
