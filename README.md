# News Analyzer API

This is a personal project built with FastAPI that consumes the [NewsAPI](https://newsapi.org/) to fetch news articles. It uses two transformer models to perform sentiment analysis on the news titles and classify the news into general topics. The processing is optimized to run on the CPU using asyncio, allowing the models to run in parallel and improve response times.

## Technologies used

- **FastAPI**: Modern and asynchronous web framework for building APIs.
- **httpx**: Asynchronous HTTP client to consume the NewsAPI.
- **Transformers**: Library for using pre-trained language models.
- **Asyncio**: Used for parallel execution of the models to improve performance on the CPU.

The models used in this project are:

- [finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis): For sentiment analysis on the news title.
- [cross-encoder/nli-MiniLM2-L6-H768](https://huggingface.co/cross-encoder/nli-MiniLM2-L6-H768): For classifying the news into general topics.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/bonillagabo/news-analyzer-api.git
    cd news-analyzer-api

2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt

4. Create the .env file from the .env.example and add your NewsAPI key:

    ```bash
    cp .env.example .env

    Then, edit the .env file to add your API key:
    NEWS_API_KEY=your_api_key_here

## Usage

1. Start the FastAPI application:

    ```bash
    fastapi dev app/main.py

2. Go to http://127.0.0.1:8000/docs to access the interactive Swagger UI and test the endpoints.

## Notes

- The transformers models used are configured to run on the CPU. If you want to use a GPU, you’ll need to modify the configuration to enable hardware acceleration.
- Using asyncio allows the sentiment analysis and topic classification models to run in parallel, improving efficiency and reducing response time.
