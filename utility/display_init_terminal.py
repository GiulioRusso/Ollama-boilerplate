import sys

def display_init_terminal():
    """
    Display the welcome message with a funny ASCII art
    """

    file_path = './prompts/init_terminal.txt'

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
        
    except FileNotFoundError:
        print(f"!!! ERROR: The init file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"!!! ERROR: An error occurred: {e}")
        sys.exit(1)