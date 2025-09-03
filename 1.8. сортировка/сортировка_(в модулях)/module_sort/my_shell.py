xxx = int(input("Введите количество элементов для ( метод шелла )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")

"""
-------------------------------------------------------------------------------------
алгоритм "метод шелла" 100 случайных чисел + время 1 000 000 2.38сек
-------------------------------------------------------------------------------------
"""
from random import randint
data = []

for i in range(xxx):
    data.append(randint(0, xxx))

def shell(data):
    inc = len(data)//2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0/11)
    return data

import time
start_3 = time.time()
shell(data)
end_3 = time.time() - start_3

import timeit
shell(data)
end_4 = timeit.timeit(lambda: shell(data), number=1)

print(f"""Затрачено времени ( метод шелла ): \t\t\t\t  --- {end_3}   сек """)
print(f"""Скорость выполнения ( метод шелла ): \t\t\t\t  --- {end_4}   сек """)
yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(data)
else:
    print("расчёт окончен")