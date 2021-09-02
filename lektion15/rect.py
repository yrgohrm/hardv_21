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

rect1 = Rectangle("nisse", 10, 20)
rect2 = Rectangle("bosse", 33, 15)

print(rect1.area())  # =====>  area(rect1)
print(rect2.area())

if rect2 < rect1:   # ===>  Rectangle.__lt__(rect2, rect1)
    print("rect 2 är minst")
else:
    print("rect 1 är minst")

rect3 = Rectangle("kalle", 1,1)

rectlist = [ rect1, rect2, rect3 ]
rectlist.sort()
print(rectlist)


def do_stuff_with_rect(rect):
    print("Här är en rektangle: " + str(rect))



do_stuff_with_rect(rect1)
