from openai import OpenAI
from config import Config
import logging

class TextSummarizer:
    def __init__(self):
        try:
            logging.info("Initializing OpenAI client...")
            self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
            logging.info("OpenAI client initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing OpenAI client: {str(e)}")
            raise

    def summarize(self, text: str) -> str:
        try:
            if not text.strip():
                return "No content to summarize."

            logging.info("Sending request to OpenAI...")
            response = self.client.chat.completions.create(
                model=Config.MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that creates clear, concise summaries."},
                    {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
                ],
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS
            )
            logging.info("Received response from OpenAI")

            return response.choices[0].message.content.strip()

        except Exception as e:
            logging.error(f"Error in summarization: {str(e)}")
            raise