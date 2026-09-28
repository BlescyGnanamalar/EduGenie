from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .config import settings
from .ai_service import (
    ask_ai,
    generate_quiz,
    simplify_concept,
    generate_learning_path,
    summarize_text
)


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered educational assistant",
    version="1.0.0"
)


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


# Static files
app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


# Request model
class RequestData(BaseModel):
    text: str


# Home page
@app.get("/")
async def home():

    return FileResponse(
        FRONTEND_DIR / "index.html"
    )


# Health check
@app.get("/health")
async def health():

    return {
        "status": "ok",
        "app": settings.APP_NAME
    }


# Ask Question
@app.post("/ask")
async def ask_question(data: RequestData):

    text = data.text.strip()

    if not text:

        return {
            "answer": "Please enter a question."
        }

    answer = ask_ai(text)

    return {
        "answer": answer
    }


# Simplify Concept
@app.post("/simplify")
async def simplify(data: RequestData):

    text = data.text.strip()

    if not text:

        return {
            "answer": "Please enter a concept."
        }

    answer = simplify_concept(text)

    return {
        "answer": answer
    }


# Generate Quiz
@app.post("/quiz")
async def quiz(data: RequestData):

    text = data.text.strip()

    if not text:

        return {
            "answer": "Please enter a topic."
        }

    answer = generate_quiz(text)

    return {
        "answer": answer
    }


# Learning Path
@app.post("/learning-path")
async def learning_path(data: RequestData):

    text = data.text.strip()

    if not text:

        return {
            "answer": "Please enter a topic."
        }

    answer = generate_learning_path(text)

    return {
        "answer": answer
    }


# Summarize
@app.post("/summarize")
async def summarize(data: RequestData):

    text = data.text.strip()

    if not text:

        return {
            "answer": "Please enter text to summarize."
        }

    answer = summarize_text(text)

    return {
        "answer": answer
    }