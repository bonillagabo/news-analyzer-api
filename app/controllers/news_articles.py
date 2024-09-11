import asyncio
from fastapi import HTTPException
from app.services.news_articles import NewsFetcherService
from app.schemas.news_response import NewsResponse
from app.services.sentiment_Analyzer import sentiment_analyzer
from app.services.news_classifier import news_classifier


class NewsFetcherController:
    async def get_news(self, request) -> NewsResponse:
        query = request.query_params.get("q")

        if not query:
            raise HTTPException(
                status_code=400,
                detail="The query parameter 'q' is required to fetch news articles. Please provide a valid query.",
            )

        news_fetcher = NewsFetcherService()
        articles = await news_fetcher.fetch_news_by_query(query)

        articles_titles = [article["title"] for article in articles]
        articles_contents = [article["content"] for article in articles]

        sentiment_analysis_task = asyncio.create_task(
            sentiment_analyzer.analysis(articles_titles)
        )
        classification_task = asyncio.create_task(
            news_classifier.classify(articles_contents)
        )

        sentiment_analysis_result, classification_result = await asyncio.gather(
            sentiment_analysis_task, classification_task
        )

        for idx, article in enumerate(articles):
            article["title_sentiment"] = sentiment_analysis_result[idx]
            article["category"] = classification_result[idx]

        return NewsResponse(articles=articles)
