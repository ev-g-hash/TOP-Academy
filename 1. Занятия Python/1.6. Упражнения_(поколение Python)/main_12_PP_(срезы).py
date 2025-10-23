"""
Срезы
"""


# s = 'abcdefg'
# print(s[::-3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

"""
Палиндром
На вход программе подаётся одно слово, записанное в нижнем регистре. 
Напишите программу, которая определяет, является ли оно палиндромом.
"""
# word = input()
# _word = word[::-1]
#
# print("YES" if word == _word else "NO")


#---------------------------------
# word = input()
# print(('NO', 'YES')[word == word[::-1]])

"""
Делаем срезы 1
На вход программе подаётся одна строка. Напишите программу, которая выводит:

общее количество символов в строке;
исходную строку, повторённую 3 раза;
первый символ строки;
первые три символа строки;
последние три символа строки;
строку в обратном порядке;
строку с удалённым первым и последним символами.

Sample Input 1:
abcdefghijklmnopqrstuvwxyz

Sample Output 1:
26
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
a
abc
xyz
zyxwvutsrqponmlkjihgfedcba
bcdefghijklmnopqrstuvwxy
"""
# _str = input()
#
# print(len(_str))
# print(_str * 3)
# print(_str[0])
# print(_str[:3])
# print(_str[-3:])
# print(_str[::-1])
# print(_str[1:-1])

"""
Делаем срезы 2
На вход программе подаётся одна строка. Напишите программу, которая выводит:

третий символ этой строки;
предпоследний символ этой строки;
первые пять символов этой строки;
всю строку, кроме последних двух символов;
все символы с чётными индексами;
все символы с нечётными индексами;
все символы в обратном порядке;
все символы строки через один в обратном порядке, начиная с последнего.

Sample Input:
abcdefghijklmnopqrstuvwxyz

Sample Output:
c
y
abcde
abcdefghijklmnopqrstuvwx
acegikmoqsuwy
bdfhjlnprtvxz
zyxwvutsrqponmlkjihgfedcba
zxvtrpnljhfdb
"""
# _str = input()
#
# print(_str[2])
# print(_str[-2])
# print(_str[:5])
# print(_str[:-2])
# print(_str[::2])
# print(_str[1::2])
# print(_str[::-1])
# print(_str[-1::-2])

"""
Две половинки
На вход программе подаётся строка текста. 
Напишите программу, которая разрежет её на две равные части, 
переставит их местами и выведет на экран.

Формат входных данных
На вход программе подаётся строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если длина строки нечётная, 
то длина первой части должна быть на один символ больше.
"""

# _str = input()
# x = len(_str) // 2
#
# if len(_str) % 2 == 0:
#     print(_str[x:] + _str[:x])
# else:
#     print(_str[x + 1:] + _str[:x + 1])


