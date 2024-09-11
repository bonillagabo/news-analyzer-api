from fastapi import FastAPI
from app.api.v1.routes import news_articles

app = FastAPI()

app.include_router(news_articles.router, prefix="/api/v1/news", tags=["News"])


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Microservice"}
