def debug_print(messages: list, model: str) -> None:
    """
    Prints the system prompt, user prompt, and the model being used for debugging.

    :param messages: A list of message dictionaries containing 'system' and 'user' prompts.
    :param model: The name of the model being used (e.g. 'gpt-4o-mini').
    """
    
    # check if messages contain both system and user prompts
    system_prompt = next((msg['content'] for msg in messages if msg['role'] == 'system'), None)
    user_prompt = next((msg['content'] for msg in messages if msg['role'] == 'user'), None)

    # print system and user prompts
    print(f"\n--> DEBUG: \n\n├── System prompt: {system_prompt}\n├── User prompt: {user_prompt}\n├── Model: {model}")