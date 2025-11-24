import requests

def answer_with_context(context, question):
    prompt = f"""
Use ONLY the context below to answer the question.
Include the page numbers in your explanation.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",   # or mistral, phi3, etc.
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        # debug print
        print("=== OLLAMA RAW RESPONSE ===")
        print(response.text)

        data = response.json()

        # normal Ollama response has:  { "response": "text..." }
        if "response" in data:
            return data["response"]

        # if error exists
        if "error" in data:
            return f"Ollama Error: {data['error']}"

        return "Unexpected Ollama response format."

    except Exception as e:
        return f"Ollama request failed: {str(e)}"
