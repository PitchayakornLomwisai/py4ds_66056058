"""
Execise 1
"""


def greeting():
    """
    Function to print a greeting message in Thai language.
    """
    # FIX : complete this
    print("สวัสดีชาวลาดกระบัง")


def know_my_name():
    """
    Asks the user for their name and returns it.

    Parameters:
        None

    Returns:
        str: The name entered by the user.
    """
    # FIX : complete this
    name = str(input("Put your name"))
    return name


def say_hi(name=None):
    """
    Print a greeting message with the given name.

    Args:
        name (str, optional): The name to greet. Defaults to None.
    """
    # FIX : complete this
    say_hi_word = "สวัสดีคุณ"+name
    print(say_hi_word)
