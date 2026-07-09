import json
import os

import ollama

MODEL_NAME = "llama3.2:3b"
PROCESSED_FOLDER = "processed_documents"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

SCHEMA_FIELDS = {
    "document_type": "",
    "purpose": "",
    "urgency": "Low",
    "quick_overview": "",
    "simple_summary": "",
    "important_actions": [],
    "important_dates": [],
    "medications": [],
    "appointments": [],
    "contacts": [],
    "warnings": [],
    "follow_up_questions": [],
}


def _normalize_analysis_payload(payload: dict) -> dict:
    normalized = dict(SCHEMA_FIELDS)

    if not isinstance(payload, dict):
        return normalized

    for key, default_value in SCHEMA_FIELDS.items():
        if key in payload:
            value = payload[key]
            if isinstance(default_value, list):
                normalized[key] = value if isinstance(value, list) else []
            elif isinstance(default_value, str):
                normalized[key] = value if isinstance(value, str) else ""
            else:
                normalized[key] = value
        else:
            normalized[key] = default_value

    urgency = str(normalized.get("urgency", "Low") or "Low").strip()
    if urgency.lower() not in {"low", "medium", "high"}:
        urgency = "Low"
    normalized["urgency"] = urgency.capitalize()

    return normalized


def analyze_document(processed_file_path: str, document_id: str):
    """
    Analyze a processed document using Llama 3.
    Save the structured JSON result and return metadata.
    """

    with open(processed_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    understanding_prompt = f"""
You are an AI assistant helping understand documents for elderly users.

Read the document below and return ONLY valid JSON with this structure:

{{
    "document_type":"",
    "purpose":"",
    "urgency":""
}}

Document:

{text}
"""

    understanding_response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": understanding_prompt
            }
        ]
    )

    understanding_payload = understanding_response["message"]["content"]

    if isinstance(understanding_payload, str):
        try:
            parsed_understanding = json.loads(understanding_payload)
        except json.JSONDecodeError:
            parsed_understanding = {"document_type": "", "purpose": "", "urgency": "Low"}
    else:
        parsed_understanding = understanding_payload

    explanation_prompt = f"""
You are an AI assistant helping elderly users understand documents.

Using the following understanding of the document:

{json.dumps(parsed_understanding, indent=2)}

Generate a clear and helpful elderly-friendly explanation.
Return ONLY valid JSON with this structure:

{{
    "quick_overview":"",
    "simple_summary":"",
    "important_actions":[],
    "important_dates":[],
    "medications":[],
    "appointments":[],
    "contacts":[],
    "warnings":[],
    "follow_up_questions":[]
}}

Original document text:

{text}
"""

    explanation_response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": explanation_prompt
            }
        ]
    )

    explanation_payload = explanation_response["message"]["content"]

    if isinstance(explanation_payload, str):
        try:
            parsed_explanation = json.loads(explanation_payload)
        except json.JSONDecodeError:
            parsed_explanation = {}
    else:
        parsed_explanation = explanation_payload

    combined_payload = {
        **parsed_understanding,
        **parsed_explanation,
    }

    normalized_payload = _normalize_analysis_payload(combined_payload)

    output_path = os.path.join(PROCESSED_FOLDER, f"{document_id}.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(normalized_payload, file, indent=2)

    return {
        "document_id": document_id,
        "analysis_file": output_path,
        "analysis": normalized_payload,
        "status": "analyzed"
    }