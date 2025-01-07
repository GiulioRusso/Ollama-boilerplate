import os

from dotenv import load_dotenv
from utility.check_api import check_api


def load_api() -> None:
    """
    Loads the Ollama API from the .env file.
    """

    # load key from .env file
    load_dotenv(override=True)
    api = os.getenv('OLLAMA_API')

    # check API key
    check_api(api=api)
