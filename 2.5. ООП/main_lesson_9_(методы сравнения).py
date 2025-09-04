"""
методы сравнения
__eq__ - равенство(==)
__ne__ - неравенство(!=)
__lt__ - меньше(<)
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно
"""

def __eq__(self, other):
    return "результат сравнения"

def __ne__(self, other):
    return "результат сравнения"

class Cord:
    def __init__(self, x):
        self.x = x

cord1 = Cord(50)
cord2 = Cord(50)

print(cord1 == cord2)

#-----------------------------------------------------------------------------
class Cord:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):            # other - объект сравнения
        return self.x == other.x

    # def __ne__(self, other):            # other - объект сравнения
    #     return self.x != other.x

    # def __ne__(self, other):            # other - объект сравнения
    #     return not self.__eq__(other)

cord1 = Cord(50)
cord2 = Cord(50)

print(cord1 == cord2)
print(cord1 != cord2)         # лучше указывать по назначению

"""
пример
"""
class Cord:
    def __init__(self, x):
            self.x = x

    def __eq__(self, other):
        if isinstance(other, Cord):
            return self.x == other.x
        if isinstance(other, int):
            return self.x == other

    def __neg__(self, other):
        return not self.__eq__(other)

cord1 = Cord(50)
cord2 = Cord(50)

print(cord1 == cord2)
print(cord1 == 50)

print(cord1 != cord2)
print(cord1 != 50)

"""
примерчик
"""
class Words:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return len(self.word) == len(other.word)

word_1 = Words('Vasya')
word_2 = Words('Masha')

print("YES" if word_1 == word_2 else "NO")
#----------------------------------------------------------------
class Words:
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        return self.word == other.word

word_1 = Words('Vasya')
word_2 = Words('Masha')

print(word_1 != word_2)

"""
задачка

Часть кода уже написана, вам нужно лишь объявить метод _eq_
Метод _eq_(self, other) содержит две проверки:

- Если other является экземпляром класса Number, 
то возвращается результат сравнения (==) атрибутов summa 
у двух экземпляров класса. То есть self и other здесь являются 
экземплярами и нужно сравнить атрибуты summa этих экземпляров и вернуть результат.

- Если other является числом (int), то возвращается результат сравнения (==) атрибута 
summa, с other.
- Для проверки лучше всего использовать isinstance().
"""

class Number:
    def __init__(self, x, y):
        self.sum = x + y

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.sum == other.sum

        if isinstance(other, int):
            return self.sum == other

num_1 = Number(4, 2)
num_2 = Number(5, 3)

print(num_1 == num_2)


"""
__lt__ - меньше(<)
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно
"""

class Person:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

id1 = Person(16)
id2 = Person(22)

print(id1 < id2)
print(id1 > id2)

"""
примеры
"""

class Person:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


id1 = Person(16)
id2 = Person(22)

print(id1 < id2)
print(id1 > id2)

#------------------------------------------------------------
class Person:
    def __init__(self, age):
        self.age = age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age


id1 = Person(25)
id2 = Person(30)
id3 = Person(30)

print(id1 <= id2)
print(id1 >= id2)
print(id2 <= id3)

class Books:
    def __init__(self, book_name, book_page):
        self.book_name = book_name
        self.book_page = book_page

    def __le__(self, other):
        return self.book_page <= other.book_page

    def __ge__(self, other):
        return self.book_page >= self.book_page

book1 = Books("Война и мир", 1368)
book2 = Books("Собака Баскервилей", 112)
book3 = Books("Скотный двор", 112)

print(book1 >= book2)
print(book1 <= book3)
print(book2 >= book3)


"""
методы чисел
__add__ (+) (radd, iadd)
__sub__ (-)
__mul__ (*)
__truediv__ (/)
__abs__ (используется при использовании встроенной функции abs() для объекта)


resalt1 = экземпляр + 100 #__add__
resalt2 = 100 + экземпляр #__radd__
экземпляр += экземпляр #__iadd__
экземпляр += 100 #__iadd__
"""

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

num1 = Number(12)
result = num1 + 88
print(result)

#--------------------------------------------
class Number:
    def __init__(self, num):
        self.num = num

    def __radd__(self, other):
        return self.num + other

num1 = Number(12)
result = 88 + num1
print(result)

#----------------------------------------------
"""
num1 = Num(10)
num2 = Num(20)
num3 = Num(30)
res1 = num1 + 40 + 50 - выполняется только __add__
res2 = 40 + 50 + num1 + num2 - выполняется только __radd__
res3 = num1 + num1 + num2 - выполняется только __add__ и __radd__

пример слоения экземпляров
"""
class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        if isinstance(other, Number):
            return self.num + other.num
        elif isinstance(other, int):
            return self.num + other

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.num

num1 = Number(10)
num2 = Number(20)
num3 = Number(30)

res1 = num1 + 40 + 50
res2 = num1 + num2 + num3

print(res1)
print(res2)

#----------------------------------
class Number:
    def __init__(self, num):
        self.num = num

    def __iadd__(self, other):
        if isinstance(other, Number):
            self.num += other.num
            return self
        if isinstance(other, int):
            self.num += other
            return self


num1 = Number(10)
num2 = Number(20)

num1 += num2
print(num1.num)

num1 += 40
print(num1.num)

num1 += 30
print(num1.num)

"""
примерчик
"""
class Number:
    def __init__(self, number):
        self.number = number

    def __radd__(self, other):
        if isinstance(other, int):
            return self.number + other

num1 = Number(50)
num2 = Number(30)
result1 = 20 + num1 + num2
print(result1)


