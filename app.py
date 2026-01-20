import streamlit as st

from core.crawler import crawl_website
from core.cleaner import clean_text
from core.chunker import chunk_text
from core.embeddings import EmbeddingStore
from core.qa_engine import QuestionAnswerEngine
from core.llm_client import OpenSourceLLM


st.set_page_config(page_title="Website AI Chatbot", layout="wide")
st.title("🌐 Website-Based AI Chatbot")

if "engine" not in st.session_state:
    st.session_state.engine = None
if "chat" not in st.session_state:
    st.session_state.chat = []

url = st.sidebar.text_input("Enter Website URL")

if st.sidebar.button("Index Website"):
    data = crawl_website(url)
    cleaned = clean_text(data["text"])
    chunks = chunk_text(cleaned, data["url"], data["title"])

    store = EmbeddingStore()
    store.build(chunks)
    store.save()

    llm = OpenSourceLLM(model="tinyllama")
    st.session_state.engine = QuestionAnswerEngine(store, llm)
    st.session_state.chat = []

    st.sidebar.success("Website indexed successfully")

if st.session_state.engine:
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    q = st.chat_input("Ask a question")
    if q:
        st.session_state.chat.append({"role": "user", "content": q})
        with st.spinner("Thinking..."):
            a = st.session_state.engine.answer(q)
        st.session_state.chat.append({"role": "assistant", "content": a})
        with st.chat_message("assistant"):
            st.write(a)
