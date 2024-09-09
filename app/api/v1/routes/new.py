from fastapi import APIRouter
from starlette.requests import Request
from app.controllers.new import NewsFetcherController

router = APIRouter()


@router.get("")
async def get_news(request: Request):
    return await NewsFetcherController().get_news(request)
