from sentence_transformers import SentenceTransformer
from core.retriever import Retriever


class QuestionAnswerEngine:
    def __init__(self, store, llm):
        self.store = store
        self.llm = llm
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.retriever = Retriever(store)

    def answer(self, question: str) -> str:
        q_vec = self.embedder.encode([question])
        chunks = self.retriever.search(q_vec)

        if not chunks:
            return "The answer is not available on the provided website."

        context = "\n".join(chunks)

        prompt = f"""
Answer ONLY using the context below.
If not found, reply exactly:
The answer is not available on the provided website.

Context:
{context}

Question:
{question}
"""

        return self.llm.generate(prompt)
