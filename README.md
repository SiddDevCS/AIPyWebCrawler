# AI Web Crawler

This is a Python-based AI Web Crawler that crawls websites and collects data. It uses techniques to navigate web pages and extract valuable information, which can be used for various purposes such as data mining, SEO analysis, or gathering data for machine learning models.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Siddharth11sehgal/AIPyWebCrawler.git
   ```

2. Navigate to the project folder:
   ```
   cd AIPyWebCrawler
   ```

3. Set up a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Once you've installed the dependencies, you can run the web crawler script:
   ```
   python app.py
   ```

2. Customize the script with your desired crawling settings, such as the URLs to start from, the depth of the crawl, and the type of data to scrape.

> #2 Is not necessary, changes may be made if wanted.

3. Send a POST request with your url like this:

```bash
curl -X POST http://127.0.0.1:8000/summarize \
     -H "Content-Type: application/json" \
     -d '{"url": "https://your-url-here.com"}'
```

Example:

```bash
siddsehgal@111 ~ % curl -X POST http://127.0.0.1:8000/summarize \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'      
{
  "summary": "The content is about the use of the domain \"example.com\" for illustrative purposes in documents without needing prior permission. It states that the domain can be freely utilized in literature as an example without coordination or approval. Additional information is available for reference."
}
```

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. Here’s how you can contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request