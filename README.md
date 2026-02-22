# 🧠 Mini RAG — Local Retrieval-Augmented Generation Assistant

A lightweight, fully local RAG system that answers questions grounded strictly in your documents — no cloud, no API keys, no data leaving your machine.

---

## ✨ Features

- **Multi-document support** — drop in as many `.txt` files as you need
- **Local embeddings** — powered by SentenceTransformers (MiniLM)
- **FAISS vector search** — fast similarity retrieval over your document chunks
- **Local LLM** — LLaMA3 via Ollama runs entirely on your hardware
- **Source tracking** — see exactly which chunks informed each answer
- **Interactive CLI** — simple question-answer loop, no UI overhead

---

## 🏗 Architecture

```
Text Documents
      │
      ▼
  Chunking
      │
      ▼
 Embeddings (MiniLM)
      │
      ▼
  FAISS Index ◄──── User Query ──► Query Embedding
      │                                    │
      └──────────► Top-K Chunks ◄──────────┘
                        │
                        ▼
              LLaMA3 via Ollama
                        │
                        ▼
                  Final Answer
```

---

## 🛠 Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3.8+ |
| Embeddings | SentenceTransformers (MiniLM) |
| Vector Search | FAISS |
| LLM | LLaMA3 |
| LLM Runtime | Ollama |
| ML Backend | PyTorch |

---

## 📂 Project Structure

```
Mini-RAG-Project/
│
├── documents/
│   └── sample.txt        # Add your .txt files here
│
├── rag.py                # Main application
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/singhharshit24/Mini-RAG-Project.git
cd Mini-RAG-Project
```

### 2. Create and activate a virtual environment
```bash
python -m venv rag_env

# Windows
rag_env\Scripts\activate

# macOS / Linux
source rag_env/bin/activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama and pull LLaMA3

Download Ollama from [ollama.com](https://ollama.com), then run:
```bash
ollama pull llama3
```

---

## ▶️ Running the Assistant

Make sure your `documents/` folder contains at least one `.txt` file and your virtual environment is active, then:

```bash
python rag.py
```

You'll see:
```
RAG Assistant Ready. Type 'exit' to quit.

You:
```

Type your question and press Enter. Type `exit` to quit.

---

## 💬 Example

**Document contains:** information about an AI summit in India

```
You: When is the AI summit happening?
Assistant: The AI Impact Summit India 2026 is scheduled from 16–21 February 2026.

You: Who is the keynote speaker?
Assistant: I don't know based on the provided documents.
```

The assistant will never hallucinate outside your documents — if the answer isn't there, it says so.

---

## 🔍 How It Works

1. Documents in `documents/` are split into overlapping text chunks
2. Each chunk is converted to a vector embedding using MiniLM
3. Embeddings are indexed in FAISS for fast similarity search
4. When you ask a question, it's embedded using the same model
5. The top-K most similar chunks are retrieved from FAISS
6. Those chunks + your question are sent to LLaMA3 as context
7. LLaMA3 generates an answer grounded in the retrieved context

The LLM's weights are never modified — all knowledge expansion happens through the vector index.

---

## 🚀 Possible Improvements

- Persistent FAISS index (skip re-indexing on restart)
- Overlapping chunking strategy for better context continuity
- Hybrid search (BM25 + dense embeddings)
- Reranker model for improved chunk selection
- Web UI with FastAPI or Streamlit
- Conversation memory across turns
- Agent-based tool usage

---

## 🎯 What You'll Learn from This Project

- How vector similarity search works in practice
- Embedding-based document retrieval
- Prompt grounding to reduce hallucination
- Local LLM deployment with Ollama
- The fundamentals of building a production-ready AI pipeline
