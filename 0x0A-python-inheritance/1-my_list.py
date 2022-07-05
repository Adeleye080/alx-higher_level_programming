#!/usr/bin/python3
"""class MyList inherit from list
"""


class MyList(list):
    """Inherit from list"""
    def print_sorted(self):
        """Prints list but sorted
        (ascending order)
        """
        print(sorted(self))
