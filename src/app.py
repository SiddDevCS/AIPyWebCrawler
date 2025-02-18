from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawler import WebCrawler
from summarizer import TextSummarizer
import uvicorn

app = FastAPI(title="Web Crawler and Summarizer API")

class URLInput(BaseModel):
    url: str

# Initialize the crawler and summarizer
crawler = WebCrawler()
summarizer = TextSummarizer()

@app.post("/summarize")
async def summarize_url(url_input: URLInput):
    try:
        text = crawler.crawl(url_input.url)
        if not text:
            raise HTTPException(status_code=404, detail="No content found on the page")
        summary = summarizer.summarize(text)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)