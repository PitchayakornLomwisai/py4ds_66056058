"""
Exercise 17
"""
import random


def roll_dice(num_of_dice):
    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """
    if num_of_dice <= 0:
        return 0

    total_sum = sum(random.randint(1, 6) for _ in range(num_of_dice))
    return total_sum
