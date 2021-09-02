class Shape:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
    
    def print_color(self):
        print(self.__color)

class Rectangle(Shape):
    def __init__(self, name, height, width):
        super().__init__("grey")
        self.__name = name
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __lt__(self, other):
        return self.__width < other.__width

    def __repr__(self):
        return f"Rectangle({self.__name}, {self.__height}, {self.__width}, {self.get_color()})"

class Circle(Shape):
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.__radius = radius

    def __repr__(self):
        return f"Cicle({self.__radius}, {self.get_color()})"

rect1 = Rectangle("nisse", 10, 20)
circle1 = Circle(123)
circle2 = Circle(333, "magenta")

circle1.set_color("blue")

print(rect1)
print(circle1)
print(circle2)