#!/usr/bin/python3
""" Module to manage id attribute
"""


class Base:
    """ Base class that manage id attribute
    Args:
        id: given value or assigned when not given
        __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
