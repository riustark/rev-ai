from fastapi import FastAPI
from app.api.router import api_router



app = FastAPI(
    title="REV_AI",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "Rev-AI is running!"}


@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

app.include_router(api_router)


    