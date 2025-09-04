"""
------------------------------------------------------------------------------------------
                                        ООП (продолжение)
------------------------------------------------------------------------------------------
"""

"""
delattr - удаление атрибута, принимает объект и название атрибута
"""

class Person:
    pass

id_1 = Person()

setattr(id_1, "name", "Вася")
print(hasattr(id_1, "name"))


class Person:
    name = "Вася"

id_1 = Person()

if hasattr(id_1, "name"):
    delattr(Person, "name")

print(id_1.__dict__)
print(Person.__dict__)

"""
задачки
"""
names = ['Klementina', 'Roza', 'Masha', 'Balu', 'Lena', 'Leonid']  # список имён

class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''

# ниже ваш код:
for i in names:
    if hasattr(Person, i):
        delattr(Person, i)
        print(i)

# строки ниже не удаляйте, ради вселенной:
print(len(Person.__dict__))

"""
Методы - функция в классе
"""
class Calculator:
    def addition(self):
        print("складываю числа")

calc = Calculator()

calc.addition()

# ------------------------------ правильно выводить метод - через экземпляр класса
class Kitty:
    def hello_kitty(self):
        print('Hello Kitty!')

cat = Kitty()

cat.hello_kitty()

"""
Создайте класс Kitty.
Создайте метод say_hello (не забудьте про self).
Внутри метода создайте print('Hello, Kitty'). 
Метод выводит на экран строку 'Hello, Kitty'.
Создайте экземпляр cat.
Вызовите метод say_hello через экземпляр cat (не забудьте скобки). 
Функцию print здесь использовать не нужно.
"""

class Kitty:
    def say_hello(self):
        print('Hello, Kitty')

cat = Kitty()

cat.say_hello()

#-----------------------------------------------------------------------

"""
примеры
"""
def add_numbers(x, y):
    return x + y

print(add_numbers(2, 5))


class Number:
    a = 10
    b = 5

first = Number()
print(first.a + first.b)


class Calculator:
    a = 10
    b = 5

    def addition(self):
        summ = self.a + self.b
        print(summ)

first = Calculator()
first.addition()


second = Calculator()
second.b = 10
second.addition()


"""
область видимости класса self вызывается через экземпляр
"""

class Calculator:
    a = 10
    b = 5

    def addition(self):
        summa = self.a + self.b
        print(summa)

first = Calculator()
first.addition()

"""
Машенька любит смотреть мультфильм Симпсоны. 
И однажды, она решила написать письмо любимым персонажам, 
начиная со строк: "Привет, Bart". И так к каждому персонажу. 
Помогите Машеньке написать начало. 

Задание:
Часть кода уже написана.
Создайте метод и назовите его как пожелаете. Помните, что имя метода означает - глагол, 
действие, поэтому подберите соответствующее название.
Метод выводит на экран надпись: "Привет, атрибут". Но слово "атрибут" замените, 
на значение атрибута name у экземпляров. У каждого экземпляра свой атрибут name, 
поэтому и сообщения будут выводиться разными. Подсказка, можно использовать f-строку 
и не забудьте self.
Вызовите метод у каждого экземпляра. Не забывайте скобки, при вызове метода.
Примеры ответов есть ниже.
"""

class Letter:
    name = "name"

    def write(self):
        print(f"Привет, {self.name}")

masha = Letter()
masha.name = "Masha"
masha.write()

bart = Letter()
bart.name = "Bart"
bart.write()

gomer = Letter()
gomer.name = "Gomer"
gomer.write()

mardg = Letter()
mardg.name = "Mardg"
mardg.write()

"""
Предыстория:
Вася продолжает разрабатывать соцсеть Person. 
На данном этапе он работает со вкладкой сообщения. 
Рядом с кнопкой "сообщения" пользователь видит количество непрочитанных сообщений. 
Так как пользователей много, и у всех разное количество сообщений, 
поэтому Вася решил использовать self в своих методах.

Задание:
Часть кода уже написана.
Создайте метод print_number_of_messages(). 
Метод выводит на экран значение атрибута message_counter. 
У каждого экземпляра свой атрибут message_counter, поэтому используйте self.
В самом конце, выведите на экран количество сообщений у экземпляра id_1 и id_2. 
ответ на отдельной строке (см. пример ответа ниже).
"""

class Person:
    message_counter = 0

    def print_number_of_messages(self):
        print(self.message_counter)

id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10
id_2.message_counter += 10
id_2.message_counter += 30
id_2.message_counter += 50

id_1.print_number_of_messages()
id_2.print_number_of_messages()


"""
Позиционные параметры
"""

class Calculator:
    def addition(self, a, b):
        print(a + b)

calc = Calculator()
calc.addition(1,2)


"""
параметры по умолчанию
"""

class Calculator:
    def addition(self, a=0, b=0):
        print(a + b)

calc = Calculator()
calc.addition(1,2)
calc.addition(1)
calc.addition()

"""
*args **kwargs
"""

class Calculator:
    def addition(self, *args, **kwargs):
        print(sum(args), kwargs)


calc = Calculator()

calc.addition(1,2,3, **{"rrr":2})



"""
конструктор
"""

class Person:
    def set_attr(self, name, age):
        self.name = name
        self.age = age

person_1 = Person()
person_1.set_attr("Вася", 14)


print(person_1.name, person_1.age)

#--------------------------------------------------------------------------------
class Person:
    def set_attr(self, name, age):
        setattr(self, "name", name)
        setattr(self, "age", age)

person_1 = Person()
person_1.set_attr("Вася", 14)


print(person_1.name, person_1.age)


"""
Предыстория
Машенька хочет купить новый журнал с покемонами, но денег у неё нет. Журнал стоит дорого, и полную сумму никто не даст. Поэтому Машенька придумала план, попросить у каждого родственника по чуть-чуть. Она попросила у папы, мамы, деды и бабы по чуть-чуть, но вот незадача, считать то Машенька ещё не умеет. Помогите Машеньке реализовать её план.

Задание:
Создайте класс NewJournal.
Объявите два метода: set_attr() и check_money().
Метод set_attr():
- Имеет 4 параметра: papa, mama, deda, baba. Это значит set_attr(self, papa, mama...и т.д.).
- Создаёт атрибуты papa, mama, deda, baba, а значения этих атрибутов будут равны параметрам papa, mama, deda, baba, соответственно. Например self.papa = papa.
- Создаёт атрибут count_money равный сумме этих четырёх атрибутов: papa, mama, deda, baba.
Метод check_money():
- Проверяет, если атрибут count_money меньше 80, то выводит на экран: Денег не хватает
- Иначе выводит на экран: Ура, денег хватает!
Создайте экземпляр masha.
Вызовите метод set_attr() через экземпляр masha. В аргументах укажите 10, 20, 30, 40 - это наши значения для атрибутов: papa, mama, deda, baba.
Вызовите метод check_money()
Не забывайте про self и скобки при вызове методов.
"""





