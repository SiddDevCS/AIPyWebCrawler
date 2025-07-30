# Summarize will be here, with the help of OpenAI API
import requests
from bs4 import BeautifulSoup
import openai
import os

def crawl_and_extract_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.stripped_strings
        content = " ".join(texts)
        return content
    except Exception as e:
        return f"Error: {e}"

def summarize_with_openai(text):
    from openai import OpenAI
    client = OpenAI()  # Uses OPENAI_API_KEY from environment

    prompt = f"Summarize the following content in a concise paragraph:\n\n{text[:4000]}"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=256,
            temperature=0.5,
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"OpenAI error: {e}"