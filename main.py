from fastapi import FastAPI

from api.upload import router as upload_router
from api.search import router as search_router
from api.chat import router as chat_router

app = FastAPI(
    title="Knowledge Intelligence Platform",
    version="1.0.0"
)

app.include_router(
    upload_router,
    tags=["Upload"]
)

app.include_router(
    search_router,
    tags=["Search"]
)

app.include_router(
    chat_router,
    tags=["Chat"]
)


@app.get("/")
def home():
    return {
        "message": "Knowledge Intelligence Platform Running"
    }