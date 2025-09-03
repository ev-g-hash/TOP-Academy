"""
1
"""

"""
допики
"""

# #-------------------------------------------------преобразование числа в список
n = int(input())
x = str(n)
print(list(map(int, x)))

"""
начало
"""
category = ["drama", "comedy", "mystery", "romance"]

# перебрать список
for i in range(len(category)):
    print(category[i])

for i in category:
    print(i)

'''
2
'''
category.append("action") # добавить в список
print(category)

category1 = ["drama", "comedy"]
category2 = ["mystery", "romance"]

category1.extend(category2) #расширить через функцию
category1.extend([1, 2, 3, 4, "cgbchr"]) #кавычки самое главное списка
print(category1)

category1.insert(0, "книга") #расширить через индекс
category1.insert(3, "книга34") #расширить через индекс
category1.insert(-1, "предмет") #расширить через индекс
print(category1)

"""
3
"""
category1 = ["drama", "comedy"]
category2 = ["mystery", "romance"]

category1.extend(category2)

category1.remove("drama") #удаляет по значению
category1.pop(2) #удаляет по индексу
category1.pop() #удаляет последний элемент по дефолту
category1.clear()#очищает список

print(category1)
"""
4
"""
category = ["drama", "comedy", "romance", "mystery", "romance"]
print(category.index("mystery")) #возвращает индекс элемента
print(category.count("romance")) #счётчик
category.sort() #сорт только принт потом сразу в принте не прокатит
category.sort(reverse=True)
print(category)
prices = [100, 250.45, 1200, 20]
prices.sort()
prices.sort(reverse=True) #список по убыванию
print(prices)
prices.reverse() #переворачивает список
print(prices)
"""
4
"""
customers = ["bob", "anna", "joi", "bob"]
print("bob" in customers) #проверяем на наличие

customers = ["bob", "anna", "joi", "bob"]
if ("bob" in customers):
    print("bob is our customers")
else:
    print("sorry")
"""
5
"""
list1 = [0, 2, 3, 4, 5]
list2 = list1
list3 = [0, 2, 3, 4, 5]
print(list2)
list2[1] = "hello"
print(list2)

print(list2 is list1)
print(list3 is list1)

"""
6
"""
list1 = [0, 2, 3, 4, 5]
print(list1)

list2 = list1.copy()
print(list2)
list2[1] = "hello"
print(list2)
list3 = list(list1)
print(list3)

"""
7
"""
list1 = [0, 2, 3, 4, 5]
list2 = list1.copy()
list1 = list2[:3]
list1[3] = "hello"
print(list2)

"""
8
"""
customers = ["bob", "anna", "joi", "bob"]
for i in range(len(customers)):
    if customers[i] == "bob":
        print(i)

"""
9
"""
myTable = [[111,112,113],[221,222,223]]

print(myTable[1][1])
print(myTable[0])

#через этот цикл хорошо выводить заданные параметры матрицы через рейндж
for i in range(1, 2):
    for j in range(3):
        print(myTable[i][j], end=" ")
    print()
#выводим матрицу
for i in myTable:
    for j in i:
        print(j, end=" ")
    print()

myTable = [[j for j in range(2)] for i in range(3)] #матрица 2 на 3
print(myTable)

stud = [["bob", 1, 2, 3, 4], ["jane", 12, 11, 11, 11], ["jane", 7, 8, 9, 10]]

for i in stud:
    print(i)

for j in stud:
    print(j, max(j[1:]))


films=[['Catch Me If You Can', 'Biography', 'Crime', 'Drama'],
      ['Mrs. Doubtfire', 'Comedy', 'Drama', 'Family']]

userCategory=input("Input film category: ")
for film in films:
    if userCategory in film[1:]:
        print(film[0])
"""
                                                    упражнения
"""
"""
----------------------------------------------------------------------------------------------
Задание 1
В списке целых, заполненном случайными числами вычислить:
negative         - Сумму отрицательных чисел;
even             - Сумму четных чисел;
odd              - Сумму нечетных чисел;
multi_3          - Произведение элементов с индексами кратными 3;
multi_x, multi_y - Произведение элементов между минимальным и максимальным элементом;
el_1, el_2       - Сумму элементов,находящихся между первыми и последним положительными элементами.
 -----------------------------------------------------------------------------------------------
"""
from random import randint

num = []

for i in range(7):
    num.append(randint(-10, 10))

print(f"случайные числа {num}")

negative = 0
even = 0
odd = 0
multi_3 = 1

# #----------------------------------Сумма отрицательных чисел----------------------------------------
for i in num:
    if i < 0:
        negative += i
print(f"сумма отрицательных чисел {negative}")

# #-------------------------------------Сумма четных чисел-------------------------------------------
for i in num:
    if i == 0:
        continue
    if i % 2 == 0:
        even += i
print(f"сумма четных чисел {even}")

# #------------------------------------Сумма нечетных чисел-------------------------------------------
for i in num:
    if i % 2:
        odd += i
print(f"сумма нечетных чисел {odd}")

# #--------------------------Произведение элементов с индексами кратными 3----------------------------
for i in range(len(num)):
    if i == 0:
        continue
    if i % 3 == 0:
        multi_3 *= num[i]
print(f"произведение элементов с индексами кратными 3 = {multi_3}")

# #-------------------Произведение элементов между минимальным и максимальным элементом---------------
print()
print(f"случайные числа {num}")

y = num.index(min(num))
x = num.index(max(num))

multi_x = 1
multi_y = 1
z = []

if x < y:
    for i in num[x + 1:y]:
        z.append(i)
        multi_x *= i
    print(f"числа в диапазоне между {[max(num)]} и {[min(num)]} = {z}")

    if multi_x == 1:
        print("между минимальным и максимальным элементом нет чисел")
    else:
        print(f"произведение этих чисел = {multi_x}")

if y < x:
    for i in num[y + 1:x]:
        z.append(i)
        multi_y *= i
    print(f"числа в диапазоне между {[min(num)]} и {[max(num)]} = {z}")

    if multi_y == 1:
        print("между минимальным и максимальным элементом нет чисел")
    else:
        print(f"произведение этих чисел = {multi_y}")

# #----------Сумма элементов,находящихся между первыми и последним положительными элементами----------
print()
ind = [] #индексы

for index, i in enumerate(num):
    if i > 0:
        ind.append(index)

el_1 = ind[0]
el_2 = ind[-1]
el = 0

for i in num[el_1 + 1:el_2]:
    el += i

print(f"первое положительное число ( {num[el_1]} ), второе последнее положительное число ( {num[el_2]} )")
print(f"сумма чисел между ними = {el}")









