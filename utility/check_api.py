import sys
import requests

def check_api(api: str) -> None:
    """
    Checks the validity of the API.

    :param api: The API to validate.
    """
    if not api:
        print("\n\t>>> ERROR: No API key was found. Please check the .env file and make sure the API key is specified as 'OLLAMA_API=http://localhost:11434/' ")
        return sys.exit(1)

    # check if the endpoint URL is valid
    try:
        response = requests.get(api, timeout=5)  # 5-second timeout for quick feedback
        if response.status_code == 200:
            print("\n\t>>> MESSAGE: OLLAMA_API is valid and the server is running.")
            return True
        else:
            print(f"\n\t>>> ERROR: Server responded with status code {response.status_code}. Run 'ollama serve' in your terminal.")
            return False
    except requests.ConnectionError:
        print("\n\t>>> ERROR: Could not connect to the server. Ensure the localhost is running. Run 'ollama serve' in your terminal.")
        return False
    except requests.Timeout:
        print("\n\t>>> ERROR: Connection to the server timed out. Check the server status.")
        return False
    except Exception as e:
        print(f"\n\t>>> ERROR: An unexpected error occurred: {str(e)}")
        return False