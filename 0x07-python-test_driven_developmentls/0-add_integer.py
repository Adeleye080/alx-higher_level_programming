#!/usr/bin/python3
"""

This module is composed by a function that add two integers

"""


def add_integer(a, b=98):
    """Function that add two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
