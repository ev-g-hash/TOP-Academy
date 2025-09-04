"""
1- что такое ООП (Объектно ориентированное программирование)
2- основные понятия ООП (наследование, полиморфирзм, инкапсуляция, абстракция)
3- что такое класс(простое представление типа объекта чертёж/план/шаблон описыающие детали объекта)
4- что такое объект(экземпляр класса своё собственное состояние и идентичность)
5- что такое инкапсуляция(сокрытие данных/ атрибут объекта который содержит скрытые данные
которые могут быть доступны членам этого класса)
6- что такое полиморфизм(разное поведение - например животное кошка, собака, собака гавкает
кошка мяукает/ присвоение поведения в подклассе)
7- что такое наследование(от слова наследие, наследование данных/ концепция в которой один
класс разделяет структуру и поведение разделённую в другом классе)
8- объясните термин конструктор(создавать атрибуты в классе/ это метод используемый для
инициализации состояния объекта, который вызывается во время создания объекта)
9- что такое метод(метод - это функция в классе/ это описание набора инструкций которую
моно назвать функцией)
10- что такое модификатор доступа и какие есть(это ключевые слова
которые помогают установить доступность классов методов и атрибутов _protected)
11- что такое статик класс(это метод класса он привязан к классу)
12- что такое лямбда функция(это функция которая использует две переменные
безымянная функция анонимная которая может включать только одно выражение)
13- что такое модуль(подключаемый функционал с помощью которого мы
можем проводить определенные вычисления/файл который содержит переменые
функции классы которые можно использовать в других программах или модулях
"""
"""
-----------------------------------------------------------------------------------
                                        Категории методов
__getattribute__
------------------------------------------------------------------------------------
"""

class User:
    name1 = "Vasya"
    name2 = "Maha"

    def __getattribute__(self, item):
        return f"Привет {object.__getattribute__(self, item)}"

user = User()
print(user.name1)
print(user.name2)

# контроль доступа к атрибутам объекта

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __getattribute__(self, item):
        if item == "password":
            raise AttributeError("Доступ запрещён")
        return object.__getattribute__(self, item)

user = User("Vasya", "password")
print(user.username)
print(user.password)

#--------------------------------------------------

class User:
    def __init__(self, number):
        self.number = number

    def __getattribute__(self, item):
        return 10 + object.__getattribute__(self, item)

user1 = User(20)
print(user1.number)

class User:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __getattribute__(self, item):
        return 10 + object.__getattribute__(self, item)

user1 = User(20, 30)
user2 = User(100, 200)
print(user1.number1, user1.number2)
print(user2.number1, user2.number2)

class User:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return object.__getattribute__(self, item) + "man"

_super = User("Super")
_bat = User("Bat")
_spader = User("Spader")

print(_super.name)
print(_bat.name)
print(_spader.name)


"""
__getattr__

предоставяет возможность определить поведение при обращении к несуществующим
атрибутам объекта.

def __getattr__(self, name):
    код определяющий при обращении к несуществующему атрибуту
"""

class Person:
    def __getattr__(self, name):
        return f"Атрибут {name} не найден"

person = Person()
print(person.age)

class Person:
    def __getattr__(self, name):
        if name == "age":
            return 30
        else:
            return f"Атрибут {name} не найден"

person = Person()
print(person.age)
print(person.dfdsfsd)

class Person:
    def __init__(self):
        self.attributes = {"name": "Илья", "age": 34}

    def __getattr__(self, item):
        if item in self.attributes:
            return self.attributes[item]

        else:
            return f"Атрибут {item} не найден"

person = Person()
print(person.name)
print(person.age)
print(person.dfdsfsd)


class Person:
    def __init__(self):
        self.attributes = ["name","age"]

    def __getattr__(self, item):
        if item in self.attributes:
            return self.attributes[item]

        else:
            return f"Атрибут {item} не найден"


person = Person()
print(person.attributes)
print(person.attr)

"""
Если атрибута "name" не существует, мы его создадим. 
Все остальные не существующие атрибуты будут возвращать текст.

Задание:

Создайте класс Person и объявите метод __getattr__.
В методе __getattr__ создайте условие проверки. Если имя атрибута равно 'name', 
создайте атрибут name со значением Vasya и верните его значение с помощью return. 
Иначе верните текст "Такого атрибута нет", с помощью return.
Создайте экземпляр person
Выведите на экран значение атрибута name через экземпляр person.
"""

class Person:
    name = "Vasya"

    def __getattr__(self, item):
        if item == "name":
            return item
        else:
            return "Такого атрибута нет"

person = Person()
print(person.name)
print(person.age)


"""
__setattr__ 

вызывается при установке значения атрибута экземпляра и позволяет определить
поведение при установке значения атрибута экземпляра

def __setattr__(self, name, value):
    object.__setattr__(self, name, value)

#или

def __setattr__(self, name, value):
    super().__setattr__(name, value)
"""

class Person:
    def __setattr__(self, name, value):
        if name == "name":
            print(f"Создали атрибут name со значением {value}")
        super().__setattr__(name, value)

person = Person()

person.name = "Vasya"
person.name = "Masha"


#---------------------------------------
class Person:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError(f"Возраст не может быть отрицательным")
        else:
            super().__setattr__(name, value)

person = Person()

person.age = 25
person.age = -5

class Immu:
    def __setattr__(self, name, value):
        raise AttributeError("Нельзя создавать объект")

immu = Immu()
immu.name = "DSDsDs"
















