"""
ООП модуль

ссылка на занятия по ООП
https://drive.google.com/drive/folders/1cQ68mwKTNa8_eG5x5bTcffjjgDxlPj_M

@classmethod - ссылка на класс
"""

class MyClass:
    name = "Hello"

    @classmethod
    def set_attr(cls, new_name):
        cls.name = new_name

    @classmethod
    def get_attr(cls):
        print(cls.name)

MyClass.get_attr()

MyClass.set_attr("Вася")
print(MyClass.name)

#--------------------------------------
class MyClass:
    name = ""

    @classmethod
    def set_attr(cls, new_name):
        cls.name = new_name

    @classmethod
    def get_attr(cls):
        print(cls.name)

MyClass.get_attr()

MyClass.set_attr("Вася")
print(MyClass.name)

# создали класс и обратились к методу класса
# isinstance - проверка к принадлежности объекта к экземпляру класса

class Point:
    @classmethod
    def creat(cls):
        return cls()

point = Point.creat()

print(isinstance(point, Point))

"""
примерчик
"""
class MyClass:
    @classmethod
    def my_method(cls, x, y):
        cls.x = x
        cls.y = y
        print(cls.x * cls.y)

MyClass.my_method(5, 20)

hop = MyClass()
hop.my_method(100, 5)

"""
пример создали класс и два метода
"""
# --------------------------------------------- вариант 1
class Counter:
    count = 0
    @classmethod
    def add_count(cls, add=1):
        cls.count += add
        print(cls.count)

    @classmethod
    def set_zero(cls):
        cls.count = 0
        print(cls.count)

Counter.add_count(5)
Counter.add_count(6)
Counter.set_zero()

# --------------------------------------------- вариант 2
class Counter:
    count = 0
    @classmethod
    def add_count(cls, add=1):
        cls.count += add
        return cls.count

    @classmethod
    def set_zero(cls):
        cls.count = 0
        return cls.count

print(Counter.add_count(5))
print(Counter.set_zero())
print(Counter.add_count(3))
print(Counter.add_count(4))
print(Counter.add_count(4))

"""
Предыстория:
Вася подарил Машеньке карточку от MagicBank, 
с помощью которой можно делать покупки до 1000. 
Сделав покупку, карточка магическим образом снова пополняется до 1000.

Задание:
Создайте класс MagicBank и объявите внутри класса атрибут money = 1000.
Создайте метод класса add_money(cls). Метод изменяет значение атрибута класса money, 
и делает его равным 1000. Затем выводит на экран текст: Ваш счёт снова равен 1000. 
В print() используйте end='\n\n'.
Создайте метод класса reduce_money(cls, amount). 
С помощью этого метода мы осуществляем проверку, покупку и магическое пополнение. 
Параметр amount - это сумма покупки. Мы не можем осуществить покупку больше чем на 1000 
за один раз, поэтому сделайте в методе вот что:
- Если amount больше 1000, выведите на экран текст: Нельзя тратить больше 1000 за один раз
- Иначе, выведите на экран: Покупка на сумму amount осуществлена. 
Например, "Покупка на сумму 500 осуществлена".
- Теперь нам нужно магически сделать наш счёт равным 1000. 
Для этого, вызываем метод  add_money() в блоке иначе. 
Сделать это можно с помощью cls.add_money().
"""
class MagicBank:
    money = 1000

    @classmethod
    def add_money(cls):
        cls.money = 1000
        print(f"Ваш счёт снова равен {cls.money}", end='\n\n')

    @classmethod
    def reduce_money(cls, amount):
        cls.amount = amount
        if cls.amount > 1000:
            print("Нельзя тратить больше 1000 за один раз")
        else:
            print(f"Покупка на сумму {cls.amount} осуществлена")
            cls.add_money()

MagicBank.reduce_money(400)



"""
Статические методы

функции внутри класса

Используются для функциональности не привязанной к конкретному экземпляру
"""

class MyClass:

    @staticmethod

    def sum_static(a, b):

        return a + b

obj = MyClass()


print(MyClass.sum_static(2, 3))
print(type(MyClass.sum_static))

print(obj.sum_static(2, 3))

"""
Предыстория:
Вася решил закрепить свои знания по статическим методам, 
взяв разного рода задачки по математике. Для этого он взял пример подсчёта 
времени относительно скорости и расстояния.

Задание:
Создайте класс Time
Создайте статический метод с помощью декоратора @staticmethod, 
и назовите его count_time. В параметрах укажите (distance, speed).
Внутри метода лишь одна операция, подсчёт времени по формуле (time = distance / speed). 
Метод возвращает результат time с помощью return
Вызовете метод count_time() через класс, и укажите в аргументах (500, 100). 
Вызывать нужно через print(), так как метод использует return
"""

class Time:

    @staticmethod

    def count_time(distance, speed):
        time = distance / speed
        return time

print(Time.count_time(500, 100))


"""
Предыстория:
Вася создаёт программу для водителей. 
В ней вы указываете расстояние, которое планируете проехать, 
расход топлива на 100км вашей машины, цену на бензин в вашем регионе. 
Программа выводит на экран информацию о будущих финансовых расходах. 
Вася вероломно использует статический метод для подсчёта.

Задание:
Создайте класс Driver
Объявите статический метод calculate_fuel_costs() с параметрами (distance, fuel, price). 
Напоминашка: @staticmethod.
- Создайте переменную result, в ней будет хранится результат подсчётов.
- Готовая формула подсчётов будет в комментариях.
- Выведите на экран округлённое значение result, используя функцию round(). 
Значение округлите до сотых. Постарайтесь сделать округление имено с round(), 
иначе ответы могут не совпасть.
Оставшаяся часть кода уже написана, вам нужно сделать то, что указано в задании.
 

Для тех кто хочет придумать формулу сам:

distance - расстояние в км, которое нужно проехать. Например 3 км.
fuel - расход топлива машины на 100км. Например 7л на 100км.
price - цена бензина за 1 л. Например 50. 
Посчитайте, сколько нужно потратить денег чтобы проехать distance. 
Сохраните результат подсчёта в result. Не забудьте округлить перед выводом на экран.
"""

class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):

        result = round((distance/100 * fuel * price), 2)

        return result
print(Driver.calculate_fuel_costs(500, 7, 50))