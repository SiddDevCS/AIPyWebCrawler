import requests
from bs4 import BeautifulSoup
import logging
from typing import Optional

class WebCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def crawl(self, url: str) -> Optional[str]:
        try:
            # Add headers to mimic a browser
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()
            
            # Get the main content
            # For BBC specifically
            if 'bbc.com' in url:
                main_content = soup.find('article') or soup.find(class_='article')
            else:
                main_content = soup.find('main') or soup.find('article') or soup.find('body')
            
            if main_content:
                # Extract text and clean it up
                text = ' '.join([p.get_text().strip() for p in main_content.find_all(['p', 'h1', 'h2', 'h3'])])
                return text
            else:
                return "No main content found on the page."

        except requests.RequestException as e:
            logging.error(f"Error crawling URL {url}: {str(e)}")
            raise