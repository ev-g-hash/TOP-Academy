"""
Задача 1: Фигуры и их площади
Создайте абстрактный класс Shape, который будет содержать абстрактный метод area().
Реализуйте несколько подклассов, например, Circle, Rectangle и Triangle,
каждый из которых будет иметь свой способ вычисления площади.
"""
print("\nЗадача 1: Фигуры и их площади")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
            self.width = width
            self.height = height
    def area(self):
            return self.width * self.height

class Triangle(Shape):
    def __init__(self, l, h):
        self.l = l
        self.h = h
    def area(self):
            return (1 / 2 ) * self.l * self.h

circle = Circle(5)
rectangle = Rectangle(6, 5)
triangle = Triangle(5, 2)

print(f"площадь круга {circle.area()}")
print(f"площадь прямоугольника {rectangle.area()}")
print(f"площадь треугольника {triangle.area()}")

"""
Задача 2: Животные и их звуки
Создайте абстрактный класс Animal, который будет содержать абстрактный метод make_sound().
Реализуйте подклассы Dog, Cat и Cow, каждый из которых будет издавать свой звук.
"""
print("\nЗадача 2: Животные и их звуки")

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Gav gav"
class Cat(Animal):
    def make_sound(self):
        return "Meow meow"
class Cow(Animal):
    def make_sound(self):
        return "Muuuuuu"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())

"""
Задача 3: Транспортные средства и их скорость
Создайте абстрактный класс Vehicle, который будет содержать абстрактный метод speed(). 
Реализуйте подклассы Car, Bicycle и Airplane, 
каждый из которых будет возвращать свою максимальную скорость.
"""
print("\nЗадача 3: Транспортные средства и их скорость")

class Vehicle(ABC):

    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def speed(self):
        return "максимальная скорость Car - 200 км/ч."
class Bicycle(Vehicle):
    def speed(self):
        return "максимальная скорость Bicycle - 300 км/ч."
class Airplane(Vehicle):
    def speed(self):
        return "максимальная скорость  Airplane - 400 км/ч."

car = Car()
bicycle = Bicycle()
airplane = Airplane()

print(car.speed())
print(bicycle.speed())
print(airplane.speed())

"""
Задача 4: Система оплаты
Представьте, что вы разрабатываете систему для обработки платежей. 
У вас есть несколько типов платежей: кредитная карта, PayPal и криптовалюта. 
Каждый из этих типов платежей имеет свой способ обработки транзакций.

1. Создайте абстрактный класс Payment, который будет содержать абстрактный 
метод process_payment(amount).
2. Создайте три подкласса: CreditCardPayment, PayPalPayment и CryptoPayment. 
Каждый из них должен реализовать метод process_payment, 
который будет выводить сообщение о том, как именно обрабатывается платеж.
3. Напишите функцию process_all_payments, которая принимает список 
объектов типа Payment и обрабатывает каждый платеж.

"""
print("\nЗадача 4: Система оплаты")

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"{self.amount} обрабатывается CreditCardPayment"

class PayPalPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"{self.amount} обрабатывается PayPalPayment"

class CryptoPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"{self.amount} обрабатывается CryptoPayment"

def process_all_payments(payment):
    print(f"платёж: {payment.process_payment()}")


creditCardPayment = CreditCardPayment(1000)
payPalPayment = PayPalPayment(2000)
cryptoPayment = CryptoPayment(3000)

process_all_payments(creditCardPayment)
process_all_payments(payPalPayment)
process_all_payments(cryptoPayment)

