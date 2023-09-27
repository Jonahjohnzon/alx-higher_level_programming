#!/usr/bin/python3
'''Private instance'''


class Square:
    '''square size'''
    def __init__(self, size=0):
        '''initialization'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
