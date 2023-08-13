from newsapi import NewsApiClient
import yaml
from utility.read_yaml import *

# Function to get latest news
def get_latest_news(api_key, country_code):
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(country=country_code)

    if top_headlines["status"] == "ok":
        articles = top_headlines["articles"]
        return articles
    else:
        print(f"Failed to get news data. Error: {top_headlines['message']}")
        return None

def get_news():
    api_keys = read_api_keys("config.yml")
    # print(api_keys)
    news_api_key = api_keys['news_api_key']

    # Replace "us" with the country code for the country you want to get news from (e.g., "us" for the United States)
    country_code = "us"

    articles = get_latest_news(news_api_key, country_code)
    if articles is not None:
        # return articles; will give an error because, dict is an unhasable type. i.e, it cannot be made a key.
        # we need to get titles from articles and then, convert it to a string. 
        news_reponse = " "
        for article in articles:
            title = article["title"]
            news_reponse += "\n"+title
        return "Latest headlines:\n--------------------------------------------------------"+news_reponse
    else:
        return 'SOME ERROR OCCURED.'
    


