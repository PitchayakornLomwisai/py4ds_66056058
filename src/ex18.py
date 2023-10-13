"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(num_coffees, price_per_coffee):
    """
    Calculate the total cost of buying a number of coffees with the "Buy 8 get 1 free" promotion.

    Args:
        num_coffees (int): The total number of coffees to buy.
        price_per_coffee (float): The cost of one cup of coffee.

    Returns:
        float: The total cost of buying the given number of coffees with the promotion.
    """
    cost = 0.0
    cups_until_free_coffee = 8

    while num_coffees > 0:
        if cups_until_free_coffee == 0:
            cups_until_free_coffee = 8
            num_coffees -= 1
        else:
            cost += price_per_coffee
            cups_until_free_coffee -= 1
            num_coffees -= 1

    return round(cost, 2)

def get_cost_of_coffee_2(num_coffees, price_per_coffee):
    """
    Calculate the total cost of buying a number of coffees with the "Buy 8 get 1 free" promotion.

    Args:
        num_coffees (int): The total number of coffees to buy.
        price_per_coffee (float): The cost of one cup of coffee.

    Returns:
        float: The total cost of buying the given number of coffees with the promotion.
    """
    cost = 0.0
    cups_until_free_coffee = 8

    while num_coffees > 0:
        if cups_until_free_coffee == 0:
            cups_until_free_coffee = 8
            num_coffees -= 1
        else:
            cost += price_per_coffee
            cups_until_free_coffee -= 1
            num_coffees -= 1

    return round(cost, 2)


