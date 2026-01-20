import numpy as np

class Retriever:
    def __init__(self, store):
        self.store = store

    def search(self, query_vector, top_k=2):
        _, indices = self.store.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.store.chunks):
                results.append(self.store.chunks[idx]["text"][:500])

        return results
