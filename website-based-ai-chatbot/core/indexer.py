# indexer.py

import os
from Crawler import crawl_website
from text_cleaner import clean_text
from chunker import chunk_text
from embeddings_store import EmbeddingStore


URL = "https://en.wikipedia.org/wiki/Machine_Learning"

# Step 1: crawl
data = crawl_website(URL)

# Step 2: clean
cleaned_text = clean_text(data["text"])

# Step 3: chunk
chunks = chunk_text(
    text=cleaned_text,
    source_url=data["url"],
    page_title=data["title"],
    chunk_size=200,
    overlap=50
)

# Step 4: vector store
store = EmbeddingStore()

if os.path.exists("vector_store/index.faiss"):
    store.load()
    print("Loaded existing vector store")
else:
    store.build(chunks)
    store.save()
    print("Created new vector store")
