from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages):
        pages.append({"text": page.extract_text(), "page": i + 1})
    return pages

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def build_chunks(path):
    all_chunks = []
    for page in load_pdf(path):
        for c in chunk_text(page["text"]):
            all_chunks.append({"text": c, "page": page["page"], "source": path})
    return all_chunks

if __name__ == "__main__":
    chunks = build_chunks("data/constitution.pdf")
    print(len(chunks), "chunks")
    print(chunks[0])