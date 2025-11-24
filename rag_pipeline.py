from retriever import search
from llm_answer import answer_with_context

def rag_answer(query):
    # Retrieve top 3 pages (less duplication & faster)
    pages = search(query, top_k=5)

    # Build context for LLM
    context = ""
    for p in pages:
        context += f"[Page {p['page_number']}]\n{p['text']}\n\n"

    # Generate answer using Ollama
    answer = answer_with_context(context, query)

    # Deduplicate pages so each page appears only once
    unique_pages = []
    seen = set()

    for p in pages:
        pg = p["page_number"]
        if pg not in seen:
            unique_pages.append({"page": pg})
            seen.add(pg)

    # Final response
    return {
        "answer": answer,
        "sources": unique_pages
    }
