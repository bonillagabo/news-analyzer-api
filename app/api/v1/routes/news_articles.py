from fastapi import APIRouter
from starlette.requests import Request
from app.controllers.news_articles import NewsFetcherController
from app.schemas.news_response import NewsResponse

router = APIRouter()


@router.get("/", response_model=NewsResponse)
async def get_news(request: Request) -> NewsResponse:
    return await NewsFetcherController().get_news(request)
