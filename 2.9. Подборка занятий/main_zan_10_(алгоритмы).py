"""
------------------------------------------------------------------------------
начало
------------------------------------------------------------------------------
"""
# lst = ["orange", "apple", "grade"]
# print("apple" in lst)
#
# s = ["pythonist"]
# print("t" in s)
#
# s = ["pythonist"]
# print("q" in s)

"""
--------------------------------------------------------------------------------
линейный поиск
--------------------------------------------------------------------------------
"""
# def LinearSearch(lys, elem):
#     for i in lys:
#         if i == elem:
#             return i
#     return -1
# print(LinearSearch([1,2,3,4,5,2,1], 2))
#
# def LinearSearch(lys, elem):
#     for i in range(len(lys)):
#         if lys[i] == elem:
#             return i
#     return -1
# print(LinearSearch([1,2,3,4,5,2,1], 2))

"""
-----------------------------------------------------------------------------------
бинарный поиск
-----------------------------------------------------------------------------------
"""
# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = - 1
#     while (first <= last) and (index == - 1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
#
# print(BinarySearch([1,2,3,4,5,6,7], 9))

"""
-----------------------------------------------------------------------------------
бинарный без функции
-----------------------------------------------------------------------------------
"""
# val = 10
# lys = [1,2,3,4,5,6,7,8]
# first = 0
# last = len(lys) - 1
# index = - 1
# while (first <= last) and (index == -1):
#     mid = (first + last) // 2
#     if lys[mid] == val:
#         index = mid
#     else:
#         if val < lys[mid]:
#                 last = mid - 1
#         else:
#             first = mid + 1
# print(index)

"""
-----------------------------------------------------------------------------------
алгоритм извлечение корня
-----------------------------------------------------------------------------------
"""
# import math
# def JumpSearch(lys, val):
#     lenght = len(lys)
#     jump = int(math.sqrt(lenght))
#     left, right = 0, 0
#     while left < lenght and lys[left] <= val:
#         right = min(lenght - 1, left + jump)
#         if lys[left] <= val and lys[right] >= val:
#             break
#         left += jump
#     if left >= lenght or lys[left] > val:
#         return -1
#     right = min(lenght - 1, right)
#     i = left
#     while i <= right and lys[i] <= val:
#         if lys[i] == val:
#             return i
#         i += 1
#     return -1
#
# print(JumpSearch([1,2,3,4,5,6,7,8,9,10], 6))

"""
---------------------------------------------------------------------------------
алгоритм Фибоначчи
--------------------------------------------------------------------------------
"""
# def Fib(lys, val):
#     fibM_minus_2 = 0
#     fibM_minus_1 = 1
#     fibM = fibM_minus_1 + fibM_minus_2
#     while (fibM < len(lys)):
#         fibM_minus_2 = fibM_minus_1
#         fibM_minus_1 = fibM
#         fibM = fibM_minus_1 + fibM_minus_2
#     index = -1
#     while(fibM > 1):
#         i = min(index + fibM_minus_2, (len(lys)-1))
#         if (lys[i] < val):
#             fibM = fibM_minus_1
#             fibM_minus_1 = fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#             index = i
#         elif (lys[i] > val):
#             fibM = fibM_minus_2
#             fibM_minus_1 = fibM_minus_1 - fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#         else:
#             return i
#     if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1]==val):
#         return index+1
#     return -1
#
# print(Fib([1,2,3,4,5,6,7,8,9,10], 11))

