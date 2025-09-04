"""
--------------------------------------------------------------------------------
                                        Полиморфизм
---------------------------------------------------------------------------------

Полиморфизм - использование единственной сущности(метод, оператор или объект)
для представления различных типов в различных сценариях использования.

например полиформизм  при сложении используется как оператор сложения и
конкатенации строк

1 + 2 = 3
a + b = ab
"""

"""
полиморфизм функций
функция len применена к разным типам данных
"""

print(len("sdfsdfs")) # строка
print(len(["sdfsdfs", "sdfsdfs"])) #список
print(len({1:"2", 2:"3"})) # словарь

"""
полиморфизм в классах

разные классы могут иметь одинаковый метод
"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


cat = Cat("Барсик", 3)
cat.info()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

dog = Dog("Гром", 5)
dog.info()

for animal in (cat, dog):
    animal.info()


"""
полиморфизм и наследование
"""

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "Я двумерная фигура"

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Квадрат")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "У квадрата все углы 90"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

a = Square(4)
b = Circle(7)

print(a)
print(b)
print(a.area())
print(b.area())

"""
абстрактные классы
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


def print_area(shape):
    print(f"Площадь:, {shape.area()}")


rectangle = Rectangle(30, 50)
circle = Circle(30)

print_area(rectangle)  # Area: 1500
print_area(circle)  # Area: 2826.0
















