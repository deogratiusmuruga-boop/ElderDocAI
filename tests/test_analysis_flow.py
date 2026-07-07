import json

from fastapi.testclient import TestClient

from app.api import analyze as analyze_api
from app.main import app
from app.services import analysis_service


class DummyOllama:
    def chat(self, model, messages):
        if "Return ONLY valid JSON with this structure" in messages[0]["content"]:
            return {
                "message": {
                    "content": '{"document_type":"letter","purpose":"informational","urgency":"low"}'
                }
            }

        return {
            "message": {
                "content": '{"quick_overview":"A short overview","simple_summary":"A sample document.","important_actions":[],"important_dates":[],"medications":[],"appointments":[],"contacts":[],"warnings":[],"follow_up_questions":[]}'
            }
        }


def test_analyze_document_saves_json_and_returns_result(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "abc123"
    (processed_dir / f"{document_id}.txt").write_text(
        "Sample document text",
        encoding="utf-8",
    )

    monkeypatch.setattr(analysis_service, "PROCESSED_FOLDER", str(processed_dir))
    monkeypatch.setattr(analysis_service, "MODEL_NAME", "llama3")
    monkeypatch.setattr(analysis_service, "ollama", DummyOllama())

    result = analysis_service.analyze_document(
        str(processed_dir / f"{document_id}.txt"),
        document_id,
    )

    assert result["document_id"] == document_id
    assert result["status"] == "analyzed"

    saved_payload = json.loads((processed_dir / f"{document_id}.json").read_text(encoding="utf-8"))
    assert saved_payload["document_type"] == "letter"
    assert saved_payload["urgency"] == "Low"
    assert "appointments" in saved_payload
    assert "follow_up_questions" in saved_payload


def test_analysis_endpoint_uses_service_layer(tmp_path, monkeypatch):
    processed_dir = tmp_path / "processed_documents"
    processed_dir.mkdir()
    document_id = "xyz789"
    (processed_dir / f"{document_id}.txt").write_text(
        "Example text",
        encoding="utf-8",
    )

    monkeypatch.setattr(analyze_api, "PROCESSED_FOLDER", str(processed_dir))

    def fake_analyze_document(text, document_id):
        return {
            "document_id": document_id,
            "status": "analyzed",
            "analysis_file": str(processed_dir / f"{document_id}.json"),
        }

    monkeypatch.setattr(analyze_api, "analyze_document", fake_analyze_document)

    client = TestClient(app)
    response = client.post(f"/analyze/{document_id}")

    assert response.status_code == 200
    assert response.json()["status"] == "analyzed"
