from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.source import Source


class Article(BaseModel):
    source: Source
    author: Optional[str]
    title: str
    publishedAt: datetime
    content: Optional[str]
    title_sentiment: Optional[str]
    category: Optional[str]
