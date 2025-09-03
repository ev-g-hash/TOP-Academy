"""
-----------------------------------------------------------------------------------------------------------
                                        Сортировка
----------------------------------------------------------------------------------------------------------
"""
#____________________________________________________________________________________сортировка вставками
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while(j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

alist = input("введите числа: ").split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print("отсортированные числа ", end=" ")
print(alist)

#___________________________________________________________слияние НЕ РАБОТАЕТ
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

alist = input("введите числа: ").split()
alist = [int(x) for x in alist]
merge_list(alist,0, len(alist)//2, len(alist))
print(alist)

#___________________________________________________________метод шелла
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

data = [3,54,2,1,9,10,90,4]
shell(data)

print(data)

#___________________________________________________________пирамидальная сортировка
def heapify(arr, n, i):
    largest = i    #самый большой элемент
    left = 2 * i + 1 #левый элемент
    right =  2 * i + 2 #правый элемент

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)                         #построение кучи(перегруппировка массива)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)              #один за другим извлекаем элемент из кучи

    for i in range(n-1, 0,-1):
        arr[i], arr[0] = arr[0], arr[i]  #перемещаем текущий корень в конец
        heapify(arr, i, 0)              #вызываем heapify на уменьшение кучи

arr = [1, 2, 4, 2, 78, 3, 90]
heap_sort(arr)
print(arr)

#___________________________________________________________быстрая сортировка
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

alist = [1, 2, 4, 2, 78, 3, 90]
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print("сортированный список: ")
print(alist)

#___________________________________________________________пузырьковая сортировка
def bublle_sort(arr):
    n = len(arr) # проходим по всем элементам
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

        if not swapped:
            break

arr = [1, 2, 4, 2, 78, 3, 90]
bublle_sort(arr)
print(arr)
"""
----------------------------------------------------------------------------
алгоритм "пузырьковая сортировка" 100 случайных чисел + время 
----------------------------------------------------------------------------
"""
from random import randint
arr = []

for i in range(100):
    arr.append(randint(0, 100))

def bublle_sort(arr):
    n = len(arr) # проходим по всем элементам
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

        if not swapped:
            break

import timeit
bublle_sort(arr)
execution_time = timeit.timeit(lambda: bublle_sort(arr), number=1)

import time
start_2 = time.time()
bublle_sort(arr)
end_2 = time.time() - start_2

print(f"""время исполнения: \t  --- {end_2}   сек""")
print("скорость:", execution_time)