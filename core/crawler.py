import requests
from bs4 import BeautifulSoup
import re

def crawl_website(url: str) -> dict:
     headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

     response = requests.get(url, headers=headers, timeout=15)
     response.raise_for_status()

     soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
     for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()

     title = soup.title.string.strip() if soup.title else "No Title"

    # Extract all visible text
     text = soup.get_text(separator=" ")

    # Clean whitespace
     text = re.sub(r"\s+", " ", text).strip()

     if len(text) < 300:
        raise ValueError("Not enough readable text found")

     return {
        "url": url,
        "title": title,
        "text": text
    }