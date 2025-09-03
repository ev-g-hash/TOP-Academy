xxx = int(input("Введите количество элементов для ( сортировка вставками )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")
"""
---------------------------------------------------------------------------------
алгоритм "сортировка вставками" 100 случайных чисел + время при 10 000 2сек при 30 000 21сек
---------------------------------------------------------------------------------
"""
from random import randint

alist_5 = []

for i in range(xxx):
    alist_5.append(randint(0, xxx))

def insertion_sort(alist_5):
    for i in range(1, len(alist_5)):
        temp = alist_5[i]
        j = i - 1
        while(j >= 0 and temp < alist_5[j]):
            alist_5[j + 1] = alist_5[j]
            j = j - 1
        alist_5[j + 1] = temp

import time
start_5 = time.time()
insertion_sort(alist_5)
end_5 = time.time() - start_5

import timeit
insertion_sort(alist_5)
end_6 = timeit.timeit(lambda: insertion_sort(alist_5), number=1)

print(f"""Затрачено времени ( сортировка вставками ): \t  --- {end_5}   сек""")
print(f"""Скорость выполнения ( сортировка вставками ): \t  --- {end_6}   сек""")
yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(alist_5)
else:
    print("расчёт окончен")