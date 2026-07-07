from fastapi.testclient import TestClient

from app.main import app
from app.services.session_store import session_store


class DummyOllama:
    def chat(self, model, messages):
        return {
            "message": {
                "content": '{"answer":"The medicine should be taken in the morning.","source_sentence":"Take the medicine in the morning."}'
            }
        }


def test_session_conversation_endpoint_uses_persisted_history(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "session123"
    session_id = "sess-1"
    (processed_dir / f"{document_id}.txt").write_text(
        "Take the medicine in the morning.",
        encoding="utf-8",
    )

    monkeypatch.setattr("app.api.session_conversation.PROCESSED_FOLDER", str(processed_dir))
    monkeypatch.setattr("app.services.conversation_service.ollama", DummyOllama())
    session_store.clear(session_id)

    client = TestClient(app)
    response = client.post(f"/session-conversation/{document_id}/{session_id}?question=What%20about%20the%20medicine%3F")

    assert response.status_code == 200
    assert response.json()["answer"] == "The medicine should be taken in the morning."
    assert response.json()["session_id"] == session_id
