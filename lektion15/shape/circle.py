class Circle:
    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius

    def area(self):
        return 3.1415 * self.__radius * self.__radius

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __repr__(self):
        return f"Circle({self.__name}, {self.__radius})"

