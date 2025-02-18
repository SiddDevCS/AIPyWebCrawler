import os
from dotenv import load_dotenv
import logging

# Load the environment variables
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "gpt-3.5-turbo"
    TEMPERATURE = 0.7
    MAX_TOKENS = 150

    @staticmethod
    def validate():
        logging.info(f"API Key loaded: {Config.OPENAI_API_KEY[:10]}...")  # Only log first 10 chars for security
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

# Add this line at the end
Config.validate()