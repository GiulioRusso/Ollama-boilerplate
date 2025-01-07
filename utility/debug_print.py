from utility.indent_prompt import indent_prompt

def debug_print(messages: list, model: str) -> None:
    """
    Prints the system prompt, user prompt, and the model being used for debugging.

    :param messages: A list of message dictionaries containing 'system' and 'user' prompts.
    :param model: The name of the model being used (e.g. 'gpt-4o-mini').
    """
    
    # check if messages contain both system and user prompts
    system_prompt = next((msg['content'] for msg in messages if msg['role'] == 'system'), None)
    user_prompt = next((msg['content'] for msg in messages if msg['role'] == 'user'), None)

    # indent prompts
    system_prompt = indent_prompt(system_prompt)
    user_prompt = indent_prompt(user_prompt)

    # print system and user prompts
    print(f"\n\t>>> DEBUG: \n\n\t\tSystem prompt: \n\n{system_prompt}")
    print(f"\n\t\tUser prompt: \n\n{user_prompt}")
    
    # print model name
    print(f"\n\t\tModel: {model}")
