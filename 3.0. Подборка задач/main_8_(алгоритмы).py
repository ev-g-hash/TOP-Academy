"""
1. Линейный поиск
Задача:
Напишите функцию linear_search(array, target),
которая принимает список чисел и целевое число.
Функция должна возвращать индекс целевого числа, если оно найдено, и -1, если нет.
"""
# def linear_search(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1
#
# print(linear_search([1,2,3,4,5,6,7,8,9,10], 10))

"""
2. Бинарный поиск
Задача: 
Напишите функцию binary_search(sorted_array, target),
которая принимает отсортированный список и целевое число.
Функция должна возвращать индекс целевого числа или -1, если оно не найдено.
"""
# def binary_search(sorted_array, target):
#     first = 0
#     last = len(sorted_array) - 1
#     index = - 1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if sorted_array[mid] == target:
#             index = mid
#         else:
#             if target < sorted_array[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
#
# print(binary_search([1,2,3,4,5,6,7,8,9,10], 11))