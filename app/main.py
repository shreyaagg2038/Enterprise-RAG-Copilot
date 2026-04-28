from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Enterprise RAG Copilot",
    docs_url="/",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
