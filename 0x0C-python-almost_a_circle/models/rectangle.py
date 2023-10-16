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
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Area of rectangle."""
        return self.width * self.height

    def display(self):
        """
            stdout the rectangle instance with '#'
        """
        rec = ""
        ps = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rec += (" " * self.x) + (ps*self.width) + "\n"
        print(rec, end="")
