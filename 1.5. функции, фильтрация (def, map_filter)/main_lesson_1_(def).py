"""
---------------------------------------------------------------------------------------------------
                                    функции
---------------------------------------------------------------------------------------------------
"""

print("*" * 7)
print("*" * 7)
print("*" * 7)
print("*" * 7)
print("*" * 7)

for _ in range(5):
    print("*" * 7)
print()

for _ in range(5):
    print("*" * 7)
print()

for _ in range(5):
    print("*" * 7)
print()

def drow_box():
    for _ in range(5):
        print("*" * 7)
    print()
drow_box()
drow_box()
drow_box()

# примеры

def print_messange():
    print("Я-Артур")
    print("король британцев")


for i in range(10):
    print_messange()

# матрица разных размеров
def drow_box(height, width):
    for _ in range(height):
        print("*" * width)
    print()
drow_box(10, 23)
drow_box(5, 10)

n = 10
m = 4

drow_box(n, m)


def func(side1, side2):
    area = side1 * side2
    perimetr = (side1 + side2) * 2
    print(area, perimetr)

func(5, 20)

"""
продолжение урока
"""
# -> int то что хотим видеть на выходе
def ccc() -> int:
    a = int(input())
    b = int(input())
    rez = a * b
    return rez

def ccc1(a:int,b:int) -> int:
    rez = a * b
    return rez

def fffff(name:str):
    name = name.capitalize()
    print("Привет", name)

fffff("tdddd")

def ccc(a:int, b:int) -> int:
    rez = a * b
    return rez

print(ccc(14, 10))
print(ccc(a=14, b=10))
print(ccc)

def ppp():
    a = int(input("введите a: "))
    b = int(input("введите b: "))
    print("площадь", a * b)

ppp()

"""
очень интересный вариант рекурсивная функция
"""
def Recursive():
    def Greting(st:str):
        print(st)
        if len(st) == 2:
            return 2
        else:
            Greting(st[:-1])

    Greting("hello")
Recursive()

"""
орёл и решка пример возврата булево значения
"""
def еее() -> bool:
    plaer = input("ввудите").strip().lower()
    return plaer == "орёл"
print(еее())

import random

def qqq() -> bool:
    plaer = input("введите").strip().lower()
    return plaer == "орёл"

def isWin(coin:int, plaer:bool):
    if coin == plaer:
        print("победа")
    else:
        print("проигрыш")
def Main():
    coin = random.randint(0,1)
    plaer = qqq()
    isWin(coin, plaer)
Main()
#-----------------------------------------------------------------
import random

coin = random.randint(0, 1)

def ddd():
    priz = input("введите орёл или решка: ")

    if coin == 0:
        if priz == "решка":
            print("выиграли")
    if coin == 1:
        if priz == "орёл":
            print("выиграли")
    else:
        print("проиграли")
ddd()

