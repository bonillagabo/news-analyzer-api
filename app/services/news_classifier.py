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
            "others",
        ]
        self.batch_size = batch_size

    def batch(self, iterable, n=1):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx : min(ndx + n, l)]

    async def classify(self, data):
        results_label = []
        for batch_data in self.batch(data, self.batch_size):
            results = await asyncio.get_running_loop().run_in_executor(
                None, self.classifier_pipeline, batch_data, self.candidate_labels
            )
            results_label.extend([result["labels"][0] for result in results])
        return results_label


news_classifier = NewsClassifier()
