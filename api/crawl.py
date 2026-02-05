from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Crawl tool is running"}

@app.get("/crawl")
def crawl(url: str = Query(...)):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.title.text if soup.title else ""
    description = ""
    desc = soup.find("meta", attrs={"name": "description"})
    if desc:
        description = desc.get("content", "")

    return {
        "url": url,
        "title": title,
        "description": description
    }
