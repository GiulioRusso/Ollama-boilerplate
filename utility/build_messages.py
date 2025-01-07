def build_messages(user_prompt: str,
                   system_prompt: str = "You are a helpful assistant.") -> list:
    """
    Builds the OpenAI API message structure.

    :param user_prompt: user prompt.
    :param system_prompt: system prompt. Default is "You are a helpful assistant.".

    :return messages list.
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    return messages