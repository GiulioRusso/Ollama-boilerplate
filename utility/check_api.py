import sys
import requests

def check_api(api: str,
              debug: bool) -> None:
    """
    Checks the validity of the API.

    :param api: The API to validate.
    :param debug: Debug flat.
    """
    if not api:
        print("!!! ERROR: No API key was found. Please check the .env file and make sure the API key is specified as 'OLLAMA_API=http://localhost:11434/' ")
        return sys.exit(1)

    # check if the endpoint URL is valid
    try:
        response = requests.get(api, timeout=5)  # 5-second timeout for quick feedback
        if response.status_code == 200:
            print("--> DEBUG: OLLAMA_API is valid and the server is running.")
            return True
        else:
            print(f"!!! ERROR: Server responded with status code {response.status_code}. Run 'ollama serve' in your terminal.")
            return sys.exit(1)
    except requests.ConnectionError:
        print("!!! ERROR: Could not connect to the server. Ensure the localhost is running. Run 'ollama serve' in your terminal.")
        return sys.exit(1)
    except requests.Timeout:
        print("!!! ERROR: Connection to the server timed out. Check the server status.")
        return sys.exit(1)
    except Exception as e:
        print(f"!!! ERROR: An unexpected error occurred: {str(e)}")
        return sys.exit(1)