xxx = int(input("Введите количество элементов для ( пузырьковой сортировки )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")

from random import randint
arr = []

for i in range(xxx):
    arr.append(randint(0, xxx))

def bublle_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

        if not swapped:
            break

import time
start_1 = time.time()
bublle_sort(arr)
end_1 = time.time() - start_1

import timeit
bublle_sort(arr)
end_2 = timeit.timeit(lambda: bublle_sort(arr), number=1)

print(f"""Затрачено времени ( пузырьковая сортировка ): \t  --- {end_1}   сек""")
print(f"""Скорость выполнения ( пузырьковая сортировка ): \t  --- {end_2}   сек""")

yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(arr)
else:
    print("расчёт окончен")

