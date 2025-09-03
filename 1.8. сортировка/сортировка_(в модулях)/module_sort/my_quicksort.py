xxx = int(input("Введите количество элементов для ( быстрой сортировки )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")
"""
--------------------------------------------------------------------------------
алгоритм "Быстрая сортировка" 100 случайных чисел + время на 80 000 падает на 70 000 1.3 сек
--------------------------------------------------------------------------------
"""
from random import randint
alist = []

for i in range(xxx):
    alist.append(randint(0, xxx))

def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)

def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
import time
start = time.time()
quicksort(alist, 0, len(alist))
end = time.time() - start

import timeit
quicksort(alist, 0, len(alist))
end_1 = timeit.timeit(lambda: quicksort(alist, 0, len(alist)), number=1)

print(f"""Затрачено времени ( быстрая сортировка ): \t\t  --- {end}   сек""")
print(f"""Скорость выполнения ( быстрая сортировка ): \t\t  --- {end_1}   сек""")

yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(alist)
else:
    print("расчёт окончен")
