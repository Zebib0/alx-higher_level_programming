#!/usr/bin/python3i

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print('#', end="")
                print("")
