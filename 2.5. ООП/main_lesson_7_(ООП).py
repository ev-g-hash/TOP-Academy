"""
Инкапсуляция

один из принципов ООП который позволяет ограничить доступ к атрибутам или
методам класса.
исключает случайное изменение

1 - сокрытие данных от прямого доступа
2 - методы доступа (геттеры и сеттеры) - позволяют обращатья к приватным атрибутам.
3 - декораторы @property позволяет определить геттеры и сеттеры для атрибутов класса.

Public - публичные самые обычные методы и атртбуты.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def print_data(self):
        print(f"{self.name}")

id1 = Person("Vasya")
id1.print_data()
print(id1.name)

"""
Protected
"""

class Person:
    def __init__(self, name):
        self._name = name

    def print_data(self):
        print(f"{self._name}")

id1 = Person("Vasya")
id1.print_data()
print(id1._name)        # Так не принято

#----------защищенный метод
class Person:
    def _vasya_cat(self):
        print("Васин кот")

    def print_protected_method(self):
        self._vasya_cat()

id1 = Person()
id1.print_protected_method()

"""
Private
- атрибуты и методы доступны только внутри класса (два подчёркивания) полная инкапсуляция.


"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(1500)

print(account.get_balance())
# print(account.__balance)            #напрямую не получится

"""
Private методы то же самое напрямую вызывать нельзя
"""

class Person:
    def __vasya(self):
        print("Васин кот")

    def print_private(self):
        self.__vasya()

id1 = Person()
id1.print_private()


"""
Private и __dict__
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(1500)
print(account.__dict__)
print(account._BankAccount__balance)

"""
задачки

Создайте класс Bank
Объявите три метода: _init_, print_balance, change_balance
Метод _init_ имеет три параметра:  имя клиента, номер карты и баланс, 
и создаёт три приватных атрибута. Имена параметрам и атрибутам придумайте сами.
Метод print_balance является обычным методом, 
и выводит на экран баланс клиента с помощью print().
Метод change_balance имеет параметр (self, money), и изменяет баланс клиента. 
Если money отрицательное, то баланс уменьшается, если money положительное, 
то баланс увеличивается. Метод только изменяет атрибут связанный с балансом.
Часть кода уже написана, вам нужно лишь сделать то, что написано выше.
"""

class Bank:
    def __init__(self, name, card, balance):
        self.__name = name
        self.__card = card
        self.__balance = balance

    def prin_balance(self):
        print(self.__balance)

    def change_balance(self, money):
            self.__balance += money
            print(self.__balance)

id1 = Bank("Vasya", 1234, 1500)

id1.prin_balance()
id1.change_balance(100)
id1.change_balance(-200)

"""
примерчик защищенного Protected
"""

class Parent:
    _x = 10
    def parent_x(self):
        print(self._x)

class Child(Parent):
    def child_x(self):
        print(self._x)

coordinate = Child()
coordinate.parent_x()
coordinate.child_x()

"""
Private
"""
class Parent:
    __x = 10
    def parent_x(self):
        print(self.__x)

class Child(Parent):
    def child_x(self):
        # print(self.__x)              #будет ошибка
        return self.parent_x()


coordinate = Child()
coordinate.parent_x()
coordinate.child_x()

"""
Модуль accessify
Декоратор @protected
"""

from accessify import protected

class Myclass:
    @protected
    def _protected(self):
        print("Это защита")

    def public(self):
        self._protected()

obj = Myclass()
obj.public()
obj._protected()

"""
@private
"""
from accessify import private

class MyClass:
    a = 2
    b = 3

    @private
    def private_sum_ab(self):
        print(f"{self.a + self.b}")

    def public_sum_ab(self):
        self.private_sum_ab()

obj = MyClass()
obj.public_sum_ab()
obj.private_sum_ab()

"""
Предыстория:
Машенька обиделась на Васю, и сказала, что с ним не будет разговаривать какое-то время. 
Но Васе нужно узнать у Машеньки, куда она положила активатор телепорта. 
Поэтому Вася сообразил, и решил узнать информацию через Маму, чтобы Мама спросила у Машеньки, а потом рассказала Васе.

Задание:
Импортируйте модуль accessify (from accessify import private)
Создайте класс Teleport
Создайте приватный метод __activator_teleport(), используя декоратор @private. 
Метод выводит на экран информацию:
"Активатор от телепорта у Машеньки под подушкой".
Создайте публичный метод mama_help(). Метод вызывает приватный метод  __activator_teleport().
К сожалению, на Stepik нет модуля accessify. 
Поэтому задание выполните у себя на компьютере, например в PyCharm. 
Часть кода уже написана, сюда вставьте ваш код из PyCharm, 
но без импорта модуля и без декоратора. Либо закомментируйте импорт и декоратор. 
Не забывайте про self и скобки при вызове методов.
"""
from accessify import private

class Teleport:
    @private
    def activator_teleport(self):
        print("Активатор от телепорта у Машеньки под подушкой")

    def mama_help(self):
        self.activator_teleport()

obj = Teleport()
obj.mama_help()