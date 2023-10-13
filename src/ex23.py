"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(num_bottles):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # TODO : complete this
    if num_bottles == 1:
        msg = "1 bottle of beer on the wall,\n1 bottle of beer.\nTake one down, pass it around,\nNo more bottles of beer on the wall!\n"
    else:
        msg = f"{num_bottles} bottles of beer on the wall,\n{num_bottles} bottles of beer.\nTake one down, pass it around,\n{num_bottles-1} bottles of beer on the wall.\n"
    return msg

def loop_bottles_of_bears(bottles):
    while bottles > 0:
        print(bottles_of_beer(bottles))
        bottles -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
