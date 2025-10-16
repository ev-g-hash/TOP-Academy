"""
                                            ТИПЫ
"""
# a = None
# print(f"a =",a, type(a))
# a = 1
# print(f"a =",a, type(a))
# a = 1.0
# print(f"a =",a, type(a))
# a = 1 + 1j
# print(f"a =",a, type(a))
# a = "1abc"
# print(f"a =",a, type(a))
# a = [1, 1, "a"]
# print(f"a =",a, type(a))
# a = (1, 1, "a")
# print(f"a =",a, type(a))
# a = {1, 1, "a"}
# print(f"a =",a, type(a))
# a = {"a":"d", "b":1}
# print(f"a =",a, type(a))
# a = True
# print(f"a =",a, type(a))

# print("list - списки, tuple - кортежи, dict - словари, set - множество")

"""
------------------------------------------------------------------------------------------
                                            числа
------------------------------------------------------------------------------------------
"""
#------------------------------------------------------------------------------переменные
# x = 10
# y = 5
# x1 = 10.0
# y1 = 5.0
# x2 = 11
# y2 = 5

#----------------------------------------------------------операторы арифметичесих действий
# z2 = x2 / y2
# t2 = x2 * y2
# s2 = x2 ** y2
# c2 = x2 // y2
# o2 = x2 % y2
# summ = x + y
# summ1 = x1 + y1
# print(summ)
# print(summ1)
# print(z2)
# print(t2)
# print(s2)
# print(c2) целочисленное деление т.е.на сколько раз разделилось число без остатка
# print(o2) остаток от деления

#--------------------------------------------------------------------------большое число
#big_intenger = 10 ** 1000 #отобразит столько, сколько поместится в оперативную память
#print(big_intenger)

#--------------------------------------------------------целое число и с плавающей точкой
#--------------------------------------------------------int и float
# my_int = 1
# my_float = float(my_int)
# print(my_float)

# my_float1 = 1.9
# my_int1 = int(my_float1)
# print(my_int1)

#----------------------------------------------------int отбрасывает значения после запятой

#----------------------------------------------------округление "round"

# my_float3 = 1.9
# print(round(my_float3))


#-------------------------преобразования числа в строку с разбивкой и переменой их местами

# x = int(input("число: "))
# y = list(str(x))
# y[0], y[1] = y[1], y[0]
# print(y)

"""
преобразование строки чисел в список или кортеж чисел
"""
# values = input('Введите числа через запятую: ')
#
# ints_as_strings = values.split(',')
#
# ints = map(int, ints_as_strings)
#
# lst = list(ints)
# tup = tuple(lst)
#
# print('Список:', lst)
# print('Кортеж:', tup)

"""
-------------------------------------------------------------------------------------------
                                булево значение операторы сравнения
-------------------------------------------------------------------------------------------
"""
# == равно, != не равно, > больше, < меньше, >= больше либо равно, <= меньше либо равно

# x_b = 10
# y_b = 10
# print(x_b == y_b)

# x_b1 = 10
# y_b1 = 10
# is_equal = x_b1 == y_b1
# print(is_equal)

# x_b2 = 10
# y_b2 = 9
# not_equal = x_b2 != y_b2
# print(not_equal)

# x_b3 = 10
# y_b3 = 10
# print(x_b3 > y_b3)
# print(x_b3 < y_b3)
# print(x_b3 >= y_b3)
# print(x_b3 <= y_b3)

# x_b4 = 12
# print(x_b4 < 11 and x_b4 > 0)
#--------------------and - и, or - или (если число попадает в диапазон то тру если нет фолс)
# is_student = True
# print(not is_student)
#--------------------------------------------оператор not возвращает обратное - вернёт фолс

#-----------------булево значение возвращает тру всё что не ноль, фолс если ноль (это числа)
#------------------в строке тру если что то написано, если строка пустая фолс
# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool("hello, world"))
# print(bool(""))

#------------------------------------------------------------операторы сравнения примеры
# if True:
#     print("hello, world")
# if False:
#     print("hello, world") #------------------------не выведет ничего пример работы фолс

# x_o1 = 10
# if x_o1 > 9:
#     print("x_o1 is positive")

# x_o1 = 10
# if x_o1 > 9:
#     print("x_o1 is positive")

# x_o2 = 0
# if x_o2 > 0:
#     print("x_o2 is positive")
# elif x_o2 < 0:
#     print("x_o2 is negative")
# else:
#     print("x_o2 is zero or undefined")

#--------------срaвниваем два значения в качестве примера использован оператор or(или) можно
#--------------заменить на and(и) если надо что бы и то и это вернёт тру или фолс
# x_o3 = -10
# y_o3 = 20
# if x_o3 > 0 or y_o3 > 0:
#     print("x_o3 and y_o3 y are positive")

#-----------------------------проверяем пустая не пустая строка аналогично можно с числом
# messange = "fff"
# if messange:
#     print("ggg не пустая строка")
# else:
#     print("ggg пустая строка")

#------------------------------------------------------------дополнения операторы сравнения
# # пример работы иф и элиф, различия заключаются это очерёдность при выполнении кода
# # если в блоке стоит несолько (иф) то прога прочитает их все
# # если в блоке стоит (иф) и (элиф) прога не будет читать элиф если тру есть в (иф)
# # если несколько (иф) и (элиф) то будет прочитан код (иф(ы)) если (иф(ы)) тру то (элифы)
# # не будут выполнены если (иф(ы)) фолс то в блоке (ифа(ов)) будут выполнены (элиф(ы))
# if False:
#     print('if')
# elif True:
#     print('elif')
# if True:
#     print('if2')
# elif True:
#     print('elif2')

#------------------------если х = 0, то тогда 6/1, если другое число то 6/ на переменную х
#------------------------исключаем ноль, чтобы программа не падала
# x = 0
# if x == 0:
#     x = 1
# print(6/x)

#-------------------исключаем символы, буквы и ноль тоже (способ не работает от пользователя
# x = 0
# if x == 0:
#     x = 1
#     print("x равен нулю")

# elif type(x) == type(5) or type(x) == type(5.0):
#     print("x корректен")
#     print(100/x)
# else:
#     print("x недопустимое значение")

# #исключаем символы, буквы и ноль
# x = input("введите число: ")
# if x.isdigit():
#     y = int(x)
#     if y == 0:
#         y = 1
#         print("вы ввели ноль")
#     else:
#         print(f"вы ввели число {x}, тогда 100/{x} =", 100 / y)
# else:
#     print(f"""пожалуйста введите число, введеное вами значение "{x}"
# не является числом""")

"""
---------------------------------------------------------------------------------------
                                            строки
---------------------------------------------------------------------------------------
"""
#--------------------------------------------------заглавная буква в предожении---------
# name = "ada lovelace i love"
# print(name.capitalize())

#--------------------------------------------------заглавные буквы---------------------
# name = "ada lovelace i love"
# print(name.title())

#--------------------------------------------------приветствие-------------------------
# my_string1 = "hello world"
# print(my_string1)

#--------------------------------------------------использование тройных кавычек------
# my_string2 = """
# hello world hello world
# """
# print(my_string2)

#---------------------------------------------------сложение строк--------------------
# first_name = "alice"
# last_name = "smith"
# full_name = first_name + " " + last_name
# print(full_name)

#---------------------------------------------------использование (f) и ( {} ) в строке
# full_name1 = f"моё имя: {first_name}, моя фамилия: {last_name}"
# print(full_name1)

#----------------------------------------------------длина строки-----------------------
# length = len(full_name)
# length1 = len(full_name1)
# print(length)
# print(length1)

#----------------------------------------------------перевод числа в строку--------------
# my_integer = 100
# my_string3 = str(my_integer)
# print(my_string3)
# print(type(my_string3))

#----------------------------------------------------перевод строки в число--------------
# my_int = int("100")
# print(my_int)
# print(type(my_int))

#--------------------------------------------------перевод строки от пользователя в число
# my_string4 = input("введите число: ")
# print(type(my_string4))
# my_string5 = int(input("введите число: "))
# print(type(my_string5))

#-----------------------------------------------------узнать сколько цифр в большом числе
# big_integer = 2 ** 100
# print(len(str(big_integer)))

#---оператор (in) входит ли слово, буква в строку возвращает тру или фолс (регистрозависимый)
# my_string = "hello world"
# print(("а" in my_string))

#------------------------------------------------------------------верхний и нижний регистр
# my_string7 = "alice"
# print(my_string7.upper())
# my_string8 = "AAAAAAA"
# print(my_string8.lower())

#-----------------------------------------------------------убирает пробел в начале и конце
# my_string9 = "    alice           "
# print(len(my_string9))
# my_string9 = "    alice           "
# print(len(my_string9.strip()))


#------------------------------------------------------------замена символов, слов букв

# my_string10 = "hello world"
# print(my_string10.replace("world", "python"))


#--------------------------------------------------------определение количества символов
# my_string11 = "hello world"
# print(my_string11.count("l"))

#------------------------------------------определить наличия числа в строке тру или фолс
#------------------------------------------использовать в if для определения числа ↓ ----
# my_string = "10"
# print(my_string.isdigit())

#------------------------------------------определение типа вот он пример ↑ -----------
# integer = input("введите число: ")
# if integer.isdigit():
#     integer = int(integer)
# print(type(integer))

#--------------------------------------------примеры занятия---------------------------
# name1 = "Евгений"
# age1 = 45
# print(f"меня зовут {name1} и мне {45} лет")

# x10 = 10
# y10 = 10
# print(f"сумма {x10 + y10}, произведение {x10 * y10} и т.д.")

#----------------------------------------------------------------цикл работы со строкой
#----------все данные будет выдавать до 5 раз букву (о) будет пропускать и не считать цикл
# x = ""
#
# while len(x) < 5:
#     y = input("ввод данных: ")
#     if y == "o":
#         continue
#     x += y
#
#     print(x)

#-----------------перебирает letters и в str_1 = '' возвращает символы с нижним регистром

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# str_1 = ''
# for i in letters:
#     if i == i.lower():
#         str_1 += i
#
# print(str_1)

"""
преобразование строки чисел в список или кортеж чисел
"""
# values = input('Введите числа через запятую: ')
#
# ints_as_strings = values.split(',')
#
# ints = map(int, ints_as_strings)
#
# lst = list(ints)
# tup = tuple(lst)
#
# print('Список:', lst)
# print('Кортеж:', tup)
"""
------------------------------------------------------------------------------------------------
                                            работа со строками
------------------------------------------------------------------------------------------------
"""
"""
примеры
"""
# myStr = "1234567890"
#
# print(myStr[2:8:2])  #357
# print(myStr[8:2:-2]) #975
# print(myStr[::-1]) #0987654321
# print(myStr[:len(myStr):3]) #1470

"""
экранирование
перенос строки
"""
#
# myStr = " There is no shortage of material to learn Python. \n The following books wight serve"
# print(myStr)

"""
табуляция, апостроф
"""
# myStr = f" There is no \t shortage of material to learn Python."
# print(myStr)


# \\ - для отображения < \ > (слеша)
# \ - для отображения апострофа

# myStr = '\'There is no shortage of material to learn Python. The following books wight serve\''
# print(myStr)

# print("15 \\\\ 2") # на каждое экранирование 1 символ

# myStr = "Backslash symbol: \\"
# print(myStr)

# myStr = " это - '\\t' слэш t, а это '\\n' слэш n"
# print(myStr)

"""
#-----------------------------------------------------------------сырая строка
"""
# normalStr = "This is a \n normal string"
# print(normalStr)
#
# rawStr = r"This is a \n normal string"     #сырая строка
# print(rawStr)

# normalText = '''Python Arithmetic Operators:\n
#     Arithmetic operators are used to perform
#     mathematical operations like addition,
#     subtraction, multiplication and division.\n
#     \tThere are 7 arithmetic operators in Python:
#     \t\tAddition +\n
#     \t\tSubtraction -\n
#     \t\tDivision /\n
#     \t\tModulus %\n
#     \t\tExponentiation **\n
#     \t\tFloor division //\n'''
# rawText = r'''Python Arithmetic Operators:\n
#     Arithmetic operators are used to perform
#     mathematical operations like addition,
#     subtraction, multiplication and division.\n
#     \tThere are 7 arithmetic operators in Python:
#     \t\tAddition +\n
#     \t\tSubtraction -\n
#     \t\tDivision /\n
#     \t\tModulus %\n
#     \t\tExponentiation **\n
#     \t\tFloor division //\n
#   '''
# print(normalText)
# print(rawText)

"""
недопустимые сырые строки
"""
# errRawStr1 = r'\'
# errRawStr2 = r'123\'
# errRawStr3 = r'abc\\\'

# userLogin=input("Your login: ")
# print("Welcome,", userLogin, ". Let's start game!")
# strMsg="Dear, "+userLogin+". Game over!"
# print(strMsg)
# print("Welcome,", userLogin,
#       ". Let’s start game!", sep="vv")

"""
# strMsg = "Welcome, {}. Let's start game!".format(input("Your login: ")) #отличная идея
# print(strMsg)
# print("Welcome, {}. вам {}!".format(input("как зовут: "),input("сколько лет: "))) #отличная идея

предположительно подойдёт для опросника
"""
# strMsg = "My name is {}, I'm {}".format(25,"Student")
# print(strMsg) # My name is 25, I'm Student

# strMsg1 = "My name is {0}, I'm {1}".format("Student",25)
# print(strMsg1) # My name is Student, I'm 25
# strMsg2 = "I'm {1}. My name is {0}".format("Student",25)
# print(strMsg2) # I'm 25. My name is Student

# strMsg3 = "My name is {name}, I'm {age}".format(name="Student", age=25)
# print(strMsg3)  # My name is Student, I'm 25
# strMsg4 = "My name is {name}, I'm {age}.My name is {name1}, I'm {age1}".format(age=25, name="Student", age1=25, name1="Student")
# print(strMsg4)  # My name is Student, I'm 25

# strMsg = "Your salary is {0:9.2f}".format(200.846)
# print(strMsg)  # Your salary is    200.85

"""
 # :b Двоичный форма
 # :c Преобразует значение в соответствующий символ Юникода
 # :d Десятичный формат
 # :o Восьмеричный формат
 # :x Шестнадцатеричный формат, нижний регистр
"""
# userNumber = int(input("Your number? "))  # 255
# myStrB = "The binary representation of a number {n} is {n: b}".format(n=userNumber)
# print(myStrB)  # The binary representation of a number 255 is 11111111
# myStrO = "The octal representation of a number {n} is {n: o}".format(n=userNumber)
# print(myStrO)  # The octal representation of a number 255 is 377
# myStrH = "The Hex representation of a number {n} is {n: x}".format(n=userNumber)
# print(myStrH)  # The Hex representation of a number 255 is ff

"""
# #  :-Отображает знак минус только для отрицательных значений
# #  :+ Отображает знак плюс только для положительных значений
# #  : символ  пробела Вставляет дополнительный пробел перед положительными числами
# # (и знак минус перед отрицательными числами)
"""

# myStr1="The number1 range from {0:-} to {1:-}".format(-10,10)
# print(myStr1) #The number1 range from -10 to 10
#
# myStr2="The number2 range from {0:+} to {1:+}".format(-20,50)
# print(myStr2) #The number2 range from -20 to +50
#
# myStr3="The number3 range from {0: } to {1:}".format(-30,30)
# print(myStr3) #The number3 range from -30 to  30

"""
#  # :< Выравнивает по левому краю (в пределах доступного пространства)
#  # :> Выравнивает по правому краю (в пределах доступного пространства)
#  # :^ Выравнивает по центру (в пределах доступного пространства)
# # установим доступное пространство для значения
"""

# myStr1 = "You have {:<10} points."
# print(myStr1.format(12))  # You have 12         points.
# myStr2 = "You have {:>10} points."
# print(myStr2.format(12))  # You have         12 points.
# myStr3 = "You have {:^10} points."
# print(myStr3.format(12))  # You have     12     points.
#-------с числами
# myStr1 = "Number is {:<10.2f}!"
# print(myStr1.format(34.8256)) #Number is 34.83     !
# myStr2 = "Number is {:>10.2f}!"
# print(myStr2.format(34.8256)) #Number is      34.83!
# myStr3 = "Number is {:^10.2f}!"
# print(myStr3.format(34.8256)) #Number is   34.83   !
#-------со строками
# myStr1 = "Your login is {:<20}!"
# print(myStr1.format("Admin")) #Your login is Admin  !
# myStr2 = "Your password is {:>20}!"
# print(myStr2.format("12345")) #Your password is  12345!
# myStr3 = "Your secret word is {:^15}!"
# print(myStr3.format("IT")) #Your secret word is   IT   !

"""
---------------------------------------------------------------------------------------------
                                            Модуль string
---------------------------------------------------------------------------------------------
"""
import string
import random

# userLogin = "".join(random.sample((string.ascii_lowercase),6))
# userPass  = "".join(random.sample((string.ascii_letters + string.digits), 8))
# print("login:",userLogin)
# print("password:",userPass)
#
# import string
# myStr = "  We have BEEN happy\n to welcome\n\n back OLD friends, \n\n\nand to make new ones  "
# #We Have Been Happy To Welcome Back Old Friends, And To Make New Ones
# print(string.capwords(myStr))
#
# from string import Formatter
# formatter = Formatter()
# print(formatter.format('{userLog}',
#                         userLog = 'Admin')) #Admin
# print(formatter.format('{} {userLog}', 'Welcome, ',
#       userLog = 'Admin')) #Welcome, Admin
# print('{} {userLog}'.format('Welcome, ',
#       userLog = 'Admin')) #Welcome,  Admin

"""
-------------------------------------------------------------------------------------------------
задачка
-------------------------------------------------------------------------------------------------
"""
"""
Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
+Посчитайте сколько раз цифры встречаются в тексте;
+ Посчитайте сколько раз знаки препинания встречаются в тексте;
+ Посчитайте количество восклицательных знаков в тексте.
"""
# txt = input("""изменить, текст1!. таким - образом2. чтобы каждое, предложение3. начиналось с большой буквы4!!! : \n""").capitalize() + "  "
#
# count = 0
# count1 = 0
# count2 = 0
#
# for i in txt:
#     if i == "!":
#         count += 1
#     if i.isdigit():
#         count1 += 1
#     if i == "!" or i == "." or i == "," or i == "?" or i == ":" or i == ";" or i == "-":
#         count2 += 1
# print(f"восклицательных знаков = {count}")
# print(f"количество цифр = {count1}")
# print(f"количество знаков препинания = {count2}")
#
# lst = (list(txt))
# vr = []
#
# for index, i in enumerate(lst):
#     if i == ".":
#         vr.append(index + 2)
#     if i == "!":
#         vr.append(index + 2)
#     if i == "?":
#         vr.append(index + 2)
#
# for j in vr:
#     lst[int(j)] = lst[int(j)].upper()
#
# print("".join(lst))






