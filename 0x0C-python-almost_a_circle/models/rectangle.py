#!/usr/bin/python3
"""Class rectangle"""


class Rectangle(Base):
    """implement base"""
    def __init__(self, width, height, x=0, y=0, id=None)
    """initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
