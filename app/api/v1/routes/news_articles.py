from fastapi import APIRouter, Query
from starlette.requests import Request
from app.controllers.news_articles import NewsFetcherController
from app.schemas.news_response import NewsResponse

router = APIRouter()


@router.get("/", response_model=NewsResponse)
async def get_news(request: Request, q: str = Query(None, description="Search term for news")) -> NewsResponse:
    return await NewsFetcherController().get_news(request)
