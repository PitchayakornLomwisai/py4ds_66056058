"""
Exercise 24 : Every 15 minutes, ante meridiem (am) and post meridiem (pm)
ante : before
post : after
meridiem : midday
"""


def get_time_every_15_min():
    """
    Generate a time string every 15 minutes.

    This function iterates through the meridiems, hours, and minutes to generate a time string
    for every 15 minutes. It prints the time string in the format "hour:minute meridiem".

    Returns:
        str: The generated time string.
    """
    # FIX : complete this

    meridiems = ['am', 'pm']

    for meridiem in meridiems:
        for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            for minute in ['00', '15', '30', '45']:
                time_string = f"{hour}:{minute} {meridiem}"

                print(time_string)
