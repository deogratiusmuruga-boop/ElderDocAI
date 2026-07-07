from fastapi.testclient import TestClient

from app.main import app


def test_prioritize_endpoint_groups_items_by_priority():
    client = TestClient(app)
    response = client.post(
        "/prioritize",
        json={
            "analysis": {
                "warnings": ["Call your doctor if chest pain occurs"],
                "important_actions": ["Take medicine every morning"],
                "simple_summary": "Your blood pressure has improved.",
            }
        },
    )

    assert response.status_code == 200
    assert len(response.json()["urgent"]) >= 1
    assert len(response.json()["important"]) >= 1
    assert len(response.json()["informational"]) >= 1
    assert "🔴" in response.json()["summary_text"]
    assert "🟡" in response.json()["summary_text"]
    assert "🟢" in response.json()["summary_text"]
