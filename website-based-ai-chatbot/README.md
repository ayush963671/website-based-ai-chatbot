
# 🌐 Website-Based AI Chatbot (RAG System)

## 📌 Project Overview

This project is a website-based AI chatbot that answers user questions strictly based on the content of a given website.

The system works by:
- Crawling a websiteCrawling a website
- Cleaning and normalizing text
- Splitting content into chunks
- Converting text into embeddings
- Storing them in a FAISS vector database
- Retrieving relevant chunks
- Using LLaMA-3 (via Ollama) to generate answers only from that context

If the information is not found on the website, the chatbot clearly responds that the answer is not available, ensuring no hallucination.

---

## 🎯 Problem Statement

Many AI chatbots generate confident answers even when the source does not contain the information, which leads to hallucinations.

This project solves that issue by implementing a Retrieval Augmented Generation (RAG) pipeline that:

- Grounds answers in website data only
- Blocks external or guessed information
- Ensures safe and controlled AI behavior


---

## 🧠 Key Features

- Website crawling and indexing
- HTML content cleaning
- Text chunking with metadata
- Embedding generation
- Vector storage using FAISS
- Semantic similarity search
- Local LLaMA-3 inference via Ollama
- Hallucination prevention
- Streamlit-based chat UI

---

## 🏗️ System Architecture

1. User enters a website URL
2. Website is crawled
3. HTML is cleaned
4. Text is split into chunks
5. Chunks are embedded
6. Embeddings are stored in FAISS
7. User asks a question
8. Relevant chunks are retrieved
9. LLaMA-3 generates an answer from context only
10. If no context is found, a safe fallback is returned


---

## 🧰 Tech Stack

-
Frontend: Streamlit
Backend: Python
LLM: LLaMA-3 (local, via Ollama)
Embeddings: Sentence-Transformers
Vector Database: FAISS

Libraries and tools:
- Requests
- BeautifulSoup
- FAISS
- Sentence-Transformers
- Streamlit
  

---

## 🚀 Local Setup & Execution (As Required in PDF)

### 🔹 Prerequisites

- Python 3.9+ 
- Git  
- Ollama installed  

---

### 🔹 Step 1: Clone the Repository

git clone https://github.com/ayush963671/website-based-ai-chatbot.git
cd website-based-ai-chatbot


⸻

🔹 Step 2: Create Virtual Environment

python -m venv venv
venv\Scripts\activate


⸻

🔹 Step 3: Install Dependencies

pip install -r requirements.txt


⸻

🔹 Step 4: Install & Run Ollama

Download Ollama from:
https://ollama.com/download

Pull the LLaMA-3 model:

ollama pull llama3

Verify installation:

ollama run llama3


⸻

🔹 Step 5: Run the Application

streamlit run app.py

The application will be available at:

http://localhost:8501


⸻

🧪 How to Use the Chatbot
	1.	Enter a valid website URL
	2.	Click Index Website
	3.	Wait for indexing to complete
	4.	Ask questions related  to that  website

If data exists → chatbot answers
If not → safe fallback messag

⸻

🚫 Hallucination Control

The chatbot intentionally does not answer:
	•	General knowledge questions
	•	Questions unrelated to the indexed website

Example:
	•	Who is the Prime Minister of India?
	
Response:

The answer is not available in the indexed website content.


⸻

🌐 Streamlit Deployment Note
    
This project uses a local LLaMA-3 model via Ollama.
Because cloud platforms do not support local LLM runtimes, the project is designed for local execution only.

⸻

📌 Why Local LLaMA-3?
	•	No dependency on paid APIs
	•	No API keys required
	•	Better control over data privacy
	•	Avoids vendor lock-in

The LLM layer is designed to be swappable for hosted models in production environments.

## 📷 Application Screenshots

### 🖥️ Main Interface



### 💬 Sample Question Answering


📄 Conclusion


This project demonstrates a safe, production-style RAG chatbot that ensures accuracy, transparency, and trust by generating answers only from verified website data.


⸻

👨‍💻 Author

Ayush Sharma 
B.Tech (CSE)

Website-Based AI Chatbot Project

