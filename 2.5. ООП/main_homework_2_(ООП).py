"""
+ Задание 1: Основы getattr
Напишите функцию get_value(obj, attr_name, default=None), которая:
Принимает объект obj, имя атрибута attr_name и значение по умолчанию default.
Возвращает значение атрибута, если он существует.
Если атрибут не существует, возвращает default.
"""
print("\nЗадание 1: Основы getattr")

class Obj:
    name = "Вася"
    age = 18

my_obj = Obj()


def get_value(obj, attr_name, default=None):
    print(getattr(obj, attr_name, default))

get_value(my_obj, "age", default=None)
get_value(my_obj, "name", default=None)
get_value(my_obj, "city", default=None)


"""
+ Задание 2: Динамическое добавление атрибутов (setattr)
Создайте класс DynamicAttributes, который позволяет добавлять атрибуты динамически.
Напишите метод add_attr(self, name, value), который добавляет атрибут с именем name 
и значением value.
Если атрибут уже существует, он должен быть перезаписан.
"""
print("\nЗадание 2: Динамическое добавление атрибутов (setattr) вариант 1")
# #-----------------------------------1(через цикл)
class DynamicAttributes:
    def __init__(self, my_dict):
        for name, value in my_dict.items():
            setattr(self, name, value)

attr = {'Алиса': 18, 'Вася': 10, 'Вася': 20, 'Вася': 30, 'Алиса': 40}
dynamic_obj = DynamicAttributes(attr)

print(dynamic_obj.__dict__)

##-----------------------------------2(просто добавлением)
print("\nЗадание 2: Динамическое добавление атрибутов (setattr) вариант 2")
class DynamicAttributes:
    pass

    def add_attr(self, name, value):
        setattr(self, name, value)


obj = DynamicAttributes()

obj.add_attr("name", "Alice")
print(obj.name)
obj.add_attr("age", 18)
print(obj.age)
obj.add_attr("name", "Коля")
print(obj.name)
obj.add_attr("age", 22)
print(obj.age)


"""
Задание 3: Проверка атрибутов (hasattr)
Напишите функцию check_attributes(obj, *attrs), которая:
Принимает объект obj и произвольное количество имен атрибутов.
Возвращает True, если все переданные атрибуты существуют у объекта, иначе False.
"""
print("\nЗадание 3: Проверка атрибутов (hasattr)")
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("Evgeny", 46)


def check_attributes(obj, *attrs):

    for attr in attrs:
        if not hasattr(obj, attr):
            return False
    return True


print(check_attributes(obj, "name", "age"))
print(check_attributes(obj, "name", "age", "hobbi"))


"""
Задание 4: Безопасное получение вложенных атрибутов (getattr)
Напишите функцию get_nested_attr(obj, attr_path, default=None), которая:
Принимает объект obj, строку с путем к атрибуту (например, "person.address.city")
и значение по умолчанию.
Возвращает значение вложенного атрибута, если он существует.
Если любого из атрибутов в пути нет, возвращает default.
"""
print("\nЗадание 4: Безопасное получение вложенных атрибутов (getattr)")
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


def get_nested_attr(obj, attr_path, default="Unknown"):
    attrs = attr_path.split(".")
    current_obj = obj

    for attr in attrs:
        try:
            current_obj = getattr(current_obj, attr)
        except AttributeError:
            return default
    return current_obj


person = Person("Evgeny", Address("Tolliatty", "Gorkogo"))

city = get_nested_attr(person, "address.city")
print(city)

country = get_nested_attr(person, "address.country", "Unknown")
print(country)

"""
Задание 5: Удаление атрибутов по условию
Напишите функцию remove_attrs_if(obj, condition), которая:
Принимает объект obj и функцию-условие condition(name, value).
Удаляет все атрибуты объекта, для которых condition(name, value) возвращает True.
Используйте getattr, hasattr и delattr.
"""
print("\nЗадание 5: Удаление атрибутов по условию")
def remove_attrs_if(obj, condition):

    for name in dir(obj):
        if hasattr(obj, name):                      # Проверяем, есть ли атрибут у объекта
            try:
                value = getattr(obj, name)          # Получаем значение атрибута
                if condition(name, value):          # Проверяем условие
                    delattr(obj, name)              # Удаляем атрибут
            except AttributeError:
                pass                                # Если атрибута не существует


# Пример:
class MyObject:
    def __init__(self):
        self.a = 1
        self.b = 'hello'
        self.c = 3.14
        self.d = [1, 2, 3]

obj = MyObject()

# Удаление атрибутов, значения которых являются числами
def delete_numbers(name, value):
    return isinstance(value, (int, float))

remove_attrs_if(obj, delete_numbers)

print(obj.__dict__)  # {'b': 'hello', 'd': [1, 2, 3]}


