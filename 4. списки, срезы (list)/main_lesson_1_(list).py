"""
string работа со строками
"""

# from string import Formatter#
# formatter = Formatter()#
# print(formatter.format('{uzerLog}', userLog='Admim'))

# from string import Template
# t = Template("какой-то текст $userRights, $userName, $appName")
# resStr = t.substitute(userName="Admin", userRights = "edit", appName="superApp")
# print(resStr)

"""
регулярные выражения
"""
r"""
------------------------------------------------------------------------------------------------------------------
Шаблон      Назначение
------      -----------
\d          Соответствует одной десятичной цифре
\D          Соответствует одному любому символу, кроме десятичной цифры
\s          Соответствует одному (любому) пробельному символу
\S          Соответствует одному (любому) символу, который не относится к пробельным
\w          Соответствует любому буквенноцифровому символу или символу нижнего подчеркивания («_»)
\W          Соответствует любому не буквенноцифровому символу и не символу нижнего подчеркивания («_»)
[..]        Соответствует любому одному из символов, перечисленных в скобках, можно также указывать диапазоны
            символов (например, [0-5] — любая цифра от 0 до 5).
            Внимание! метасимволы внутри [] теряют свое специальное значение и обозначают просто символ. 
            Например, точка внутри [] будет обозначать именно точку, а не любой символ
[^..]       Соответствует любому одному символу, кроме перечисленных в скобках или кроме тех, что попадают в
            указанный диапазон
\b          Соответствует началу или концу слова (т.е. слева от \b
            пусто или не буквенный символ, справа буква и наоборот для конца слова).
            В отличие от предыдущих шаблонов соответствует
            позиции, а не символу
\B          Соответствует «внутреннему» (неграничному) символу слова (т.е. слева и справа от \B буквенные символы,
            или слева и справа от \B не буквенные символы)
------------------------------------------------------------------------------------------------------------------
"""
# import re
# userStr = "abcd abc efgh"
# match = re.search(r"\w{4}", userStr)
# print(match.group())
# print(match.group(0))

# import re
# userStr = "abcd abc 12 123 efgh 456"
# match = re.search(r"\d{3}", userStr)
# print(match.group())

# import re
# userStr = "My cell phone numbers: Vodafone +38(095)1234567; Cellcom +38(067)9875612"
# match1 = re.search(r"Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)", userStr)
# print(match1.group())
# print(match1.group(1,2))

# import re
# userStr = "2021-2022 Competition Calendar:30.11.2021 — 2021 Grand Prix Series; 14.01.2022 — Grand Pemio D'Italia"
# match2 = re.findall(r'\d{2}\.\d{2}\.\d{4}', userStr)
# print(match2) # ['30.11.2021', '14.01.2022']

# import re
# userStr1="My cell phone numbers: Vodafone +38(095)1234567; Cellcom +38(067)9875612"
# userStr2="Vodafone +38(095)1234567; Cellcom +38(067)9875612 — my cell phone numbers"
# match3 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr1)
# match4 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)', userStr2)
#
# print(match3) #None
# print(match4.group()) # Vodafone +38(095)1234567; Cellcom +38(067)9875612

# import re
# userStr = "2021-2022 Competition Calendar: 30.11.2021 — 2021 Grand Prix Series; 14.12.2021 — Grand Pemio D'Italia"
# newStr = re.sub(r'[-;]', '/',userStr)
# print(newStr) #2021/2022 Competition Calendar:30.11.2021 / 2021 Grand Prix Series/ 14.12.2021 / Grand Pemio D'Italia


# import re
# userStr="30.11.2021 — 2021 Grand Prix Series, 14.12.2021 — Grand Pemio D'Italia; 27.12.2021 — Cup of Austria by IceChallenge"
# strList=re.split(r'[,;]+', userStr)
# print(strList) # создаёт список


"""
------------------------------------------------------------------------------------------------------------------------
Понятие классического массива - список
------------------------------------------------------------------------------------------------------------------------
"""
# courses = ["math", "algoritms", "databases"]
# courses1 = list(("math", "algoritms", "databases"))
#
# print(courses)
# print(type(courses))
# print(courses1)
# print(type(courses1))

# courses = ["яблоко", 234, 7009, "network", 5 + 5, True]
#
# print(courses)
# print(type(courses))


# вложение в список
# myList = [1, 22, 3, 4, 5, [45, "ckjdjdj"]]
#
# print(myList)
# print(myList[5][0])

# mySymbols = list("abcde")
# print(mySymbols) #разбивка

# list1 = [i * i for i in range(6)]
# print(list1)

# list2 = [ i + "*" for i in "exzample"]
# print(list2)

# list3 = [ i * 5 for i in "abcdtf"]
# print(list3)

# list4 = [i * i for i in range(1,11) if i % 2 == 0]
# print(list4)

# customers = ["михаил", "никита", "евгений", "андрей"]
# list5 = [i for i in customers if i != "никита" and i != "андрей"]
# print(list5)

# list6 = [x * y for x in range(1,4) for y in range(1,4)]
# print(list6)


# list6 = [[x * y for x in range(1,4)] for y in range(1,4)]
# for o in list6:
#     print(o)

# myList = ["uzer", 12, 200.34, False, True]
# print(myList[-1])
# print(myList[1])
# print(myList[len(myList)-1])

#срезы в списках
# myCourses = ["algoritms", 2345, 7009, "Networks", "databases"]
# print(myCourses[1:3])
# print(myCourses[-4:-2])
# print(myCourses[1:-1])
# print(myCourses[::-1])
# print(myCourses[3:])
# print(myCourses[::2])
# print(myCourses[::-1])
# print(myCourses[-4::-1])

# category = ["вася","петя","коля"]
# print(category)
# category[0] = "action"
# print(category)










