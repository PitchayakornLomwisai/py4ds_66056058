"""
Exercise 13
"""


def calc_sum(lst):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    if len(lst) == 0:
        return 0
    else:
        return sum(lst)


def calc_prod(lst):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    result = 1
    if len(lst) == 0:
        return result
    else:
        for i in lst:
            result = result * i
        print(result)
        return result
