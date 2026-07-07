from fastapi.testclient import TestClient

from app.main import app


def test_cross_check_analysis_endpoint_verifies_items_against_document(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "cross123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Appointment July 17.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.cross_check.PROCESSED_FOLDER", str(processed_dir))

    client = TestClient(app)
    response = client.post(
        f"/cross-check-analysis/{document_id}",
        json={
            "analysis": {
                "appointments": ["Appointment July 18"],
            }
        },
    )

    assert response.status_code == 200
    assert response.json()["analysis"]["appointments"][0]["verified"] is False
