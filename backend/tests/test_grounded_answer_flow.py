from fastapi.testclient import TestClient

from app.main import app


class DummyOllama:
    def chat(self, model, messages):
        return {
            "message": {
                "content": '{"answer":"The appointment is on Monday.","source_sentence":"Your appointment is on Monday."}'
            }
        }


def test_grounded_answer_endpoint_returns_answer_and_source(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "grounded123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Your appointment is on Monday.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.grounded_answer.PROCESSED_FOLDER", str(processed_dir))
    monkeypatch.setattr("app.services.grounded_answer_service.ollama", DummyOllama())

    client = TestClient(app)
    response = client.post(f"/grounded-answer/{document_id}?question=When%20is%20my%20appointment%3F")

    assert response.status_code == 200
    assert response.json()["answer"] == "The appointment is on Monday."
    assert response.json()["source_sentence"] == "Your appointment is on Monday."
