"""
--------------------------------------------циклы----------------------------------------------
"""
# fruits = ["яблоко", "банан", "вишня"]
#
# for elem in fruits:
#     print(f"у меня в кармане {elem}")


# word = "Python"
#
# for elem in word:
#     print(f"у меня в кармане {elem}")
"""
# ------- позволяет получать два значения, и по отдельности grades.items()------
"""
# grades = {"Аня": 90,"Борис": 85,"Света": 80}

# grades.items()

# for key, value in grades.items():
#     print(f"{key} получил {value} баллов")

# for value in grades.items():
#     print(f"получил {value} баллов")
#
# for key in grades:
#     print(f"получил {key} баллов")

# --------------------------------------------------------------возвращение индекса---
# color = ["красный","зелёный","синий"]
#
# for index, color in enumerate(color):
#     print(f"Цвет {index + +1}: {color}")


# -------------------------------------------------------------------брейк и контине---

# for i in range(10):
#     if i == 5:
#         print("Цикл прерван")
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         print(f"Цикл прерван на числе {i}")
#         break
#     print(i)

# numbers = [1, 2, 3, 4, 5]
# target = 3
#
# for i in numbers:
#     if i == target:
#         print(f"число {target} найдено!")
#         break
#     else:
#         print(f"число {target} не надено.")


# for i in range(10):
#     if 3 <= i <= 6:
#         continue
#     print(i)

"""
# вложенные циклы
"""
# print("\n", "\t" * 15, "таблица умножения\n")
# print('^' * 140)
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("|", j, "*", i, "=", j * i, end="|\t")
#     print()
# print('^' * 140)
"""
матрица
"""
# matrix = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
#
# for row in matrix:
#     for elem in row:
#         print(elem, end="|")
#     print()






