"""
                                        Классы
объект - единица информации в памяти
экземпляр - конкретный объект каждого класса
класс - инструкция по созданию объектов определённого типа
метод - функция в классе для воздействия на объект

"""
"""
Окно
"""
# from tkinter import Tk
#
# root = Tk()
# root.mainloop()


"""
создание класса
"""
# class Purse:
#     pass
#
# x = Purse()
# print(type(x))

# class Purse:
#     def show(self, name="xxx"):
#         print("Hello", name)
#
#
# x = Purse()
# y = Purse()
# x.show()
# y.show("Alice")

#-------------------------------------------------
class Purse:

    def __init__(self, valuta, name="xxx"):
        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.money = self.money + howmany

    def top_dow_balance(self, howmany):
        if self.money - howmany < 0:
            print("недостаточно средств")
            raise ValueError ("недостаточно средств")
        self.money = self.money - howmany

    def info(self):
        return self.money

x = Purse("USD")
y = Purse("EUR", "Bill")
x.top_up_balance(100)
print(y.info())
print(x.info())

x.top_dow_balance(100)
print(x.info())