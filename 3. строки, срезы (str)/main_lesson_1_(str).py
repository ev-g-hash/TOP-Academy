"""
кодировки
"""
ord()           # принимает строку
chr(67)

print(chr(104)+chr(101)+chr(108)+chr(108)+chr(48)+chr(32)+chr(119)+chr(48)+chr(114)+chr(108)+chr(100)+chr(33)+chr(9829))
print(ord('!'))

userMessage = 'Können Sie mir bitte helfen?'
userMessageEnc=userMessage.encode('utf-8')
print(userMessageEnc)
userMessageDec=userMessageEnc.decode('utf-8')
print(userMessageDec)


"""
-----------------------------------------------------------------------------------------------
                                            строки
-----------------------------------------------------------------------------------------------
"""
myStr="hello"
print(id(myStr))
print(type(myStr))
print(myStr)
myStr="ello"
print(myStr)
print(id(myStr))
print(type(myStr))

myStr="""hello world"""
print(myStr)
print(id(myStr))
print(type(myStr))

#------------------------------------------------------доступ по индексу
myStr="""world"""
print(myStr[0])
print(myStr[1])
print(len(myStr)-0)

#-------------------------------------------------------Конкатенация (объединение) строк
str1 = "Hello,"
str2 = "Admin"
print(str1 + str2)
str3 = str1 + str2
print(str3)

#------------------------------------------------------------------------умножение строк
myStr="Hello"
print(myStr*5)
myBigStr=myStr*5
print(myBigStr)

# Особенности работы со строками Методы для изменения регистра строки

myStr="Привет Евгений, как твои дела_всё хорошо?"
print(myStr.capitalize()) # Привет евгений, как твои дела. всё хорошо?
print(myStr.lower())    # привет евгений, как твои дела. всё хорошо?
print(myStr.upper())    # ПРИВЕТ ЕВГЕНИЙ, КАК ТВОИ ДЕЛА. ВСЁ ХОРОШО?
print(myStr.title())    # Привет Евгений, Как Твои Дела. Всё Хорошо?
print(myStr.swapcase()) # пРИВЕТ еВГЕНИЙ, КАК ТВОИ ДЕЛА. вСЁ ХОРОШО?

# --------------------------------------------------------- Методы поиска подстроки в строке
myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
print(myStr.count('Python', 20)) #2
print(myStr.count('Python',20,65)) #
print(myStr.find('a'))  #8
print(myStr.find('a',0, 100))  #-1
print(myStr.index('a'))      #8
# print(myStr.index('a',2,5))  #ValueError
print(myStr.rfind('a'))  #48
print(myStr.rfind('a',2,20))  #14
print(myStr.rindex('a'))  #48
# print(myStr.rindex('a',2,6))  #ValueError - substring not found
print(myStr.startswith('P'))  #True
print(myStr.startswith('p'))  #False
print(myStr.startswith('w',7))  #True
print(myStr.endswith('!'))  #True
print(myStr.endswith('n',2,6))  #True

#-----------------------------------------------------------------------Методы проверки строк

myStr = "Python2021"
print(myStr.isalnum())  # True есть ли буквы и цифры, если символ то False
print(myStr.isalpha())  # False только буквы

myAge = "16"
print(myAge.isdigit())  # True только цифры

myStr1 = "it was created in the late 1980's"
print(myStr1.islower())  # True все маленькие буквы (нижний регистр)

myStr2 = " \t  \n \t\t"
print(myStr2.isspace())  # True пробелы

myName1 = "Вuido Пan Пossum"
print(myName1.istitle())  # False если с заглавной буквы

myName2 = "GUIDO VAN ROSSUM"
print(myName2.isupper())  # True все большие

#------------------------------------------------------------Методы форматирования строк
myStr="Python 2021"
print(myStr.center(30)) #центрирует в этом диапазоне

print(myStr.center(30,'*'))#заполняет этот диапазон
print(myStr.center(5))

# табуляция
myStr="Python2021\t Python- cool!"
print(myStr)
print(myStr.expandtabs(tabsize=9))
print(myStr.expandtabs())

myStr="Python- cool!"
print(myStr.ljust(20))
print(myStr.ljust(30,'@'))
print(myStr.ljust(5))

myStr = "          Python- cool!     "
print(myStr.lstrip())
print(myStr.rstrip())
print(myStr.strip())
myStr = "@;          Python- cool!     @"
print(myStr.lstrip('@;'))
print(myStr.rstrip('@'))
print(myStr.strip('@'))
myStr="123"
print(myStr.zfill(5))
myStr="+123"
print(myStr.zfill(5))
"""
-------------------------------------------------------------------------------------------------
                                                срезы
-------------------------------------------------------------------------------------------------
"""

myStr="Python-cool!"
print(myStr[1:3]) #yt
print(myStr[-5:-2]) #coo
print(myStr[-5:11]) #cool
print(myStr[:6]) #Python
print(myStr[:-1]) #Python-cool
print(myStr[6:]) #-cool!
print(myStr[-5:]) #cool!

myStr = "1234567890"
print(myStr[2:8:2])  # 357
print(myStr[8:2:-2])  # 975
print(myStr[::-1])  # 0987654321
print(myStr[5::2])  # 680
print(myStr[-1::-2])  # 08642
print(myStr[:len(myStr):3])  # 1470











