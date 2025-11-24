# 📘 RTL –RAG Document Assistant  
*A fast, simple, fully local PDF Question-Answering system using FastAPI, FAISS, and Ollama.*

---

## 🚀 Overview

**RTL** is a lightweight local Retrieval-Augmented Generation (RAG) system that allows you to:

- 📤 Upload **any PDF document**
- ❓ Ask natural-language questions
- 🤖 Get LLM-generated answers **based only on the PDF**
- 📄 See which **page numbers** were used
- 🔒 Run everything **offline** using **Ollama (Llama3)**

No cloud.  
No API keys.  
No privacy risks.

---

## 🗂️ Project Structure
RTL/
│
├── app.py # FastAPI backend + endpoints
├── rag_pipeline.py # RAG workflow: retrieval + LLM
├── retriever.py # FAISS vector search over embeddings
├── load_pdf.py # Extract text + build embeddings for each page
├── embedder.py # MiniLM sentence embeddings
├── llm_answer.py # Calls Ollama model through local HTTP API
├── static/index.html # Simple front-end UI
├── requirements.txt # Python dependencies
└── generate_cert.py # Optional: create HTTPS certificates


---
 🛠️ Installation

### 1️⃣ Clone the Repository

git clone https://github.com/shrich2406/RTL.git
cd RTL

2️⃣ Create & Activate a Virtual Environment
python -m venv .venv
.\.venv\Scripts\Activate

3️⃣ Install Python Dependencies
pip install -r requirements.txt

🤖 Install & Run Ollama

Download: https://ollama.com/download

Start the Ollama server:

ollama serve


Pull a model:

ollama pull llama3

▶️ Run the Application
Start FastAPI (HTTP mode)
uvicorn app:app --reload

Or run with HTTPS (optional)
uvicorn app:app --ssl-keyfile=key.pem --ssl-certfile=cert.pem

🌐 Open the Web UI

Visit:

http://localhost:8000/static/index.html


Then:

Upload a PDF

Ask a question

Receive an answer + page references

