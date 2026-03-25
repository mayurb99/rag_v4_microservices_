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
        response = requests.post(
            "http://127.0.0.1:8001/rag",
            json={"question": req.question}
        )

        print("RAG RESPONSE:", response.text) 

        return {
            "question": req.question,
            "answer": response.json()["answer"]
        }

    except Exception as e:
        return {"error": str(e)}