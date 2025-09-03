"""
---------------------------------------------------------------------------------------------------
Два списка целых заполняются случайными числами.
Необходимо:
----------                                                                          ---------------
"""
# num_general_1 - Сформировать третий список, содержащий элементы обоих списков;
# num_general_2 - Сформировать третий список, содержащий элементы обоих списков без повторений;
# num_general_3 - Сформировать третий список, содержащий элементы общие для двух списков;
# num_general_4 - Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# num_general_5 - Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

from random import randint

num1 = []
num2 = []

for i in range(7):
    num1.append(randint(-10, 10))
for i in range(7):
    num2.append(randint(-10, 10))


num_general_1 = []
num_general_2 = []
num_general_3 = []
num_general_4 = []
num_general_5 = [[min(num1), max(num1)], [min(num2), max(num2)]]

print(f"первый список случайных чисел {num1}")
print(f"второй список случайных чисел {num2}")

# num_general_1
for i in num1:
    num_general_1.append(i)
for j in num2:
    num_general_1.append(j)
print(f"- num_general_1, содержащий элементы обоих списков {num_general_1}")

# num_general_2
for i in num1:
    if i not in num_general_2:
        num_general_2.append(i)
    for j in num2:
        if j not in num_general_2:
            num_general_2.append(j)
print(f"- num_general_2, содержащий элементы обоих списков без повторений {num_general_2}")

# num_general_3
num_general_3_1 = []

for i in num1:
    for j in num2:
        if j == i:
            num_general_3_1.append(j)

for z in num_general_3_1:
    if z not in num_general_3:
        num_general_3.append(z)
print(f"- num_general_3, содержащий элементы общие для двух списков {num_general_3}")

# num_general_4
num_general_4_1 = []

for i in num1:
    if i not in num_general_4_1:
        num_general_4_1.append(i)
num_general_4.append(num_general_4_1)

num_general_4_2 = []

for j in num2:
    if j not in num_general_4_2:
        num_general_4_2.append(j)
num_general_4.append(num_general_4_2)

print(f"- num_general_4,содержащий только уникальные элементы каждого из списков {num_general_4}")

# num_general_5
print(f"- num_general_5, содержащий только минимальное и максимальное значение каждого из списков {num_general_5}")
