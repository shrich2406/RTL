import pickle
from pypdf import PdfReader
from embedder import get_embedding

def ingest_pdf(pdf_path, save_path="embeddings.pkl"):
    reader = PdfReader(pdf_path)
    pages = []
    
    for page_number, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        
        emb = get_embedding(text)
        
        pages.append({
            "page_number": page_number + 1,
            "text": text,
            "embedding": emb
        })
        print(f"Embedded page {page_number+1}")

    pickle.dump(pages, open(save_path, "wb"))
    print(f"Saved {len(pages)} pages to {save_path}")

