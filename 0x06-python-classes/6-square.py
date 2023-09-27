#!/usr/bin/python3
'''Private instance'''


class Square:
    '''square size'''
    def __init__(self, size=0, position=(0, 0)):
        '''initialization'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Getter'''
        return self.__position

    @position.setter
    '''setter'''
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''print square'''
        if (self.__size == 0):
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for x in range(self.__size)]
            print("")
