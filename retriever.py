import pickle
import numpy as np
import faiss
from embedder import get_embedding

def load_embeddings(path="embeddings.pkl"):
    return pickle.load(open(path, "rb"))

def search(query, top_k=5):
    pages = load_embeddings()

    # build matrix of embeddings
    embeddings = np.array([p["embedding"] for p in pages]).astype("float32")
    
    # FAISS index for similarity search
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    q_emb = np.array([get_embedding(query)]).astype("float32")
    scores, idx = index.search(q_emb, top_k)

    results = []
    for i in idx[0]:
        results.append(pages[i])

    return results
