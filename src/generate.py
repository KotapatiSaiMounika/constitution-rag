from google import genai
from retrieve import retrieve

client = genai.Client()
MODEL = "gemini-3.5-flash"

def build_prompt(question, chunks):
    context = "\n\n".join(f"[Page {c['page']}]\n{c['text']}" for c in chunks)
    return f"""You are an assistant answering questions about the Constitution of India.
Use ONLY the context below. If the answer is not in the context, say:
"I could not find this in the retrieved text."
Cite page numbers like (page 42).

Context:
{context}

Question: {question}
Answer:"""

def answer(question, k=4):
    chunks = retrieve(question, k)
    prompt = build_prompt(question, chunks)
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text, chunks

if __name__ == "__main__":
    q = input("Ask: ")
    text, chunks = answer(q)
    print("\n" + text)
    print("\nSources:", sorted({c["page"] for c in chunks}))