"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    if 10 <= num % 100 <= 20:
        suffix = "th"
    else:
        last_digit = num % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return str(num) + suffix
