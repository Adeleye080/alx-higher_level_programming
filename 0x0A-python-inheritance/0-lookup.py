#!/usr/bin/python3
"""  This module contains a function that returns the available attributes 
and method of an object
"""


def lookup(obj):
    """returns available methods and attributes"""
    return dir(obj)
