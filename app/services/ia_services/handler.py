class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, subject: str, question: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(subject, question)
        return None
