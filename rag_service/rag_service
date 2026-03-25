from fastapi import FastAPI
from pydantic import BaseModel
from src.rag_pipeline import get_rag_answer

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG Service running"}

@app.post("/rag")
def run_rag(req: QueryRequest):
    answer = get_rag_answer(req.question)
    return {
        "answer": answer
    }