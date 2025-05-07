import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
serpapi_key = os.getenv("SERPAPI_API_KEY")

def get_learning_resources(query):
    search = GoogleSearch({
        "q": f"best resources for {query}",
        "api_key": serpapi_key,
        "num": 5
    })
    results = search.get_dict()
    links = []
    for item in results.get("organic_results", []):
        title = item.get("title")
        link = item.get("link")
        if title and link:
            links.append({"title": title, "link": link})
    return links