from fastapi import FastAPI
from app.api.v1.routes import new

app = FastAPI()

app.include_router(new.router, prefix="/api/v1/news", tags=["News"])


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Microservice"}
