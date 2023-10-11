#!/usr/bin/python3
"""
Contains  function
"""


def inherits_from(obj, a_class):
    """returns boolean"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
