"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(p1, p2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    # FIX : complete this
    winning_condition = {
        ('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')
    }

    # check invalid Input
    if p1 not in {'rock', 'paper', 'scissors'} or p2 not in {'rock', 'paper', 'scissors'}:
        return "Invalid choice"


    if p1 == p2:
        return "tie"
    elif (p1, p2) in winning_condition:
        return "player one"
    else:
        return "player two"
