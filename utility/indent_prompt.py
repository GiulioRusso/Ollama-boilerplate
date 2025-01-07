def indent_prompt(input_str: str) -> str:
    """
    Adds three tab characters at the beginning of each line in the input string.

    :return indented string.
    """
    
    # split the input string into lines and add three tabs to the start of each line
    indented_str = "\n".join(["\t\t\t" + line for line in input_str.splitlines()])
    
    return indented_str
