def read_file(file_path: str) -> str:
    """
    Reads the content of a text file and returns it as a string.

    :param file_path: The path to the text file to read.

    :return the content of the file as a string.
    """
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"\n\t>>> ERROR: The file at {file_path} was not found.")
    except IOError as e:
        raise IOError(f"\n\t>>> ERROR: An error occurred while reading the file: {e}")
