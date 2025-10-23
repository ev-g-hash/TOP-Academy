"""
---------------------------------------------------------------------------------------
списки
--------------------------------------------------------------------------------------
"""
#
# names = ["Денис", "Виталя", "Лёха", "Юра", "Серёга"]
#
# print()
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
#
# message_1 = f"Привет мой друг {names[0]}"
# message_2 = f"Привет мой друг {names[1]}"
# message_3 = f"Привет мой друг {names[2]}"
# message_4 = f"Привет мой друг {names[3]}"
# message_5 = f"Привет мой друг {names[4]}"
#
# print()
# print(message_1)
# print(message_2)
# print(message_3)
# print(message_4)
# print(message_5)
#
#
# avto = ["Лада Гранта", "Нива Шевроле", "Джилли МК Kросс"]
#
# print(f"\nЯ хотел бы купить {avto[2]}")
#
#
# #-----------------------------------------------------------------------
# print()
# print(f"я приглашаю вас на обед {names[0]}, {names[1]} и {names[3]}")
# print(f"{names[3]} не сможет придти")
#
# names[3] = "Петя"
# print(names)
#
# print()
# print("всем привет я купил стол большего размера и у меня будет много гостей")
#
# names.insert(0, "Вася")
# print(names)
# names.insert(2, "Коля")
# print(names)
# names.append("Зина")
# print(names)
#
# prig_0 = f"приглашаю в гости {names[0]}"
# prig_1 = f"приглашаю в гости {names[1]}"
# prig_2 = f"приглашаю в гости {names[2]}"
# prig_3 = f"приглашаю в гости {names[3]}"
# prig_4 = f"приглашаю в гости {names[4]}"
# prig_5 = f"приглашаю в гости {names[5]}"
# prig_6 = f"приглашаю в гости {names[6]}"
#
#
# print(prig_0)
# print(prig_1)
# print(prig_2)
# print(prig_3)
# print(prig_4)
# print(prig_5)
# print(prig_6)
# print()
# print(names)
#
# print("будут приглашены два гостя")
# gst_1 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_1}")
# gst_2 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_2}")
# gst_3 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_3}")
# gst_4 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_4}")
# gst_5 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_5}")
# gst_6 = names.pop()
# print(names)
# print(f"я очень сожалею {gst_6}")
# print(f"вы приглашены {names[0]} и {names[1]}")
# del names[0]
# print(names)
# del names[0]
# print(names)

"""
#--------------------------------------------------------------------------
сортировка списка

sorted(my_country) ----------------- сортирует но не меняет список
my_country.sort() ------------------ метод сортирует и изменяет список
my_country.reverse() ---------------- переворачивает (не путать с сортировкой)
"""

# my_country = ["Китай", "Россиия", "Африка", "Америка", "Белоруссия"]
# print(my_country)
# print(sorted(my_country))
# print(my_country)
# print(sorted(my_country, reverse=True)) #сортирует
# print(my_country)
# my_country.reverse()                     #меняет порядок на обратный
# print(my_country)
# my_country.reverse()
# print(my_country)
# my_country.sort()
# print(my_country)
# my_country.sort(reverse=True)
# print(my_country)
# print(len(my_country))
# my_number = [10,2,30,4,50,6]
# my_number.sort()
# print(my_number)
# my_number.reverse()
# print(my_number)
# my_number.reverse()
# print(my_number)
# my_number.sort(reverse=True)
# print(my_number)
# print(sorted(my_number))
# print(sorted(my_number, reverse=True))
# print(my_number)
# my_number.reverse()
# print(my_number)
#
# print(my_country[-1])