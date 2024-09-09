from fastapi import HTTPException
from app.services.new import NewsFetcherService


class NewsFetcherController:
    async def get_news(self, request):
        query = request.query_params.get("q")

        if not query:
            raise HTTPException(
                status_code=400,
                detail="The query parameter 'q' is required to fetch news articles. Please provide a valid query.",
            )

        newsFetcher = NewsFetcherService()
        articles = await newsFetcher.fetch_news_by_query(query)
        return articles
