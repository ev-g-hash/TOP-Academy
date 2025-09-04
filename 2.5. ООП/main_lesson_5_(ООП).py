"""
-----------------------------------------------------------------------------------------
                                ООП наследование и super
-----------------------------------------------------------------------------------------
"""
"""
super - временный объект, который позволяет обращаться к методам и атрибутам
родительского класса.
super().метод() 
super().атрибут
"""
#--------------------------------------------------метод
class Cat:
    def hello_cat(self):
        self.name = "hello cat"

class Dog(Cat):
    def hello_dog(self):
        super().hello_cat()

test = Dog()
test.hello_dog()
print(test.name)
#---------------------------------------------------атрибут
class Cat:
    name = "cat"

class Dog(Cat):
    def print_name(self):
        print(super().name)

test = Dog()
test.print_name()
#-----------------------------------------------__init__
class Cat:
    def __init__(self):
        self.cat = "котик"

class Test(Cat):
    def __init__(self):
        super().__init__()
        self.dog = "пёсик"

test = Test()
print(test.cat)
print(test.dog)

"""
super - позволяет обращаться к методам и атрибутам родительского класса
super - имеет необязательные атрибуты
super - позволяет обращаться к объектам родительского класса без явного
использования его имени.
"""
"""
Создайте два класса Minecraft и Roblox. Класс Roblox - будет дочерним классом Minecraft.
В классе Minecraft создайте метод hello_creeper, 
который будет выводить на экран фразу - "Hello, Creeper!".
В классе Roblox создайте метод hello_all, 
который будет вызывать метод hello_сreeper. 
Метод hello_all также будет выводить на экран фразу "Hello, Pozzy!" с помощью print.
Создайте экземпляр hello класса Roblox.
Вызовите метод hello_all, через экземпляр hello. Функцию print не нужно использовать.
"""

class Minecraft:
    def hello_creeper(self):
        print("Hello, Creeper!")

class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creeper()
        print("Hello, Pozzy!")

hello = Roblox()
hello.hello_all()

"""
примерчики
"""

class Alfa:
    def sum_number(self, x, y):
        self.x = x
        self.y = y
        print(self.x + self.y)

class Beta(Alfa):
    def result(self, x, y, z):
        super().sum_number(x, y)
        self.z = z
        print(self.z)

test = Beta()
test.result(10, 20, 50)


"""
Создайте два класса Alfa и Beta (дочерний)
В классе Alfa создайте статический метод sum_number используя декоратор @staticmethod. 
Метод sum_number имеет два параметра (x, y). 
Помните, что в статических методах не используется self. 
Сам метод возвращает сумму параметров
x, y, используя return
В дочернем классе Beta создайте обычный метод result, 
который имеет 4 параметра (self, x, y, z). Метод:
записывает в переменную summa, результат вызова метода sum_number, 
используя параметры x, y.
То есть summa = результат вызова sum_number.
выводит на экран результат деления переменной summa на параметр z, с помощью print. 
   	4. Создайте экземпляр test класса Beta
   	5. Вызовите метод result через экземпляр test, используя аргументы 10, 20, 30. 
   	Функцию print() использовать не нужно
"""
class Alfa:
    @staticmethod
    def sum_number(x, y):
        return x + y

class Beta(Alfa):
    def result(self, x, y, z):
        summa = super().sum_number(x, y)
        self.z = z
        print(summa / z)

test = Beta()
test.result(10, 20, 30)

"""
примерчик
"""
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Student(Person):
    def __init__(self, name, age, height, weight, class_number, hobby):
        super().__init__(name, age, height, weight)
        self.class_number = class_number
        self.hobby = hobby

class Worker(Person):
    def __init__(self, name, age, height, weight, work, experience):
        super().__init__(name, age, height, weight)
        self.work = work
        self.experience = experience


id1 = Student("Tanya", 6, 100, 25, 1, "cook")
id2 = Worker("Vasya", 28, 180, 70, "driver", 6)


print(id1.__dict__)
print(id2.__dict__)

"""
примерчик
"""

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()               # можно так - super(Child, self).greet()
        print("Hello from Child")

c = Child()
c.greet()


"""
множественное наследование
"""

class A:
    def metod1(self):
        print("Metod1 from A")

class B:
    def metod2(self):
        print("Metod1 from B")

class C(A, B):
    def metod3(self):
        print("Metod3 from C")

child = C()

child.metod1()
child.metod2()
child.metod3()

"""
Задание:
Создайте три класса King, Queen, Prince. Класс Prince наследуется от (King, Queen).
В классе King создайте атрибут "a" равный 4.
В классе Queen создайте атрибут "b" равный 6. 
В классе Prince создайте атрибут "c" равный 10.
Создайте экземпляр count от класса Prince.
Выведите на экран результат сложения атрибутов "a" и "b" и "c", 
через экземпляр count (т.е. count.a + ...)
"""

class King:
    a = 4

class Queen:
    b = 6

class Prince(King, Queen):
    c = 10

count = Prince()
print(count.a + count.b + count.c)

"""
порядок множественного наследования
пример
"""


class A:
    def __init__(self):
        print("metod A")

class B:
    def __init__(self):
        print("metod B")

class C(A,B):
    pass

c = C()

print(c)

#--------------------------------------
class A:
    def __init__(self):
        print("metod A")

class B:
    def __init__(self):
        print("metod B")

class C(A,B):
    def __init__(self):
        print("metod C")

c = C()

print(c)

"""
Атрибут __mro__ (порядок в котором Пайтон ищет методы в иерархии класса
при наследовании

C3 Linearization для определения  mro
"""

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


print(D.__mro__)

# по иерархии снизу вверх

"""
MRO особенно полезен при множественном наследовании, 
когда у класса есть несколько родительских классов. 
Он помогает избежать проблем с дублированием методов и позволяет определить, 
какой метод будет вызван в случае конфликта имен методов в разных классах.
"""





