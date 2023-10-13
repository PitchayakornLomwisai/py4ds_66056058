"""
Execise 2
"""


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # FIX : complete this
    warning_message = "please put your celsius temp"
    if celsius == None:
        return warning_message
    else:
        fahrenheit_temp = (9/5) * celsius + 32
        return fahrenheit_temp


def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # FIX : complete this
    warning_message = "please put your fahrenheit temp"
    if fahrenheit == None:
        return warning_message
    else:
        celsius = (fahrenheit - 32) * (5/9)
        return celsius

