#!/usr/bin/python3
"""Class rectangle"""
from models.base import Base


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

    @property
    def x(self):
        """getter/setter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter/setters"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

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

    def __str__(self):
        """print() and str() rep of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ functtion"""
        if (len(args) == 0):
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
