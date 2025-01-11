import ollama
from utility.debug_print import debug_print
from utility.print_response import print_response


def call_Ollama(messages: list,
                model: str,
                debug: bool = False) -> None:
    """
    Call the Ollama API to query the model. Print the response content.

    :param messages: input message in the Ollama API format.
    :param model: Ollama model.
    _param debug: Debug flag.
    """

    try:
        # debug print
        if debug:
            debug_print(messages=messages, model=model)

        # call Ollama
        response = ollama.chat(model=model,
                               messages=messages,
                               stream=True)

        # print Ollama response
        print_response(response=response)

    except Exception as e:

        print(f"!!! ERROR: An unexpected error occurred: {str(e)}")