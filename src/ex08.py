"""
Execise 8
"""


def write_to_file(filename, message):
    """
    Write the given message to a file with the provided filename.

    Args:
        filename (str): The name of the file to write to.
        message (str): The message to write to the file.

    Returns:
        None
    """
    # FIX : complete this
    with open(filename, "w") as file:
        file.write(message)


def read_from_file(filename):
    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    # FIX : complete this

    with open(filename, "r") as file:
        contents = file.read()
    return contents



def append_to_file(filename, message):
    """
    Append the given message to the end of the specified file.

    Args:
        filename (str): The name of the file to append the message to.
        message (str): The message to append to the file.

    Returns:
        None: This function does not return anything.
    """
    # FIX : complete this
    with open(filename, "a") as file:
        file.write(message)
