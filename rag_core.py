import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import ollama

DOCUMENTS_PATH = "documents"
os.makedirs(DOCUMENTS_PATH, exist_ok=True)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
all_chunks = []
metadata = []

# NEW: in-memory manual text storage
manual_texts = []


def build_index():
    global index, all_chunks, metadata

    all_chunks = []
    metadata = []

    # 1️⃣ Load uploaded files
    for filename in os.listdir(DOCUMENTS_PATH):
        if filename.endswith(".txt"):
            with open(os.path.join(DOCUMENTS_PATH, filename), "r", encoding="utf-8") as f:
                text = f.read()

            chunks = text.split("\n\n")

            for chunk in chunks:
                chunk = chunk.strip()
                if chunk:
                    all_chunks.append(chunk)
                    metadata.append({"source": filename})

    # 2️⃣ Load manual texts (in-memory)
    for i, text in enumerate(manual_texts):
        chunks = text.split("\n\n")
        for chunk in chunks:
            chunk = chunk.strip()
            if chunk:
                all_chunks.append(chunk)
                metadata.append({"source": f"manual_input_{i}"})

    if not all_chunks:
        index = None
        return

    embeddings = embed_model.encode(all_chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


def add_manual_text(text):
    manual_texts.append(text)
    build_index()


def ask(question, k=2):
    try:
        if index is None:
            return "No documents available."

        q_embedding = embed_model.encode([question])
        distances, indices = index.search(np.array(q_embedding), k=k)

        retrieved_chunks = []
        for idx in indices[0]:
            chunk = all_chunks[idx]
            source = metadata[idx]["source"]
            retrieved_chunks.append(f"[Source: {source}]\n{chunk}")

        context = "\n\n".join(retrieved_chunks)

        response = ollama.chat(
            model="phi3",
            messages=[{"role": "user", "content": context + "\n\nQuestion: " + question}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"

def get_manual_text_count():
    return len(manual_texts)
