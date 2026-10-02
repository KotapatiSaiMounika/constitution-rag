import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = np.load("data/vectors.npy")
with open("data/chunks.json") as f:
    chunks = json.load(f)

def retrieve(query, k=4):
    q = model.encode(query, normalize_embeddings=True)
    scores = vectors @ q
    top = np.argsort(scores)[::-1][:k]
    return [{**chunks[i], "score": float(scores[i])} for i in top]

if __name__ == "__main__":
    query = input("Ask: ")
    for r in retrieve(query):
        print(f"\n[page {r['page']}] score={r['score']:.3f}")
        print(r["text"])