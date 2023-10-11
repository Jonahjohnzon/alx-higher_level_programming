#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""
    def area(self):
        """when called start an exception"""
        raise Exception("area() is not implemented")
