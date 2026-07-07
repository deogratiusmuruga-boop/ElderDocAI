from collections import defaultdict


class SessionStore:
    """
    In-memory session store for lightweight conversation state.
    """

    def __init__(self):
        self._sessions = defaultdict(list)

    def get_history(self, session_id: str):
        return list(self._sessions.get(session_id, []))

    def append_turn(self, session_id: str, question: str, answer: str, source_sentence: str = ""):
        self._sessions[session_id].append(
            {
                "question": question,
                "answer": answer,
                "source_sentence": source_sentence,
            }
        )

    def clear(self, session_id: str):
        self._sessions.pop(session_id, None)


session_store = SessionStore()
