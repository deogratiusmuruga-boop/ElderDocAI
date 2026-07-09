# ElderDocAI

ElderDocAI is an AI-powered document intelligence system designed to help elderly users understand, interact with, and act on information contained in complex documents through retrieval-augmented generation, conversational AI, and accessible explanations.

The system is designed to make complex documents accessible, actionable, and easier to understand.

---

## Features

- 📄 File upload and document processing
- 📑 PDF text extraction, cleaning, and normalization
- 🧠 Two-stage analysis using Llama 3 to build structured knowledge
- ❓ Grounded question answering with supporting evidence
- 💬 Multi-turn conversational follow-up
- 🔊 Voice-friendly text generation
- ⚠ Prioritized action dashboard for key risks and next steps
- 🔎 Fact verification against document content
- 📚 Plain-language explanations for difficult terms
- 🧠 Document indexing and retrieval support
- ⏰ Reminder extraction from document text

---

## System Workflow

```text
Upload Document
        │
        ▼
Document Processing
        │
        ▼
Text Extraction
        │
        ▼
Text Cleaning
        │
        ▼
Llama 3 Analysis
        │
        ▼
Structured Knowledge
        │
        ├──────────────┐
        ▼              ▼
Action Dashboard   Question Answering
        │              │
        ▼              ▼
 Voice Output    Conversation Support
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload a document file (PDF/JPG/PNG) |
| POST | `/process/{document_id}` | Process an uploaded document and extract text |
| POST | `/analyze/{document_id}` | Analyze a processed document and build structured output |
| POST | `/ask/{document_id}` | Ask a question about a processed document |
| POST | `/grounded-answer/{document_id}` | Ask a question and get evidence from the document |
| POST | `/conversation/{document_id}` | Single-turn conversational interaction with optional history |
| POST | `/session-conversation/{document_id}/{session_id}` | Multi-turn session conversation with stored history |
| GET | `/voice/{document_id}` | Get speech-friendly text for a document |
| POST | `/summary-status` | Build a UI-friendly summary status from analysis payload |
| POST | `/action-dashboard` | Generate prioritized actions from analysis payload |
| POST | `/confidence-analysis` | Annotate analysis results with confidence scores |
| POST | `/cross-check-analysis/{document_id}` | Verify extracted analysis items against the document text |
| GET | `/explain-term` | Explain a difficult term in simple language |
| POST | `/prioritize` | Rank analysis items by urgency and importance |
| POST | `/ocr/{document_id}` | Run lightweight OCR-style text extraction on a processed document |
| POST | `/index-document/{document_id}` | Index a processed document for retrieval |
| POST | `/retrieve` | Search indexed document chunks by query |
| POST | `/reminders` | Extract reminders and date-based events from text |

---

## Technology Stack

- Python
- FastAPI
- Ollama
- Llama 3
- PyMuPDF
- Local file storage for document upload and processing

---

## Project Structure

```
ElderDocAI/
├── app/
│   ├── api/
│   ├── services/
│   ├── prompts/
│   ├── models/
│   └── utils/
├── uploaded_documents/
├── processed_documents/
├── vector_db/
├── tests/
├── requirements.txt
└── README.md
```

---

## Installation

1. Create and activate a Python virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Start the API server:

```bash
uvicorn app.main:app --reload
```

4. Open the interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## How It Works

1. Upload a document using `/upload`.
2. Process the uploaded file with `/process/{document_id}` to extract and clean text.
3. Analyze the cleaned text with `/analyze/{document_id}` to build structured understanding.
4. Ask questions using `/ask/{document_id}` or `/grounded-answer/{document_id}`.
5. Use `/conversation/{document_id}` or `/session-conversation/{document_id}/{session_id}` for follow-up interaction.
6. Generate voice-ready text with `/voice/{document_id}`.
7. Build UI-friendly summaries and dashboards with `/summary-status`, `/action-dashboard`, `/confidence-analysis`, `/cross-check-analysis/{document_id}`, `/explain-term`, and `/prioritize`.
8. Index documents with `/index-document/{document_id}` and retrieve relevant chunks with `/retrieve`.
9. Extract reminders with `/reminders`.

---

## Current Capabilities

- Upload and preprocess PDF, JPG, and PNG documents
- Extract text and clean it for analysis
- Analyze documents with Llama 3 to build structured knowledge
- Answer questions with grounded evidence and conversational context
- Build action-driven dashboards and prioritize urgent items
- Generate plain-language term explanations and confidence annotations
- Index documents for lightweight retrieval
- Extract reminder candidates from text

---

## Notes

- OCR is currently implemented as a lightweight placeholder and can be replaced with a production OCR engine.
- Retrieval uses a simple chunk-based in-memory store and can be upgraded to a full vector database such as ChromaDB.

---

## Future Enhancements

- Full OCR support for scanned or image-only documents
- Multi-document reasoning across uploads
- ChromaDB or vector database integration for large-scale retrieval
- Reminder scheduling and notification workflows
- Web or mobile user interface integration

---

## License

This project was developed as part of a master's research project focused on AI-assisted document understanding for elderly users.
