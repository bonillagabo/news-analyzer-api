import httpx
import logging
from fastapi import HTTPException
from app.core.config import settings


class NewsFetcherService:
    def __init__(self):
        self.api_key = settings.NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2"

    async def _make_request(self, url: str, params: dict):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url, params=params, headers=headers, timeout=20.0
                )
                response.raise_for_status()
                return response.json()
            except httpx.TimeoutException:
                logging.error(
                    "The request timed out. This may be due to slow network or unresponsive server."
                )
                raise HTTPException(
                    status_code=504,
                    detail="The request timed out. Please try again later or check the server status.",
                )
            except httpx.HTTPStatusError as http_err:
                logging.error(f"HTTP error occurred: {http_err.response.status_code}")
                raise HTTPException(
                    status_code=http_err.response.status_code,
                    detail=f"HTTP error occurred with status code {http_err.response.status_code}. Please check the request and try again.",
                )
            except httpx.RequestError as req_err:
                logging.error(f"An error occurred while making the request: {req_err}")
                raise HTTPException(
                    status_code=500,
                    detail="An error occurred while making the request. Please try again later.",
                )
            except ValueError as json_err:
                logging.error(f"Error decoding the JSON response: {json_err}")
                raise HTTPException(
                    status_code=500,
                    detail="An error occurred while decoding the JSON response. Please check the response format and try again.",
                )

    async def fetch_news_by_query(self, query: str):
        url = f"{self.base_url}/everything"
        params = {
            "apiKey": self.api_key,
            "sortBy": "publishedAt",
            "pageSize": "100",
            "language": "en",
            "q": query,
        }
        response_json = await self._make_request(url, params)
        if response_json:
            articles = response_json.get("articles")
            if not articles:
                logging.warning("No articles found for the query.")
                raise HTTPException(
                    status_code=404, detail="No articles found for the given query."
                )
            return articles
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while fetching news.",
        )
