# vector_db.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

text_chunks = []
embeddings = []
index = None

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def build_vector_db(text):
    global text_chunks, embeddings, index
    text_chunks = chunk_text(text)
    embeddings = model.encode(text_chunks, show_progress_bar=False)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

def retrieve_similar_chunks(query, top_k=3):
    if index is None:
        return []
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [text_chunks[i] for i in indices[0]]
