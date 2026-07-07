from fastapi.testclient import TestClient

from app.main import app


def test_explain_term_endpoint_returns_simple_explanation():
    client = TestClient(app)
    response = client.get("/explain-term?term=Hypertension")

    assert response.status_code == 200
    assert response.json()["found"] is True
    assert "High blood pressure" in response.json()["explanation"]
