xxx = int(input("Введите количество элементов для ( пирамидальная сортировка )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")
"""
------------------------------------------------------------------------------------
алгоритм "пирамидальная сортировка" 100 случайных чисел + время 1 000 000 5сек
-----------------------------------------------------------------------------------
"""
from random import randint
arr_2 = []

for i in range(xxx):
    arr_2.append(randint(0, xxx))

def heapify(arr_2, n, i):
    largest = i
    left = 2 * i + 1
    right =  2 * i + 2

    if left < n and arr_2[left] > arr_2[largest]:
        largest = left
    if right < n and arr_2[right] > arr_2[largest]:
        largest = right
    if largest != i:
        arr_2[i], arr_2[largest] = arr_2[largest], arr_2[i]
        heapify(arr_2, n, largest)

def heap_sort(arr_2):
    n = len(arr_2)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr_2, n, i)

    for i in range(n-1, 0,-1):
        arr_2[i], arr_2[0] = arr_2[0], arr_2[i]
        heapify(arr_2, i, 0)

import time
start_2 = time.time()
heap_sort(arr_2)
end_2 = time.time() - start_2

import timeit
heap_sort(arr_2)
end_3 = timeit.timeit(lambda: heap_sort(arr_2), number=1)

print(f"""Затрачено времени ( пирамидальная сортировка ):   --- {end_2}   сек""")
print(f"""Скорость выполнения ( пирамидальная сортировка ):   --- {end_3}   сек""")

yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(arr_2)
else:
    print("расчёт окончен")




