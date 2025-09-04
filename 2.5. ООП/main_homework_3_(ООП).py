"""
Задача 1: Класс "Круг"
Создайте класс Circle, который будет иметь атрибут радиуса
и методы для вычисления площади и периметра круга.
"""
print(f"\nЗадача 1: Класс 'Круг'")
from math import pi

class Circle:
    radius = 0

    def my_radius(self):

        s = pi * self.radius**2
        c = 2 * pi * self.radius

        print(f"площадь круга: {round(s, 2)}")
        print(f"периметр круга: {round(c, 2)}")

my_s_c = Circle()
my_s_c.radius = 1
my_s_c.my_radius()

"""
Задача 2: Класс "Прямоугольник"
Создайте класс Rectangle, который будет иметь атрибуты ширины
и высоты, а также методы для вычисления площади и периметра.
"""
print(f"\nЗадача 2: Класс 'Прямоугольник'")
class Rectangle:
    width = 0
    height = 0

    def my_square(self):
        s = self.width * self.height
        print(f"площадь прямоугольника - {s}")

    def my_perimeter(self):
        p = 2 * (self.width + self.height)
        print(f"периметр прямоугольника - {p}")

my_rectangle = Rectangle()
my_rectangle.width = 1
my_rectangle.height = 1
my_rectangle.my_square()
my_rectangle.my_perimeter()

"""
Задача 3: Класс "Счетчик"
Создайте класс Counter, который будет иметь метод для
увеличения счетчика на 1 и метод для получения текущего значения счетчика.
"""
print("\nЗадача 3: Класс 'Счетчик'")
class Counter:
    counter = 0

    def my_counter(self):
        self.counter += 1

    def get_counter(self):
        print(f"текущее значение счётчика: {self.counter}")


my_counter = Counter()
my_counter.counter = 10
my_counter.my_counter()
my_counter.get_counter()

"""
Задача 4: Класс "Автомобиль"
Создайте класс Car, который будет иметь атрибуты для марки,
модели и года выпуска. Добавьте метод для отображения информации об автомобиле.
"""
print("\nЗадача 4: Класс 'Автомобиль'")
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self. model = model
        self.year = year

    def my_info(self):
        print(f"""
        информация об автомобиле:
                                марка - {self.brand}, 
                                модель - {self. model},
                                год выпуска - {self.year}""")

my_car = Car("TIGGO", "T11", 2012)
my_car.my_info()

"""
Задача 5: Класс "Студент"
Создайте класс Student, который будет иметь атрибуты имени,
фамилии и списка оценок. Реализуйте методы для добавления оценки и
вычисления среднего балла.
"""
print("\nЗадача 5: Класс 'Студент'")
class Student:

    def __init__(self, name, surname, *grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def my_grade(self, *grade1):

        self.grade1 = self.grade + grade1
        print(f"{self.name}, {self.surname}, {self.grade1}")

        x = 0
        for i in self.grade1:
            x += i
        print(f"средняя оценка: {round(x / len(self.grade1), 0)}")

stud_1 = Student("Вася", "Васечкин", 5,4,4,4,4,4,5)
stud_1.my_grade(7)