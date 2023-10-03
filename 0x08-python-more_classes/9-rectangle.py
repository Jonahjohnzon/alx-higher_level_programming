#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/setter."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/setter."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the Rectangle."""
        return (self.__width * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle with the greater area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Rectangle with width and height equal to size
        """
        return (cls(size, size))

    def perimeter(self):
        """perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """printable representation of the Rectangle.
        """
        if (self.__width == 0 or self.__height == 0):
            return ("")

        rec = []
        for index in range(self.__height):
            [rec.append(str(self.print_symbol)) for a in range(self.__width)]
            if index != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """ representation of the Rectangle."""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """a message for every deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")