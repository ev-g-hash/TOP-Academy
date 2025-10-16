"""
СЛОВАРИ
"""
"""
способы создания, просмотры, вызовы
"""
# d1 = {"a": 7}
# print(d1)
# print(d1["a"])
# print(d1.keys())
# print(d1.values())
# d1["b"] = 2
# print(d1)
# d1["a"] = 3
# print(d1)
# del d1["a"]
# print(d1)
#
# #----------------------------------------------------------------
# d2 = dict(b=2)
# d2_1 = dict([["евгений",89088595009],["ксения",89088600299]])
# print(d2)
# print(d2_1)
# #--------------------------------------------------------------
# d3 = dict.fromkeys([1,2,3,4])
# print(d3)
# d3 = dict.fromkeys([1,2,3,4], "val")
# print(d3)

"""
вложенный словарь
"""
# users = {
#     "Alex7": {"password": 9856214, "id": 1957},
#     "Jimmy99": {"password": 123648, "id": 9654},
#     "Bob33": {"password": 9546752, "id": 6453},
#     }
#
# print(users["Alex7"]["password"])
# print(users["Alex7"]["id"])

"""
пример работы с функцией
"""
# price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}
# def buy():
#     pay = 0
#     while True:
#         enter = input("Что покупаем???\n")
#         if enter == "end":
#             break
#         pay += price[enter]
#     return pay
#
# print(buy())

"""
методы
"""
# d1 = {"a": 7, "b": 9}
# d2 = dict([["евгений",89088595009],["ксения",89088600299]])
# d3 = dict.fromkeys([1,2,3,4], "val")
#
# d5 = d1.copy()
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d1.update(d2)
# print(d1)
#
# y = d1.get("c", "val")
# print(y)
#
# t = d1.pop("a")
# print(t)

"""
циклы
"""
# price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}
#
# for i in price:
#     print(i)
#
# new_price = {}
# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)
#
# print(price)
# print(new_price)

#----------------------------------------------------------
# price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}
#
# new_price = {}
# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)
#
# x = new_price.items()
# print(price)
# print(new_price)
# print(x)
# print(type(x))
#
# for k, v in price.items():
#     print(k)
#     print(v)
#
# new = {}
# for k, v in price.items():
#     new[v] = k
#
# print(new)
#
# for v in price.values():
#     print(v)
#
# for k in price.keys():
#     print(k)



