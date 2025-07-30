# /summarize will go here, so crawl -> pass it onto openai api
import requests
from bs4 import BeautifulSoup

def crawl_and_extract_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract all visible text
        texts = soup.stripped_strings
        content = " ".join(texts)
        return content
    except Exception as e:
        return f"Error: {e}"