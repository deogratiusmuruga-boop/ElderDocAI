from fastapi.testclient import TestClient

from app.main import app


def test_confidence_analysis_endpoint_adds_confidence_scores():
    client = TestClient(app)
    response = client.post(
        "/confidence-analysis",
        json={
            "analysis": {
                "appointments": ["Cardiology appointment"],
                "warnings": ["Call your doctor"],
            }
        },
    )

    assert response.status_code == 200
    assert response.json()["analysis"]["appointments"][0]["confidence"] >= 0.8
    assert response.json()["analysis"]["warnings"][0]["confidence"] >= 0.8
