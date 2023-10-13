"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year

    # FIX : complete this
    if (year < 1 or month < 1 or month > 12 or day < 1):
        return False

    max_days_per_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day > max_days_per_month[month - 1]:
        return False

    return True
