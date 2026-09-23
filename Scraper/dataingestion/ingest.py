import requests
import xml.etree.ElementTree as ET

def fetch_news():
    url = "https://feeds.bbci.co.uk/news/world/rss.xml"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200: return []
        root = ET.fromstring(response.text.strip().encode("utf-8"))
        articles = []
        for item in root.findall(".//item"):
            articles.append({
                "title": item.find("title").text if item.find("title") is not None else "No Title",
                "link": item.find("link").text if item.find("link") is not None else "",
                "description": item.find("description").text if item.find("description") is not None else ""
            })
        print(f"Successfully fetched {len(articles)} news articles!")
        return articles
    except Exception as e:
        print("Error fetching data:", e)
        return []
