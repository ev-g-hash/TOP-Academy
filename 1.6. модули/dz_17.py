"""
1) Создайте пакет с несколькими модулями. Например, создайте структуру каталогов:

my_package/
    math_operations.py
    text_utils.py
    date_utils.py
"""
print("пакет с модулями: ")

from my_package import math_operations
print(math_operations.math_operations(1))

from my_package import text_utils
print(text_utils.text_utils(2))

from my_package import date_utils
print(date_utils.date_utils(3))


"""
2) Модуль для преобразования единиц измерения
Создайте модуль unit_converter.py, который будет содержать функции для преобразования различных единиц измерения:
* celsius_to_fahrenheit(celsius) — преобразует градусы Цельсия в Фаренгейты.
* fahrenheit_to_celsius(fahrenheit) — преобразует градусы Фаренгейта в Цельсий.
* meters_to_kilometers(meters) — преобразует метры в километры.
"""
print("\nпреобразование единиц измерения:")

from unit_converter import *

print(celsius_to_fahrengeit(10), "F")
print(fahrengeit_to_celsius(50), "C")
print(meter_to_kilometers(1000), "км")

"""
3) Создайте модуль collection_utils.py, который будет содержать функции для работы с коллекциями:
* unique_elements(lst) — возвращает список уникальных элементов из списка.
* count_occurrences(lst) — возвращает словарь с количеством вхождений каждого элемента в списке.
"""
print("\nсписок уникальных элементов из списка:")
from collection_utils import unique_elements
unique_elements([1,2,1,2,1,3,3,4,4,5,6,6,5])

print("\nсловарь с количеством вхождений каждого элемента в списке:")
from collection_utils import count_occurrences
print(count_occurrences([1,2,3,4,5,"lst_1","lst_2","lst_3"]))

"""
4) Создать модуль рандомных эмоций (с помощью эмоджи)
"""
from collection_utils import z
print(f"\nсмайлик - {z}")