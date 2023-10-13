"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    hours, remainder = divmod(tsec, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_time = ""
    if hours > 0:
        formatted_time += f"{hours}h "
    if minutes > 0:
        formatted_time += f"{minutes}m "
    if seconds > 0 or (tsec == 0 and (hours == 0 and minutes == 0)):
        formatted_time += f"{seconds}s"

    return formatted_time.strip()
