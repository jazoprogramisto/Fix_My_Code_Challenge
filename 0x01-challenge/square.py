#!/usr/bin/python3
"""
Module for class Square
"""


class Square():
    """ Defines square

    Attributes:
        - width: width of the square
        - height: height of the square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Class instantiation
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable rep
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
