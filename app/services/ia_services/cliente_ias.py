from .ias.chatgpt_handler import ChatGptHandler
from .ias.gemini_handler import GemeniHandler
from .ias.dummyai_handler import DummyHandler


class ClientIAs:
    def question(self, subject: str, question: str) -> str:
        chatgpt = ChatGptHandler()
        gemini = GemeniHandler()
        dummy = DummyHandler()

        chatgpt.set_next(gemini).set_next(dummy)

        result = chatgpt.handle(subject, question)

        return result