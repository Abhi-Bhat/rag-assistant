from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from RAG.retrieval_pipeline import get_answer

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask", response_class=HTMLResponse)
def ask(request: Request, question: str = Form(...)):
    answer, sources = get_answer(question)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question,
        "answer": answer,
        "sources": sources
    })