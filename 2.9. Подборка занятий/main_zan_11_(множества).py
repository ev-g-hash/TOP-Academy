"""
-----------------------------------------------------------------------------------
                                         Множество
-----------------------------------------------------------------------------------
"""

"""
# #множество - это коллекция из уникальных элементов
# #создание (set)
"""
# my_set = {1, 2, 3, 4, 5}
#
# print(type(my_set))
# print(my_set)

"""
# #другой способ создания (set)
"""
# my_set = set()
# for i in range(5):
#     my_set.add(i)
# print(type(my_set))
# print(my_set)

"""
# #удаление элемента
"""
# my_set = {1, 2, 3, 4, 5}
# my_set.remove(2)
# print(my_set)

"""
##(set) включает уникальные элементы, если добавить
## элемент который уже существует он не добавит
"""
# my_set = {1, 2, 3, 4, 5}
# my_set.add(2)
#print(my_set)

"""
# #тоже самое при объединении одинаковые элементы не добавляет
"""
# my_set1 = {1, 2, 3, 4}
# my_set2 = {3, 4, 5, 6}
# print(my_set1)
# print(my_set2)
# my_set = my_set1.union(my_set2)
# print(my_set)

"""
# #пересечение (возвращает одинаковые элементы)
"""
# print(my_set1.intersection(my_set2))

"""
# #метод возвращает элементы которых нет в другом сэте)
"""
# print(my_set1.difference(my_set2))

"""
# # сэты будут равны если они влючают одни и теже значения не важно в каком порядке
"""
# print({1, 2, 3} == {3, 2, 1})

"""
# # удаление дубликатов из множества
"""
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
# not_duble_num = set(numbers)
# print(type(not_duble_num))
# print(not_duble_num)

"""
# #либо удалить и сразу преобразовать в лист
"""
# not_duble_num2 = list(set(numbers))
# print(type(not_duble_num2))
# print(not_duble_num2)

"""
вес и скорость выполнения по сравнению с другими (вес больше всех, преимущество в скорости
обработки)
"""
# #--------------------------------------------------------вес
# x = (1,2,3,4,5,6,7,8,9,10)
# y = [1,2,3,4,5,6,7,8,9,10]
# u = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
# h = {1,2,3,4,5,6,7,8,9,10}
#
# print(x.__sizeof__())
# print(y.__sizeof__())
# print(u.__sizeof__())
# print(h.__sizeof__())
#
# #-------------------------------------------------------------скорость
# import time
# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#     return list_new
#
# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))
#
# start = time.time()
# f(z,x,c,)
# stop = time.time() - start
# print(stop)
#
# start2 = time.time()
# r = set(z)
# t = r.union(set(x), set(c))
# stop2 = time.time() - start2
# print(stop2)

"""
методы
"""
# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}
#
# print(z)
# print(x)
#
# z.add(7)  #добавить
# print(z)
#
# z.remove(7) #удалить
# print(z)
#
# z.discard(7) #удалить если элемента нет ошибки не будет
# print(z)
#
# y = z.union(x) #соединить два множества
# print(y)
#
# x.update(z) #обновить (в один добавить другой)
# print(x)


# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}
#
# t = z.intersection(x) #пересечение общие элементы
# print(t)
#
# e = z.difference(x) #разница между множеством
# print(e)
#
# a = x.difference(z) #разница между множеством
# print(a)

"""
пример на работе с текстом (текста по факту нет только код)
"""
# ---------------------------добавление уникальных элементов с двух файлов
# new = set()
#
# r = open("text1.txt")
# new.update(set(r.read().split()))
# r.close()
#
# r = open("text2.txt")
# new.update(set(r.read().split()))
# r.close()
#
# print(new)

# --------------------------------сравнение и разница уникальных элементов

# r = open("text1.txt")
# r1 = set(r.read().split())
# r.close()
#
# r = open("text2.txt")
# r2 = set(r.read().split())
# r.close()
#
# new = r1.intersection(r2)
# new1 = r1.difference(r2)
#
# print(new)
# print(new1)
