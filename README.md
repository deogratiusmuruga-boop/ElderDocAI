# ElderDocAI

ElderDocAI is a document-understanding assistant designed for elderly users. It helps people upload documents, understand what matters, and ask simple questions about the content in clear, accessible language.

## What it does

- Uploads and processes documents such as PDFs
- Extracts and cleans document text
- Analyzes the document with Llama 3
- Produces structured analysis output
- Supports grounded Q&A from the processed document
- Offers voice-ready text for speech-based interfaces
- Provides a simple action dashboard and prioritization view
- Explains difficult terms in plain language
- Supports conversation and session-based follow-up questions

## Main workflow

1. Upload a document
2. Process and clean the text
3. Analyze the document
4. Ask questions or review the action dashboard

## API highlights

- POST /upload
- POST /process/{document_id}
- POST /analyze/{document_id}
- POST /ask/{document_id}
- POST /grounded-answer/{document_id}
- POST /conversation/{document_id}
- POST /session-conversation/{document_id}/{session_id}
- GET /voice/{document_id}
- POST /summary-status
- POST /action-dashboard
- POST /confidence-analysis
- POST /cross-check-analysis/{document_id}
- GET /explain-term
- POST /prioritize

## Technology stack

- FastAPI
- Python
- Ollama with Llama 3
- Standard file-based processing for uploaded and processed documents

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

## Notes

The system is designed to be practical and accessible, with a strong focus on helping users understand important information quickly and clearly.
