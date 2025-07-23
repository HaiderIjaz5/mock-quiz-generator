# chunking.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory vector store
index = faiss.IndexFlatL2(384)
chunks_store = []

def embed_and_store(text):
    global index, chunks_store
    chunks_store.clear()
    index.reset()

    # Simple chunking
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 30]
    embeddings = model.encode(paragraphs)
    index.add(np.array(embeddings).astype('float32'))
    chunks_store.extend(paragraphs)

def search_chunks(query, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec).astype('float32'), top_k)
    return [chunks_store[i] for i in I[0]]
