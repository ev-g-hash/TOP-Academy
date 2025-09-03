"""
------------------------------------------------------------------------------------------------
                                            работа со строками
------------------------------------------------------------------------------------------------
"""
"""
примеры
"""
myStr = "1234567890"

print(myStr[2:8:2])  #357
print(myStr[8:2:-2]) #975
print(myStr[::-1]) #0987654321
print(myStr[:len(myStr):3]) #1470

"""
экранирование
перенос строки
"""

myStr = " There is no shortage of material to learn Python. \n The following books wight serve"
print(myStr)

"""
табуляция
"""
myStr = f" There is no \t shortage of material to learn Python."
print(myStr)

r"""
\\ - для отображения < \ > (слеша)
\" - для отображения апострофа
"""
myStr = '\'There is no shortage of material to learn Python. The following books wight serve\''
print(myStr)

print("15 \\\\ 2") # на каждое экранирование 1 символ

myStr = "Backslash symbol: \\"
print(myStr)

myStr = " это - '\\t' слэш t, а это '\\n' слэш n"
print(myStr)

"""
#-----------------------------------------------------------------сырая строка
"""
normalStr = "This is a \n normal string"
print(normalStr)

rawStr = r"This is a \n normal string"     #сырая строка
print(rawStr)

normalText = '''Python Arithmetic Operators:\n
    Arithmetic operators are used to perform
    mathematical operations like addition,
    subtraction, multiplication and division.\n
    \tThere are 7 arithmetic operators in Python:
    \t\tAddition +\n
    \t\tSubtraction -\n
    \t\tDivision /\n
    \t\tModulus %\n
    \t\tExponentiation **\n
    \t\tFloor division //\n'''
rawText = r'''Python Arithmetic Operators:\n
    Arithmetic operators are used to perform
    mathematical operations like addition,
    subtraction, multiplication and division.\n
    \tThere are 7 arithmetic operators in Python:
    \t\tAddition +\n
    \t\tSubtraction -\n
    \t\tDivision /\n
    \t\tModulus %\n
    \t\tExponentiation **\n
    \t\tFloor division //\n
  '''
print(normalText)
print(rawText)

"""
недопустимые сырые строки
"""
# errRawStr1 = r'\'
# errRawStr2 = r'123\'
# errRawStr3 = r'abc\\\'

userLogin=input("Your login: ")
print("Welcome,", userLogin, ". Let's start game!")
strMsg="Dear, "+userLogin+". Game over!"
print(strMsg)
print("Welcome,", userLogin,
      ". Let’s start game!", sep="vv")

"""
# strMsg = "Welcome, {}. Let's start game!".format(input("Your login: ")) #отличная идея
# print(strMsg)
# print("Welcome, {}. вам {}!".format(input("как зовут: "),input("сколько лет: "))) #отличная идея

предположительно подойдёт для опросника
"""
strMsg = "My name is {}, I'm {}".format(25,"Student")
print(strMsg) # My name is 25, I'm Student

strMsg1 = "My name is {0}, I'm {1}".format("Student",25)
print(strMsg1) # My name is Student, I'm 25
strMsg2 = "I'm {1}. My name is {0}".format("Student",25)
print(strMsg2) # I'm 25. My name is Student

strMsg3 = "My name is {name}, I'm {age}".format(name="Student", age=25)
print(strMsg3)  # My name is Student, I'm 25
strMsg4 = "My name is {name}, I'm {age}.My name is {name1}, I'm {age1}".format(age=25, name="Student", age1=25, name1="Student")
print(strMsg4)  # My name is Student, I'm 25

strMsg = "Your salary is {0:9.2f}".format(200.846)
print(strMsg)  # Your salary is    200.85

"""
 # :b Двоичный форма
 # :c Преобразует значение в соответствующий символ Юникода
 # :d Десятичный формат
 # :o Восьмеричный формат
 # :x Шестнадцатеричный формат, нижний регистр
"""
userNumber = int(input("Your number? "))  # 255
myStrB = "The binary representation of a number {n} is {n: b}".format(n=userNumber)
print(myStrB)  # The binary representation of a number 255 is 11111111
myStrO = "The octal representation of a number {n} is {n: o}".format(n=userNumber)
print(myStrO)  # The octal representation of a number 255 is 377
myStrH = "The Hex representation of a number {n} is {n: x}".format(n=userNumber)
print(myStrH)  # The Hex representation of a number 255 is ff

"""
# #  :-Отображает знак минус только для отрицательных значений
# #  :+ Отображает знак плюс только для положительных значений
# #  : символ  пробела Вставляет дополнительный пробел перед положительными числами
# # (и знак минус перед отрицательными числами)
"""

myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
print(myStr1) #The number1 range from -10 to 10

myStr2="The number2 range from {0:+} to {1:+}".format(-20,50)
print(myStr2) #The number2 range from -20 to +50

myStr3="The number3 range from {0: } to {1:}".format(-30,30)
print(myStr3) #The number3 range from -30 to  30

"""
#  # :< Выравнивает по левому краю (в пределах доступного пространства)
#  # :> Выравнивает по правому краю (в пределах доступного пространства)
#  # :^ Выравнивает по центру (в пределах доступного пространства)
# # установим доступное пространство для значения
"""

myStr1 = "You have {:<10} points."
print(myStr1.format(12))  # You have 12         points.
myStr2 = "You have {:>10} points."
print(myStr2.format(12))  # You have         12 points.
myStr3 = "You have {:^10} points."
print(myStr3.format(12))  # You have     12     points.
#-------с числами
myStr1 = "Number is {:<10.2f}!"
print(myStr1.format(34.8256)) #Number is 34.83     !
myStr2 = "Number is {:>10.2f}!"
print(myStr2.format(34.8256)) #Number is      34.83!
myStr3 = "Number is {:^10.2f}!"
print(myStr3.format(34.8256)) #Number is   34.83   !
#-------со строками
myStr1 = "Your login is {:<20}!"
print(myStr1.format("Admin")) #Your login is Admin  !
myStr2 = "Your password is {:>20}!"
print(myStr2.format("12345")) #Your password is  12345!
myStr3 = "Your secret word is {:^15}!"
print(myStr3.format("IT")) #Your secret word is   IT   !

"""
---------------------------------------------------------------------------------------------
                                            Модуль string
---------------------------------------------------------------------------------------------
"""
import string
import random

userLogin = "".join(random.sample((string.ascii_lowercase),6))
userPass  = "".join(random.sample((string.ascii_letters + string.digits), 8))
print("login:",userLogin)
print("password:",userPass)

import string
myStr = "  We have BEEN happy\n to welcome\n\n back OLD friends, \n\n\nand to make new ones  "
#We Have Been Happy To Welcome Back Old Friends, And To Make New Ones
print(string.capwords(myStr))

from string import Formatter
formatter = Formatter()
print(formatter.format('{userLog}',
                        userLog = 'Admin')) #Admin
print(formatter.format('{} {userLog}', 'Welcome, ',
      userLog = 'Admin')) #Welcome, Admin
print('{} {userLog}'.format('Welcome, ',
      userLog = 'Admin')) #Welcome,  Admin

"""
----------------------------------------------------------------------------------------------------
задача
- есть список
- есть зарезирвированные слова
- найти в списке зарезирвированные слова и изменить регистр на верхний
(при методе реплейс есть побочка в ввиде: если зарезервированное слово
например (опт) мы находим в списке и меняем на верхний регистр, то в слове ( оптовик )
 он тоже поменяет. пример ниже
"""
let = "я ищу опт и меняю его на верх регистр а оптовик нет".split()
zsl = "ищу".split()

for i in let:
    let = str(let)
    for j in zsl:
        if i == j:
            let = let.replace(i, j.upper())

for j in let:
    if j.isalpha() or j.isspace():
        print(j, end="")
"""
такую задачу решаем замену элемета через индекс пример ниже (тоже побочка второе не находит)
я ищу опт и меняю его на верх регистр а оптовик нет, е не е, а я нет
------------------------------------------------------------------------------------------------------
"""
let = "я ищу опт и меняю его на верх регистр а оптовик нет".split()
zsl = "я".split()

ind = []

for i in let:
    for j in zsl:
        if j == i:
            y = let.index(i)
            ind.append(y)

for a in ind:
    let[int(a)] = let[int(a)].upper()

print(" ".join(let))

"""
вот оно идеальное решение для такой задачи можно посмотреть
------------------------------------------------------------------------------------------------------
"""
lst = "я ищу опт и меняю его на верх регистр а я оптовик и я не опт, а да я и опт и оптовик".split()
sl = "я и а опт верх".split()
vr = []

for index, i in enumerate(lst):
    for j in sl:
        if i == j:
            vr.append(index)
print(vr)

for j in vr:
    lst[int(j)] = lst[int(j)].upper()

print(" ".join(lst))
"""
-------------------------------------------------------------------------------------------------
Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
+Посчитайте сколько раз цифры встречаются в тексте;
+ Посчитайте сколько раз знаки препинания встречаются в тексте;
+ Посчитайте количество восклицательных знаков в тексте.
-------------------------------------------------------------------------------------------------
"""
txt = input("""изменить, текст1!. таким - образом2. чтобы каждое, предложение3. начиналось с большой буквы4!!!: \n""").capitalize() + "  "
zn = ["!", ".", ",", "?", ":", ";", "-"]
count = 0
count1 = 0
count2 = 0

for i in txt:
    if i == "!":
        count += 1
    if i.isdigit():
        count1 += 1
    for z in zn:
        if z == i:
            count2 += 1

print(f"восклицательных знаков = {count}")
print(f"количество цифр = {count1}")
print(f"количество знаков препинания = {count2}")

lst = (list(txt))
vr = []

for index, i in enumerate(lst):
    if i == ".":
        vr.append(index + 2)
    if i == "!":
        vr.append(index + 2)
    if i == "?":
        vr.append(index + 2)

for j in vr:
    lst[int(j)] = lst[int(j)].upper()

print("".join(lst))
