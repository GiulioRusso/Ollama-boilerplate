import ollama

def print_response(response: ollama.ListResponse):
    """
    Print Ollama response with typewriter effect.

    :param response: Ollama ListResponse object
    """
    
    print("\n>>> ", end='')
    for chunk in response:
        content = chunk.get('message', {}).get('content', '')
        print(content, end='', flush=True)  # print each chunk as it arrives
