from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Microservice"}


def test_get_news():
    query = "technology"
    response = client.get(f"/api/v1/news?q={query}")
    assert response.status_code == 200
    assert "articles" in response.json()
