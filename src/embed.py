import json
import numpy as np
from sentence_transformers import SentenceTransformer
from ingest import build_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True, normalize_embeddings=True)

if __name__ == "__main__":
    chunks = build_chunks("data/constitution.pdf")
    texts = [c["text"] for c in chunks]

    vectors = embed_texts(texts)
    print("shape:", vectors.shape)
    print("first vector (first 5 numbers):", vectors[0][:5])

    np.save("data/vectors.npy", vectors)
    with open("data/chunks.json", "w") as f:
        json.dump(chunks, f)