import asyncio
from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self, batch_size=25):
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="finiteautomata/bertweet-base-sentiment-analysis",
        )
        self.batch_size = batch_size

    def batch(self, iterable, n=1):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx : min(ndx + n, l)]

    async def analysis(self, data):
        results_label = []
        for batch_data in self.batch(data, self.batch_size):
            results = await asyncio.get_running_loop().run_in_executor(
                None, self.sentiment_pipeline, batch_data
            )
            results_label.extend([result["label"] for result in results])
        return results_label


sentiment_analyzer = SentimentAnalyzer()
