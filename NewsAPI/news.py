#Load Library
import requests
from datetime import datetime

#Write API key and URL
API_KEY = "adaab206b93a415a9454c0a8963ef289"
news_url = "https://newsapi.org/v2/top-headlines"

#Define get_top_headlines
def get_top_headlines(category):


    querystring = {
        "from" : datetime.now().strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "apiKey": API_KEY, 
        "category": category,
        "language": "en",
    }
    headers = {'Content-type': 'application/json'}

    response = requests.request("GET", news_url, headers=headers, params=querystring)
#Handle user inputs
    if response.status_code == 200:
        return True, response.json()

    return False, "Error"
