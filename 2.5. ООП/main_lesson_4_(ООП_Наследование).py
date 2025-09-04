"""
-----------------------------------------------------------------------------------------
                                    Наследование
-----------------------------------------------------------------------------------------
"""

class Transport:
    pass                            # Родительский класс

class Car(Transport):
    pass                            # Дочерний класс

"""
примеры
"""

class Transport:
    name = "car"
    def get_name(self):
        return self.name

class Car(Transport):
    pass

toyota = Car()
print(toyota.name, toyota.get_name())
print(Car.name)

#-----------------------------------------------
class Transport:
    name_transport = "класс транспорт"
    def get_transport(self):
        return "метод Транспорт"

class Car(Transport):
    name_car = "атрибут Car"
    def get_car(self):
        return "метод Car"

car = Car()
print(car.name_car, car.get_car(), car.name_transport, car.get_transport())

transport = Transport()
print(transport.name_transport, transport.get_transport())


"""
----------------------------------------------------------------------------
"""

class Transport:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

class Car(Transport):
    pass

class Airplane(Transport):
    pass

class Train(Transport):
    pass

toyota = Car("легковой автомобиль", 100)
tu_154 = Airplane("самолёт", 1000)
poezd = Train("поезд", 300)

print(toyota.__dict__)
print(tu_154.__dict__)
print(poezd.__dict__)

"""
Дочерний класс наследует все атрибуты и методы родительского класса

Экземпяры наследуют класс (родительский или дочерний) и могут обращаться к ним

Наследование позволяет избежать повторяющего кода

Видимая область важная составляющая в этих моментах
"""

"""
Задание:
Создайте класс Homer.
Создайте в классе Homer метод _init_(self, name), который создает атрибут name.
Создайте пустой класс Daughter и сделайте его дочерним классом для Homer. 
Используйте pass для пустого класса.
Создайте экземпляр daughter1 для класса Daughter и присвойте атрибуту name значение Lisa.
Выведите на экран значение атрибута name через экземпляр daughter1
"""

class Homer:
    def __init__(self, name):
        self.name = name

class Daughter(Homer):
    pass

daughter1 = Daughter("Lisa")

print(daughter1.name)
print(daughter1.__dict__)


"""
Области видимости
"""

class Transport:
    name = "toyota"                 #родитель

class Avto(Transport):
    pass                            #дочка

rav4 = Avto()                       #экземпляр дочки

print(rav4.name)                    #вывод данных


"""
Переопределение
"""
class Transport:
    name1 = "toyota"
    name2 = "subaru"
    name3 = "opel"

class Avto(Transport):
    name2 = "Lada"

rav4 = Avto()
rav4.name3 = "Vaz"

print(Transport.name1, Transport.name2, Transport.name3)
print(Avto.name1, Avto.name2, Avto.name3)
print(rav4.name1, rav4.name2, rav4.name3)


#-------------------------методы унаследовали и внесли изменения

class Cat:
    def say_cats(self):
        print("hello cats!")
    def say_dogs(self):
        print("hello dogs!")

class Dog(Cat):
    def say_dogs(self):
        print("Ваф! Ваф!")

cat = Cat()
cat.say_cats()
cat.say_dogs()

dog = Dog()
dog.say_dogs()
dog.say_cats()

"""
пример
"""

class Simpson:
    name1 = "Homer"
    name2 = "Marge"

class Daughter(Simpson):
    name1 = "Lisa"
    name2 = "Meggy"

name_is = Simpson()
print(name_is.name1)



"""
Полиморфизм

пример

часто используется в играх пример при озвучке персонажей при атаке
команда имеет одно и то же имя, а вот действия разные.
"""

class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


"""
задачки

Предыстория:
Вася программирует и составляет родословную на компьютере. 
Кондратий Палыч - это дедушка Маши, а Вася - это отец Маши. 
Но что-то пошло не так и получилось, что Маша - это отец, а Вася - это дед. 
Исправьте пожалуйста код, чтобы было всё верно.
Задание:
Код уже написан, но с ошибками. Подумайте, что можно поменять чтобы 
семейный статус выводился верно.
В комментарии указано в какой области кода ошибка, внесите исправления именно там.
В итоге команда print(masha.status) и print(vasya.status), 
должны выводить слова Дочь и Отец на отдельных строках. 
Код с выводом на экран написан правильно, его исправлять не нужно.
"""

class Grandfather:
    def status(self):
        return "Это дед"

class Father(Grandfather):
    def status(self):
        return "Это Отец"

class Daughter(Father):
    def status(self):
        return "Это Дочь"

vasya = Father()
masha = Daughter()

print(vasya.status())
print(masha.status())

#------------------------------------------------------------

class Kondraty_Palich:
    status = 'Деда'

class Vasya(Kondraty_Palich):
    status = 'Отец'

class Masha(Vasya):
    status = 'Дочь'

# подумайте что можно поменять вот здесь:
masha = Vasya()
vasya = Kondraty_Palich()

# эту часть кода не исправляйте:
print(masha.status, vasya.status, sep='\n')


"""
Задачка

Задача 3: Классы для сотрудников

Создайте базовый класс Employee с атрибутами name и salary. 
Затем создайте два класса-наследника: Manager и Developer, 
которые добавляют свои специфические атрибуты и методы.
"""

class Employee:
    name = "сотрудник"
    salary = "зарплата"

class Manager(Employee):
    name = "Mенеджер"
    salary = "30000р"
    def status(self):
        return "IP-телефония"

class Developer(Employee):
    name = "Разработчик"
    salary = "130000р"
    def status(self):
        return "Python - разработчик"

manager = Manager()
developer = Developer()

print(manager.name, manager.salary, manager.status())
print(developer.name, developer.salary, developer.status())


"""
Задача 5: Классы для студентов

Создайте базовый класс Student, который будет иметь атрибуты name и grade. 
Затем создайте два класса-наследника: Undergraduate и Graduate, 
которые добавляют свои специфические атрибуты и методы.
"""

class Student:
    name = "студент"
    grade = "оценка"

class Undergraduate(Student):
    name = "Бакалавриат"
    grade = "отличник"
    def status(self):
        return "Бакалавр"

class Graduate(Student):
    name = "Выпускник"
    grade = "хорошист"
    def status(self):
        return "Выпускается"

undergraduate = Undergraduate()
graduate = Graduate()

print(undergraduate.name, undergraduate.grade, undergraduate.status())
print(graduate.name, graduate.grade, graduate.status())








