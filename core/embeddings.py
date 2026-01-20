import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer


class EmbeddingStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []

    def build(self, chunks):
        self.chunks = chunks
        texts = [c["text"] for c in chunks]
        vectors = self.model.encode(texts, show_progress_bar=True)

        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)

    def save(self, path="vector_store"):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, f"{path}/index.faiss")
        with open(f"{path}/chunks.pkl", "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self, path="vector_store"):
        self.index = faiss.read_index(f"{path}/index.faiss")
        with open(f"{path}/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)
