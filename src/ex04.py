"""
Execise 4
"""


def area(length, width):
    """
    Calculates the area of a rectangle given its length and width.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    # FIX : complete this
    area_cal = length * width
    return area_cal


def perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    # FIX : complete this
    perimeter_cal = 2 * (length + width)
    return perimeter_cal


def volume(length, width, height):
    """
    Calculates the volume of an object given its length, width, and height.

    Args:
        length (float): The length of the object.
        width (float): The width of the object.
        height (float): The height of the object.

    Returns:
        float: The volume of the object.
    """
    # FIX : complete this
    vol_cal = length * width * height
    return vol_cal


def surface_area(length, width, height):
    """
    Calculate the surface area of a rectangular prism.

    Parameters:
        length (float): The length of the rectangular prism.
        width (float): The width of the rectangular prism.
        height (float): The height of the rectangular prism.

    Returns:
        float: The total surface area of the rectangular prism.
    """
    # FIX : complete this
    surface_area_cal = 2 * (width * length) + 2 * (height * width) + 2 * ( length * height)
    return surface_area_cal
