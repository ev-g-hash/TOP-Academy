xxx = int(input("Введите количество элементов для ( сортировка слияние )(например (1000)): "))
print(f"\nПри длине списка равной {xxx} элементов: ")
"""
---------------------------------------------------------------------------------
алгоритм "сортировка слияние" 100 случайных чисел + время 1 000 000 2.9сек
---------------------------------------------------------------------------------
"""
from random import randint
arr_6 = []

for i in range(xxx):
    arr_6.append(randint(0, xxx))

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

import time
start_6 = time.time()
random_list_of_nums = arr_6
random_list_of_nums = merge_sort(random_list_of_nums)
end_6 = time.time() - start_6

import timeit
merge_sort(random_list_of_nums)
end_7 = timeit.timeit(lambda: merge_sort(random_list_of_nums), number=1)

print(f"""Затрачено времени ( сортировка слияние ): \t\t  --- {end_6}   сек""")
print(f"""Скорость выполнения( сортировка слияние ): \t\t  --- {end_7}   сек""")
yyy = input("""
Желаете вывести отсортированный список элементов (напишите "да" или "нет"): """)
if yyy == "да".lower():
    print(random_list_of_nums)
else:
    print("расчёт окончен")
