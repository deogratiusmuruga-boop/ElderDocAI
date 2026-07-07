from fastapi.testclient import TestClient

from app.main import app


class DummyOllama:
    def chat(self, model, messages):
        return {
            "message": {
                "content": '{"answer":"The medicine should be taken in the morning.","source_sentence":"Take the medicine in the morning."}'
            }
        }


def test_conversation_endpoint_uses_history(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "conv123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Take the medicine in the morning.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.conversation.PROCESSED_FOLDER", str(processed_dir))
    monkeypatch.setattr("app.services.conversation_service.ollama", DummyOllama())

    client = TestClient(app)
    response = client.post(
        f"/conversation/{document_id}?question=What%20about%20the%20medicine%3F",
        json={
            "history": [
                {"question": "What should I do first?", "answer": "Read the instructions."}
            ]
        },
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "The medicine should be taken in the morning."
