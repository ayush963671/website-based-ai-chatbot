import requests
from bs4 import BeautifulSoup


def crawl_website(url: str) -> dict:
    headers = {"User-Agent":  (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No Title"

    main = soup.find("div", id="mw-content-text")
    if not main:
        raise ValueError("Main content not found")

    paragraphs = main.find_all("p")
    text = " ".join(p.get_text(strip=True) for p in paragraphs)

    if len(text) < 200:
        raise ValueError("Insufficient textual content")

    return {
        "url": url,
        "title": title,
        "text": text
    }
