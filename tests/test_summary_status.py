from fastapi.testclient import TestClient

from app.main import app


def test_summary_status_endpoint_builds_user_friendly_summary():
    client = TestClient(app)
    response = client.post(
        "/summary-status",
        json={
            "analysis": {
                "document_type": "Hospital Discharge Summary",
                "purpose": "Inform the patient",
                "urgency": "High",
                "medications": ["Aspirin"],
                "appointments": ["Follow-up on Monday"],
                "important_actions": ["Take medicine"],
                "warnings": ["Avoid alcohol"],
            }
        },
    )

    assert response.status_code == 200
    assert response.json()["document_type"] == "Hospital Discharge Summary"
    assert response.json()["confidence"] == "High"
    assert "Contains: ✓ Medication" in response.json()["status_text"]
    assert "Contains: ✓ Warning" in response.json()["status_text"]
