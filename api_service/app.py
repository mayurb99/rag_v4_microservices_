from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "API Service running"}

@app.post("/ask")
def ask(req: QueryRequest):

    try:
        print("Calling RAG service...")
        response = requests.post(
            "http://localhost:8001/rag",
            json={"question": req.question}
        )

        print("RAG RESPONSE:", response.text) 

        return {
            "question": req.question,
            "answer": response.json()["answer"]
        }

    except Exception as e:
        return {"error": str(e)}