#!/usr/bin/python3
"""This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class Square:
    """ Class Square with constuctor method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class Square
        Arg
            size: size to initializate __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Calculate the area of a square
        Returns:
            The area of the square
        """
        return self.__size ** 2
