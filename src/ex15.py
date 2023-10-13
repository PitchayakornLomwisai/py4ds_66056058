"""
Exercise 15
"""


def median(list_data):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    sortedLst = sorted(list_data)
    lstLen = len(list_data)
    index = (lstLen - 1) // 2

    if len(list_data) == 0:
        return None
    elif (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
