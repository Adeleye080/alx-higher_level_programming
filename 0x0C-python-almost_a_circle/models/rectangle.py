#!/usr/bin/python3
""" Module rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ check input """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ check input """
        return self.__width

    @property
    def height(self):
        """ check input """
        return self._height

    @property
    def x(self):
        """ check input """
        return self.__x

    @property
    def y(self):
        """ check input """
        return self.__y

    @width.setter
    def width(self, value):
        """ checks input """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ checks input """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ checks input """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ checks input """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the Area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ checks input """
        if self.__y > 0:
            print("\n" * self.__y)
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x + "#" * self.__width)
            else:
                print("#" * self.__width)

    def __str__(self):
        """ check input """
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ check input """
        attrs = [self.id, self.__width, self.__height, self.__x, self.__y]
        var = ('id', 'width', 'height', 'x', 'y')
        if kwargs is not None and (args is None or len(args) == 0):
            for key, value in kwargs.items():
                if key in var:
                    attrs[var.index(key)] = value
            (self.id, self.__width, self.__height, self.__x, self.__y) = attrs
        else:
            args_aux = list(attrs[i] for i in range(len(args), 5))
            args_aux2 = list(args) + args_aux
            (self.id, self.__width, self.__height,
             self.__x, self.__y) = args_aux2

    def to_dictionary(self):
        """ checks input """
        dictionary = {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dictionary
