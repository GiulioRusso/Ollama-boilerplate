import ollama


def call_Ollama(messages: list,
                model: str) -> None:
    """
    Call the Ollama API to query the model. Print the response content.

    :param messages: input message in the Ollama API format.
    """

    try:
        # call Ollama
        response = ollama.chat(model=model, messages=messages)
        
        # print Ollama response
        ollama_response = response['message']['content']
        
        print("\n\t>>> Ollama Response: ")
        print(ollama_response)

    except Exception as e:

        print(f"\n\t>>> ERROR: An unexpected error occurred: {str(e)}")