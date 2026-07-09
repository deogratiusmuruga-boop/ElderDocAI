from fastapi.testclient import TestClient

from app.main import app


class DummyOllama:
    def chat(self, model, messages):
        return {"message": {"content": "The appointment is on Monday."}}


def test_ask_endpoint_returns_grounded_answer(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "doc123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Your appointment is on Monday.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.ask.PROCESSED_FOLDER", str(processed_dir))
    monkeypatch.setattr("app.services.question_answering_service.ollama", DummyOllama())

    client = TestClient(app)
    response = client.post(f"/ask/{document_id}?question=When%20is%20my%20appointment%3F")

    assert response.status_code == 200
    assert response.json()["answer"] == "The appointment is on Monday."
