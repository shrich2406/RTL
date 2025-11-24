from fastapi import FastAPI, UploadFile
from load_pdf import ingest_pdf
from rag_pipeline import rag_answer
from fastapi.staticfiles import StaticFiles
import shutil, tempfile

app = FastAPI()

# serve UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile):
    temp = tempfile.mktemp(suffix=".pdf")
    with open(temp, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ingest_pdf(temp)
    return {"message": "PDF processed and embeddings saved"}

@app.get("/ask")
def ask(q: str):
    return rag_answer(q)

@app.get("/")
def home():
    return {"message": "Local RAG is running! Go to /static/index.html"}
