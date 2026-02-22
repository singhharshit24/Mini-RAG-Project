import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import ollama

# -------------------------
# 1️⃣ Load Embedding Model
# -------------------------
print("Loading embedding model...")
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------
# 2️⃣ Load Documents
# -------------------------
documents_path = "documents"

all_chunks = []
metadata = []

print("Indexing documents...")

for filename in os.listdir(documents_path):
    if filename.endswith(".txt"):
        with open(os.path.join(documents_path, filename), "r", encoding="utf-8") as f:
            text = f.read()

        # Better chunking (split by paragraphs)
        chunks = text.split("\n\n")

        for chunk in chunks:
            chunk = chunk.strip()
            if chunk:
                all_chunks.append(chunk)
                metadata.append({"source": filename})

# -------------------------
# 3️⃣ Create Embeddings
# -------------------------
embeddings = embed_model.encode(all_chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

print(f"Indexed {len(all_chunks)} chunks successfully.\n")


# -------------------------
# 4️⃣ Ask Function
# -------------------------
def ask(question, k=3):
    q_embedding = embed_model.encode([question])
    distances, indices = index.search(np.array(q_embedding), k=k)

    retrieved_chunks = []
    for idx in indices[0]:
        chunk = all_chunks[idx]
        source = metadata[idx]["source"]
        retrieved_chunks.append(f"[Source: {source}]\n{chunk}")

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a helpful assistant.
Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


# -------------------------
# 5️⃣ Interactive Loop
# -------------------------
print("RAG Assistant Ready. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting RAG assistant.")
        break

    answer = ask(user_input)

    print("\nAssistant:", answer)
    print("-" * 60)
