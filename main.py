import os
from ner import get_answers_from_gpt
from news import NewsDataClient
# Usage
if __name__ == "__main__":

    api_key = os.environ.get("NEWSDATA_API_KEY")
    client = NewsDataClient(api_key)

    # Fetch the latest news with country and category
    latest_news = client.get_latest_news(country="IT", category="environment")
    print(latest_news)

    content=latest_news["results"][0]["description"]
    # Fetch news by a specific date with country and category (e.g., "2023-08-20")
    #news_by_date = client.get_news_by_date("2023-08-20", country="US", category="politics")
    #print(news_by_date)
    questions=["Di quali luoghi si parla nell'articolo?"]

    responses = get_answers_from_gpt(content, questions)
    for q, a in zip(questions, responses):
        print(f"Q: {q}\nA: {a}\n")