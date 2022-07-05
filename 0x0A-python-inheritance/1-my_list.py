#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """Inherit from list"""
    def print_sorted(self):
        """Prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
