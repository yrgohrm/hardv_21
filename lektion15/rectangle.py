class Rectangle:
    def __init__(self, name, height, width):
        self.__name = name
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __lt__(self, other):
        return self.__width < other.__width

    def __repr__(self):
        return f"Rectangle({self.__name}, {self.__height}, {self.__width})"

