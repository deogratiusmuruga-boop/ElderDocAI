from fastapi.testclient import TestClient

from app.main import app


def test_voice_endpoint_returns_voice_ready_text(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "voice123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Your appointment is on Monday.\nPlease arrive early.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.voice.PROCESSED_FOLDER", str(processed_dir))

    client = TestClient(app)
    response = client.get(f"/voice/{document_id}")

    assert response.status_code == 200
    assert "appointment" in response.json()["voice_ready_text"].lower()
