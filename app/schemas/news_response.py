from pydantic import BaseModel
from typing import List
from app.schemas.article import Article


class NewsResponse(BaseModel):
    articles: List[Article]
