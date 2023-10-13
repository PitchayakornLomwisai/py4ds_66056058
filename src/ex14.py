"""
Exercise 14
"""


def average(list_data) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    sum = 0
    if len(list_data) == 0:
        return sum
    else:
        for i in list_data:
            sum = sum + i
        return sum/len(list_data)
