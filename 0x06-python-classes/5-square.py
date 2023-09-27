#!/usr/bin/python3
'''Private instance'''


class Square:
    '''square size'''
    def __init__(self, size=0):
        '''initialization'''
        self.__size = size

    def area(self):
        '''area'''
        return self.__size ** 2

    @property
    def size(self):
        '''getters'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setters'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''print square'''
        if (self.__size == 0):
            print("")
        for x in range(0, self.__size):
            [print("#", end="") for x in range(self.__size)]
            print("")
