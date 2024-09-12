import asyncio
from transformers import pipeline


class NewsClassifier:
    def __init__(self, batch_size=25):
        self.classifier_pipeline = pipeline(
            "zero-shot-classification", model="cross-encoder/nli-MiniLM2-L6-H768"
        )
        self.candidate_labels = [
            "sports",
            "politics",
            "technology",
            "entertainment",
            "health",
            "business",
            "economy",
            "unknown",
        ]
        self.batch_size = batch_size

    async def classify(self, data):
        results = await asyncio.get_running_loop().run_in_executor(
            None,
            lambda: self.classifier_pipeline(
                data, candidate_labels=self.candidate_labels, batch_size=self.batch_size
            ),
        )
        return [result["labels"][0] for result in results]


news_classifier = NewsClassifier()
