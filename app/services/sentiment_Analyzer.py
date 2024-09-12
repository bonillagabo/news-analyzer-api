import asyncio
from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self, batch_size=25):
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="finiteautomata/bertweet-base-sentiment-analysis",
        )
        self.batch_size = batch_size
        self.sentiment_types = {"POS": "positive", "NEG": "negative", "NEU": "neutral"}

    async def analysis(self, data):
        results = await asyncio.get_running_loop().run_in_executor(
            None, lambda: self.sentiment_pipeline(data, batch_size=self.batch_size)
        )
        return [self.sentiment_types[result["label"]] for result in results]


sentiment_analyzer = SentimentAnalyzer()
