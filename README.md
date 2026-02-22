🧠 Mini RAG Project – Local Retrieval-Augmented Generation Assistant

A lightweight, fully local Retrieval-Augmented Generation (RAG) system built in Python using:

FAISS (vector similarity search)

SentenceTransformers (embeddings)

Ollama + LLaMA3 (local LLM inference)

This project demonstrates how to build a document-grounded AI assistant that answers questions strictly based on uploaded documents.

🚀 Features

✅ Multi-document support

✅ Local embeddings

✅ FAISS vector database

✅ Local LLM (LLaMA3 via Ollama)

✅ Interactive CLI assistant

✅ Source tracking for retrieved chunks

✅ No cloud dependency

🏗 Architecture
                +------------------+
                |  Text Documents  |
                +------------------+
                          |
                          v
                +------------------+
                |   Chunking       |
                +------------------+
                          |
                          v
                +------------------+
                |  Embeddings      |
                | (MiniLM Model)   |
                +------------------+
                          |
                          v
                +------------------+
                |   FAISS Index    |
                +------------------+
                          |
User Query  --->   Embedding ---> Vector Search
                          |
                          v
                +------------------+
                |  Retrieved       |
                |   Context        |
                +------------------+
                          |
                          v
                +------------------+
                |   LLaMA3 (LLM)   |
                |  via Ollama      |
                +------------------+
                          |
                          v
                      Final Answer

🛠 Tech Stack

Python 3.8+

FAISS (vector search)

SentenceTransformers

Ollama

LLaMA3 (local model)

PyTorch

📂 Project Structure
Mini-RAG-Project/
│
├── documents/
│   └── sample.txt
│
├── rag.py
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/singhharshit24/Mini-RAG-Project.git
cd Mini-RAG-Project

2️⃣ Create Virtual Environment
python -m venv rag_env
rag_env\Scripts\activate   # Windows
# source rag_env/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama

Download from:
https://ollama.com

Pull LLaMA3 model:

ollama pull llama3

▶️ How to Run

Make sure:

documents/ folder contains .txt files

Virtual environment is activated

Run:

python rag.py


You will see:

RAG Assistant Ready. Type 'exit' to quit.


Ask questions interactively.

Type exit to close.

💬 Example Usage

If your document contains information about an AI summit:

You: When is the AI summit happening?
Assistant: The AI Impact Summit India 2026 is scheduled from 16–21 February 2026.


If information is not in the documents:

Assistant: I don't know based on the provided documents.

🧠 What is RAG?

Retrieval-Augmented Generation (RAG) is an architecture that:

Retrieves relevant documents using embeddings

Injects them into the LLM prompt

Generates grounded responses

The LLM weights are NOT trained or modified.

Knowledge expansion happens through vector database indexing.

🔍 How It Works Internally

Documents are split into chunks

Chunks are converted into embeddings

Embeddings are stored in FAISS

User query is embedded

Top-k similar chunks are retrieved

Context + query sent to LLaMA3

Answer generated

📈 Possible Improvements

Persistent FAISS index storage

Better chunking with token overlap

Hybrid search (BM25 + embeddings)

Reranker model

Web UI (FastAPI / Streamlit)

Conversation memory

Agent-based tool usage

🎯 Learning Outcomes

This project demonstrates:

Vector similarity search

Embedding-based retrieval

Prompt grounding

Local LLM deployment

Building scalable AI pipelines