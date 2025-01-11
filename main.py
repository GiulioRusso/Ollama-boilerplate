import argparse
from utility.load_api import load_api
from utility.display_init_terminal import display_init_terminal
from utility.read_prompt import read_prompt
from utility.build_messages import build_messages
from utility.call_Ollama import call_Ollama

def main(system_prompt_path: str, model: str) -> None:

    # load API from .env file
    load_api(debug=True)

    # load the welcome print
    display_init_terminal()

    # build the message for the OpenAI API
    messages = build_messages(
        system_prompt=read_prompt(file_path=system_prompt_path),
        user_prompt=input(">>> ")
    )

    # call Ollama API
    call_Ollama(messages=messages, model=model, debug=True)


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(description="Run Ollama with specified prompts and model.")
    
    # define command-line arguments
    parser.add_argument('--system_prompt', '--sp', type=str, required=True, 
                        help="Path to the system prompt text file.")
    parser.add_argument('--model', '--m', type=str, required=True, 
                        help="The model string to use (e.g., 'llama3.2').")
    
    # parse the arguments
    args = parser.parse_args()

    # run the main function with the parsed arguments
    main(system_prompt_path=args.system_prompt,
         model=args.model)