"""
------------------------------------------------------------------------------------
                            ООП (наследование, полиморфирзм, инкапсуляция)
------------------------------------------------------------------------------------
"""

"""
1) Вася продвинулся в программировании и решил создать
небольшую соцсеть и назвал её Person. Помогите Васе создать его первый аккаунт id_1.

Создайте класс Person
Создайте атрибут name внутри класса, и присвойте ему значение "Vasya"
Создайте экземпляр класса и назовите его id_1. Не забывайте про скобки у класса.
Выведите на экран значение атрибута name, который принадлежит экземпляру id_1,
используя print()
"""
print("Задание 1")
class Person:
    name = "Vasya"

id_1 = Person()

print(id_1.name)


"""
2) Вася продолжает создавать свою соцсеть Person. 
И в этот раз ему нужно научиться изменять имена пользователей, с помощью классов.

Создайте класс Person.
Создайте в классе Person, атрибут name со значением "Vasya".
Создайте экземпляр id_1 класса Person.
Создайте в экземпляре id_1, атрибут name со значением "Lena".
Измените в классе Person атрибут name на значение "Masha".
Выведите на экран значение атрибута name класса Person, и экземпляра id_1 с помощью print. 
Каждый результат на отдельной строке, сначала у Person, затем у id_1 (см. пример ниже).
"""
print("\nЗадание 2")
class Person:
    name = "Vasya"
a = Person.name
id_1 = Person()
id_1.name = "Lena"
b = id_1.name
id_1.name = "Masha"
c = id_1.name


print(Person.name)
print(b)
print(c)

"""
3) У Машеньки день рождения, и она планирует отправиться в парк с единорогами. 
В парке идёт акция, приведи 5 друзей и получишь шапку-единорожку. 
Машенька любит разные весёлые шапки, поэтому пригласила 5 друзей. 
Но в последний момент один из её друзей не смог прийти, 
и она решила пригласить вас на свой день рождения. Помогите Машеньке обрести 
шапку-единорожку.

Создайте пустой класс Holiday (используйте pass внутри класса).
Создайте экземпляр friends.
Создайте 5 атрибутов для экземпляра friends, с именами name1, 
name2...name5 со значениями 'Sveta', 'Katya', 'Lena', 'Natasha', 
'Leonardo DiCaprio' соответственно.
Так как 'Leonardo DiCaprio' не смог прийти, Машенька приглашает вас на свой ДР. 
Измените атрибут name5 на своё имя, или можете использовать любое другое имя.
Часть кода уже написана, вам нужно лишь сделать то, что написано в задании.
"""
print("\nЗадание 3")
class Holiday:
    pass

friends = Holiday()
friends.name1 = 'Sveta'
friends.name2 = 'Katya'
friends.name3 = 'Lena'
friends.name4 = 'Natasha'
friends.name5 = 'Leonardo DiCaprio'

friends.name5 = 'Evgeny'

print(friends.name1)
print(friends.name2)
print(friends.name3)
print(friends.name4)
print(friends.name5)

"""
примерчики
"""
class Person:
    def __init__(self, name, gender, age, study, work):
        self.name = name
        self.gender = gender
        self.age = age
        self.study = study
        self.work = work


id_1 = Person("Вася", "муж.", 18, "колледж", "доставка")
id_2 = Person("Ярослав", "муж.", 18, "универ", "сварщик")
id_3 = Person("Маша", "жен.", 18, "колледж", "кассир")

print(id_1.__dict__)

class Person1:
    def __init__(self, music, film, what, ufo, ID):
        self.music = music
        self.film = film
        self.what = what
        self.ufo = ufo
        self.ID = ID

id_1_1 = Person1("Техно", "Кино", "всё", "объект", 1234)
print(id_1_1.__dict__)



"""
функции для работы с атрибутами

setattr - создание атрибута или изменение его
getattr - получение значения атрибута
hasattr - проверка наличия атрибута
dejattr - удаление атрибута
"""

"""
setattr
"""

class Person:
    pass

id_1 = Person()
setattr(id_1, "name", "Кирилл")
print(id_1.__dict__)
setattr(id_1, "name", "Женя")
print(id_1.__dict__)
id_1.name = "Артём"
print(id_1.__dict__)

file = {"name": "Alex", "age": 18, "hobby": "film"}

class Person:
    pass

id_1 = Person()

for k, v in file.items():
    setattr(id_1, k, v)

print(id_1.__dict__)
print(id_1.name)

#__________________________________________________
class Person:
    pass

id_1 = Person()
setattr(id_1, "name", "Вася")
print(id_1.__dict__)
setattr(id_1, "name", "Маша")
#__________________________________________________

class Person:
    setup = ['set_name', 'set_age', 'set_work', 'set_study']

id_1 = Person()

for i in id_1.setup:
    setattr(id_1, i, input())

print(id_1.__dict__)

for i in id_1.setup:
    print(getattr(id_1, i))

"""
getattr
"""
class Person:
    name = "Вася"
    age = 14

person_1 = Person()

print(getattr(person_1, "name", False))
print(getattr(person_1, "age", False))

file = ["name", "age", "hobby", "lolo"]

class Person:
    hobby = "films"

for v in file:
    if getattr(Person, v, False):
        print(v)

"""
задачка
"""
"""
Маша, Prosto, Kvasha, Мы любим тебя
"""

class Person:
    name1 = 'Masha'
    name2 = 'Prosto'
    name3 = 'Kvasha'

list_person = []
file = ['name1', 'name2', 'name3', 'name4']

for value in file:
    list_person.append(getattr(Person, value, 'Мы любим тебя'))

print(list_person)

"""
Создайте экземпляр id_1 класса Person. Не забывайте про скобки Person().
С помощью getattr(), выведите на экран значения трёх атрибутов, используя экземпляр. 
Каждое значение выводится на отдельной строке, начиная с dance, 
смотрите пример вывода ниже. Не забывайте про кавычки, если используете getattr() вне цикла.
По желанию, используйте цикл for.
"""

class Person:
    pass

id_1 = Person()
print(getattr(id_1, "name", "Вася"))
print(getattr(id_1, "age", 18))
print(getattr(id_1, "hobby", "футболист"))

#--------------------------------------------------------
list_person = ["hobby", "work", "study"]
class Person:
    hobby = "dance"
    work = "design"
    study = "college"

id_1 = Person()
print(getattr(id_1, "hobby"))
print(getattr(id_1, "work"))
print(getattr(id_1, "study"))
#

"""
Машенька увлеклась изучением коктейлей, и используя книгу, 
решила угостить вас её коктейлем. Правда Машенька не знала, 
что это книга для начинающих ведьмочек. Напишите программу, чтобы узнать, 
какие ингредиенты выпадут именно вам.

Задание:
Часть кода уже написана
Создайте класс Magic
Создайте атрибут класса ingredients со значением sample(magic_ing, 3). 
Таким образом создастся список из трёх рандомных ингредиентов для коктейля.
Создайте экземпляр my_cocktail от класса Magic (не забудьте скобки).
С помощью цикла и getattr(), выведите на экран три ингредиента, которые находятся 
в атрибуте ingredients, используя экземпляр. Если не получится, можете вывести без цикла, 
но с помощью getattr() для тренировки. Не забывайте кавычки в имени атрибута.
Нажмите кнопку "Запустить код", таким образом вы увидите ингредиенты, которые 
Машенька приготовила для вашего коктейля.
Закомментируйте, всё что вы сделали в пункте 5 задания. Закомментировать, 
значит поставить # перед кодом.
Выведите на экран текст: "Спасибо, Машенька!" и нажмите кнопку "Отправить".
"""
from random import sample

class Magic1:
    magic_ing = ["cocos", "banan", "kiwi", "яблоко", "клубника", "арбуз", "сливки"]
    ingredients = sample(magic_ing, 3)

my_cocktail = Magic1()

for v in my_cocktail.ingredients:
    getattr(my_cocktail, "ingredients")
    print(v)

print("спасибо Машенька")



"""
hasattr - проверка наличия атрибута
"""

class Person:
    hobby = "dance"
    work = "design"
    study = "college"

id_1 = Person()

print(hasattr(Person, "hobby"))
print(hasattr(id_1, "hobby"))
print(hasattr(id_1, "age"))


"""
Предыстория:
Машенька подписана на журнал "Покемоны". С каждым новым журналом, 
в подарок идут три рандомные карточки с покемонами. 
Проверьте, есть ли в новом журнале покемоны, которых нет у Машеньки.

Задание:
Создайте пустой класс Pokemon (используйте pass).
Создайте экземпляр pokemons класса Pokemon.
С помощью setattr(), добавьте в экземпляр 4 атрибута: 
pikachu, scyther, gyarados, gengar. Значения у всех атрибутов будет пустая строка, 
например pikachu = "". Можно использовать списки и циклы, или как вам удобней.
С помощью hasattr(), сделайте проверку, есть ли в экземпляре атрибут: 
lapras, pikachu, alakazam. Результат проверки напишите на отдельной строке, 
соответственно перечисленным атрибутам (см. пример ниже).
"""

class Pokemon:
    pass

pokemons = Pokemon()
setattr(pokemons, "pikachu", "")
setattr(pokemons, "scyther", "")
setattr(pokemons, "gyarados", "")
setattr(pokemons, "gengar", "")

print(hasattr(pokemons, "lapras"))
print(hasattr(pokemons, "pikachu"))
print(hasattr(pokemons, "alakazam"))



