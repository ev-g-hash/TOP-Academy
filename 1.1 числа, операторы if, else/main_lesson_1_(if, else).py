# булево значения if, else
x = 5

if x == 5:
    print(f"x равно: {x}")
else:
    print(f"x не равно 5")

#--------------------------------------------
x = 7
print(x == 5)
print(x < 5)
print(x > 5)
print(x >= 5)
print(x <= 5)
print(x != 5)

#--------------------------------------------
num1 = 3
num2 = 7

if num1 < num2:
    print("меньше")
else:
    print("больше")

#--------------------------------------------
x = 5

if x > 2:
    if x < 10:
        print("x больше 2, но меньше 10")

#--------------------------------------------
# логические операторы and(и), or(или) not(нет)
age = 12

user_class = 7

if age >= 12 and user_class == 7:
    print("условие верно")

#--------------------------------------------
age = 1

user_class = 7

if age >= 12 or user_class == 7:
    print("условие верно")

#--------------------------------------------
age = 12
if not age == 12:
    print("возраст не равен 12")

#--------------------------------------------

#(можно самим задавать приоритет посредством скобок)
# (при использовании if - else имеет увязку к последнему if в блоке)

t = float(input("введите температуру тела: "))

if t == 36.6:
    print("ваша температура оптимальна и равна 36.6")
elif t > 36.6 and t < 37:
    print("ваша температура больше 36.6, но меньше 37")
elif t < 36.6 and t > 35:
    print("ваша температура меньше 36.6, но больше 35")
else:
    print("Вам очень плохо либо проверьте градусник")

#--------------------------------------------
# (при использовании if - else имеет увязку к последнему if в блоке,
# при других неравных значениях if else не сработает),
# для того чтобы if(ы) отработали надо под каждым поставить else
x = 5
if x != 5:
    print("Yes")
# else:
#     print("No")
if x == 5:
    print("Yes")
# else:
#     print("No")
if x != 10:
    print("Yes")
else:
    print("No")
# можно записать короче
if x >= 5 and x == 5 and x != 10:
    print("Yes")
else:
    print("No")
#--------------------------------------------
# проверка возраста(необязательное else)
# age = int(input("введите свой возраст: "))

if age >= 14 and age < 18:
    print("вам больше или 14 лет")
elif age >= 18 and age < 21:
    print("вам больше или 18 лет")
elif age >= 21 and age <= 45:
    print("вам больше или 21 год")
elif age > 45:
    print("вам больше 45 лет")
#--------------------------------------------
num = int(input("введите число: "))
print("четное" if num % 2 == 0 else "нечётное")
#--------------------------------------------
# # свич кейсы
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

#--------------------------------------------
x = int(input("введите число: "))

if x > 100:
    print("+")
elif x < 100:
    print("-")
else:
    print("100")

#--------------------------------------------
x = int(input("введите число: "))
y = int(input("введите число: "))
z = int(input("введите число: "))

if x > 10 and y > 10 and z > 10:
    print("yes")
else:
    print("no")

#--------------------------------------------
x = int(input("введите число c 1 до 12: "))
if x == 1 or x == 2 or x == 12:
    print("зима")
elif x >= 3 and x <= 5:
    print("весна")
elif x >= 6 and x <= 8:
    print("лето")
elif x >= 9 and x <= 11:
    print("осень")
else:
    print("не является временем года")



