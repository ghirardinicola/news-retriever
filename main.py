import json
import requests
import os

class NewsDataClient:
    BASE_URL = "https://newsdata.io/api/1"
    # For example
    # https://newsdata.io/api/1/news?apikey=pub_28005ea204110770a684764e4b10d2e6b376c&country=it&category=environment 

    def __init__(self, api_key):
        self.api_key = api_key

    def get_latest_news(self, country=None, category=None):
        """Get the latest news with optional country and category parameters"""
        endpoint = "/news"
        query_params = {}
        query_params['apikey'] = api_key
        if country:
            query_params['country'] = country
        if category:
            query_params['category'] = category

        response = requests.get(self.BASE_URL + endpoint, params=query_params, timeout=1000)
        return response.json()

    def get_news_by_date(self, date, country=None, category=None):
        """Get news by a specific date with optional country and category parameters"""
        endpoint = f"/news/{date}"
        query_params = {}
        query_params['apikey'] = api_key

        if country:
            query_params['country'] = country
        if category:
            query_params['category'] = category

        response = requests.get(self.BASE_URL + endpoint,params=query_params, timeout=100)
        print(response)
        return response.json()

# Usage
if __name__ == "__main__":

    api_key = os.environ.get("NEWSDATA_API_KEY")
    client = NewsDataClient(api_key)

    # Fetch the latest news with country and category
    latest_news = client.get_latest_news(country="IT", category="environment")
    print(latest_news)

    # Fetch news by a specific date with country and category (e.g., "2023-08-20")
    #news_by_date = client.get_news_by_date("2023-08-20", country="US", category="politics")
    #print(news_by_date)