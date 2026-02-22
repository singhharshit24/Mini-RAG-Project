# 🧠 Mini RAG — Flask-Based Local RAG Assistant

A fully local **Retrieval-Augmented Generation** web app — upload documents, paste text, ask questions, and get grounded answers. No cloud APIs. No data leaving your machine.

Built with FAISS · SentenceTransformers · Ollama (phi3 / LLaMA3) · Flask · Bootstrap

---

## ✨ Features

- Upload `.txt` documents or paste text directly into the app
- Automatic re-indexing whenever new content is added
- Visual indicator showing whether answers came from uploaded files or manual text
- Loading animation during LLM inference
- Semantic vector search via FAISS
- Fully local LLM — no API keys, no internet required
- Modular backend separating Flask routing from RAG logic

---

## 🏗 Architecture

```
Browser (Bootstrap UI)
        │
        ▼
Flask Web Server (app.py)
        │
        ▼
RAG Core — FAISS + SentenceTransformers (rag_core.py)
        │
        ▼
Ollama — phi3 / LLaMA3
        │
        ▼
Generated Answer
```

---

## 📂 Project Structure

```
Mini-RAG-Project/
│
├── documents/            # Uploaded .txt files
├── templates/
│   └── index.html        # Frontend UI
│
├── rag_core.py           # Embedding, indexing, and retrieval logic
├── app.py                # Flask routes and server
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

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama and pull a model

Download from [ollama.com](https://ollama.com), then choose based on your available RAM:

| RAM    | Recommended Model | Command               |
|--------|-------------------|-----------------------|
| 8 GB   | phi3              | `ollama pull phi3`    |
| 16 GB+ | LLaMA3            | `ollama pull llama3`  |

---

## ▶️ Running the App

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

---

## 📄 Usage

1. **Add knowledge** — upload a `.txt` file or paste text directly into the manual input field
2. The system chunks and re-indexes your content automatically
3. A source indicator shows whether retrieved context came from a file or manual text
4. **Ask a question** — a loading animation plays while the LLM processes your query
5. The answer is generated strictly from the retrieved context

If the information isn't in your documents:
```
I don't know based on the provided documents.
```

---

## ⚠️ Important Notes

**Flask debug mode** — disable it to prevent threading conflicts with local LLM inference:
```python
app.run(debug=False, use_reloader=False)
```

**Out-of-memory errors** — if you see `model requires more system memory`, switch to `phi3`, close other heavy applications, and consider reducing the retrieval parameter `k` in `rag_core.py`.

---

## 🔍 How It Works

1. Documents and pasted text are split into chunks
2. Each chunk is embedded using SentenceTransformers (MiniLM)
3. Embeddings are stored in a FAISS index
4. Your query is embedded with the same model
5. The top-K most similar chunks are retrieved
6. Those chunks + your question are sent to the LLM as context
7. The LLM generates an answer grounded strictly in that context

The model's weights are never modified — all knowledge expansion happens through the vector index.

---

## 🚀 Future Improvements

- Persistent FAISS index (save and reload across restarts)
- Chat-style conversation UI with memory
- Streaming responses for real-time output
- In-app document viewer
- Hybrid search (BM25 + dense embeddings)
- User authentication
- Docker containerization and cloud VM deployment

---

## 🎯 What You'll Learn from This Project

- Semantic search and vector indexing with FAISS
- Embedding-based document retrieval
- Local LLM deployment and integration with Ollama
- Modular Flask backend architecture
- Building a full-stack AI web application
