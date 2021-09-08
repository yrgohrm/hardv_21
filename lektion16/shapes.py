
class Triangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        print(self.__height * self.__width / 2)

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        print(self.__height * self.__width)
