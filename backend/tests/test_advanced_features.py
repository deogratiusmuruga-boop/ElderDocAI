from fastapi.testclient import TestClient

from app.main import app


def test_ocr_endpoint_returns_placeholder(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "ocr123"
    (processed_dir / f"{document_id}.txt").write_text("Sample text", encoding="utf-8")

    monkeypatch.setattr("app.api.advanced_features.PROCESSED_FOLDER", str(processed_dir))

    client = TestClient(app)
    response = client.post(f"/ocr/{document_id}")

    assert response.status_code == 200
    assert "ocr_text" in response.json()


def test_retrieval_and_reminder_endpoints_work():
    client = TestClient(app)

    index_response = client.post("/index-document/doc1")
    assert index_response.status_code == 404

    reminder_response = client.post(
        "/reminders",
        json={"text": "Please attend on July 18."},
    )

    assert reminder_response.status_code == 200
    assert reminder_response.json()["reminders"]
