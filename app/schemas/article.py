from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.source import Source

class Article(BaseModel):
    source: Source
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    urlToImage: Optional[str]
    publishedAt: datetime
    content: Optional[str]
