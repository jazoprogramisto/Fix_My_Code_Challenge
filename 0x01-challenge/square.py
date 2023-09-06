#!/usr/bin/python3

class Square():
    """Module for class Square
    """
    def __init__(self, width=0, height=0):
        """Method that defines a square

        Attributes:
          - width: width of the square
          - height: height of the square
        """
        self.width = width
        self.height = heigiht

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__Main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
