#!/usr/bin/python3
"""
Module for User class
"""


class User():
    """ Defines class square

    Attributes:
        - email: user email
    """
    def __init__(self):
        """ Initializes the class user """
        self.__email = None

    @property
    def email(self):
        """ Decorator of the attr """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter attr """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
