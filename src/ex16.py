"""
Exercise 16
"""


def mode(list_data):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if len(list_data) == 0:
        return None

    frequency = {}
    for number in list_data:
        frequency.setdefault(number, 0)
        frequency[number] += 1

    highestFrequencyInLst = max(frequency.values())
    highestFrequencyLst = []

    for number, freq in frequency.items():
        if freq == highestFrequencyInLst:
            highestFrequencyLst.append(number)

    return highestFrequencyLst[0]
