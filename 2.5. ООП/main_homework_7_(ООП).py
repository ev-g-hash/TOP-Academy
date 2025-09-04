"""
1) Создайте класс Restricted,
который запрещает доступ к атрибутам, начинающимся с _secret_.
При попытке получить такой атрибут должно вызываться исключение AttributeError.
"""
class Restricted:
    _secret_ = "Vasya"

    def __getattribute__(self, item):
        raise AttributeError("Доступ запрещён")

restricted = Restricted()
print(restricted._secret_)


"""
2) Создайте класс Dynamic, в котором при обращении к атрибуту square_<число>
возвращается квадрат этого числа.
"""
print(f"\n 2) класс Dynamic")
class Dynamic:
    def __init__(self, square):
        self.square = square

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)**2

dynamic = Dynamic(2)
print(dynamic.square)

"""
3) Создайте класс Immutable, который запрещает изменять атрибуты, начинающиеся с _lock_.
При попытке изменить такой атрибут должно вызываться исключение AttributeError.
"""
# class Immutable:
#      def __setattr__(self, _lock_, value):
#             raise AttributeError("Запрещено изменять атрибут")
#
# immutable = Immutable()
# immutable._lock_ = "DSDsDs"

"""
4) Создайте класс Lowercase,
который автоматически переводит имена атрибутов в нижний регистр.
"""
print(f"\n 4) класс Lowercase")
class Lowercase:
    def __setattr__(self, name, value):
        super().__setattr__(name.lower(), value)

    def __getattr__(self, name):
        return super().__getattr__(name.lower())

lowercase = Lowercase()
lowercase.TEST = "lowercase"

print(lowercase.test)

"""
5) Создайте класс Restricted,
который разрешает устанавливать только атрибуты из заранее заданного 
списка allowed_attrs.
"""
print(f"\n 5) класс Restricted")
allowed_attrs = ["test_1", "test_2"]

class Person:
    def __setattr__(self, name, value):
        for i in allowed_attrs:
            if name == i:
                print(f"Создали атрибут {i} со значением {value}")
        super().__setattr__(name, value)

person = Person()

person.test_1 = "Вася"
person.test_2 = "Коля"
person.test_3 = "Марина"