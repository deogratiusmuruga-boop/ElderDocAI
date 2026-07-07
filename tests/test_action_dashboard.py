from fastapi.testclient import TestClient

from app.main import app


def test_action_dashboard_endpoint_builds_simple_dashboard():
    client = TestClient(app)
    response = client.post(
        "/action-dashboard",
        json={
            "analysis": {
                "important_actions": ["Take Amlodipine"],
                "important_dates": ["July 18"],
                "appointments": ["Cardiology appointment"],
                "warnings": ["Contact your doctor if chest pain occurs."],
            }
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Priority-Aware Dashboard"
    assert any(section["title"] == "What You Need to Know First" for section in response.json()["sections"])
    assert any(item["text"] == "Take Amlodipine" for section in response.json()["sections"] for item in section["items"])
    assert any(item["text"] == "Cardiology appointment" for section in response.json()["sections"] for item in section["items"])
