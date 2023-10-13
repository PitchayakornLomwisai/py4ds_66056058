"""
Execise 7
"""


def print_ASCII_table(start_char, end_char):
    """
    Generate and print the ASCII table for a range of characters.

    Args:
        start_char (int): The ASCII value of the starting character.
        end_char (int): The ASCII value of the ending character.

    Returns:
        str: Returns nothing. The function simply prints the ASCII characters.

    """
    # FIX : complete this
    if start_char <= end_char:
        for char_code in range(start_char, end_char + 1):
            character = chr(char_code)
            print(f"{character}")
    else:
        print("Invalid range: start_char must be less than or equal to end_char")
