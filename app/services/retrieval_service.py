import re


class SimpleVectorStore:
    """
    Lightweight in-memory retrieval store with chunking and overlap scoring.
    """

    def __init__(self):
        self._documents = {}

    def _chunk_text(self, text: str, chunk_size: int = 120):
        words = re.findall(r"\b\w+\b", text)
        chunks = []
        for index in range(0, len(words), chunk_size):
            chunk_words = words[index:index + chunk_size]
            if chunk_words:
                chunks.append(" ".join(chunk_words))
        return chunks

    def add_document(self, document_id: str, text: str):
        chunks = self._chunk_text(text)
        self._documents[document_id] = chunks

    def search(self, query: str, limit: int = 3):
        query_terms = set(re.findall(r"\b\w+\b", query.lower()))
        if not query_terms:
            return []

        scored_matches = []
        for document_id, chunks in self._documents.items():
            for chunk in chunks:
                chunk_terms = set(re.findall(r"\b\w+\b", chunk.lower()))
                overlap = len(query_terms & chunk_terms)
                if overlap > 0:
                    scored_matches.append({
                        "document_id": document_id,
                        "chunk": chunk,
                        "score": overlap,
                    })

        scored_matches.sort(key=lambda item: item["score"], reverse=True)
        return scored_matches[:limit]


vector_store = SimpleVectorStore()
