"""
Условные операторы
"""
# car_0 = "subaru"
# print(car_0 == "subaru")
#
# car_1 = "audi"
# print(car_1 == "subaru")
#
# print(car_0 == car_1)
#
# car_3 = "audi"
#
# print(car_3 == car_1)
#
# car_4 = "Audi"
# print(car_4 == "audi")
#
# car_4 = "Audi".lower()
# print(car_4 == "audi")
#
#
# my_age_0 = 20
# my_age_1 = 22
#
# print(my_age_0 == 20)
# print(my_age_0 >= 20)
# print(my_age_0 >= 20 and my_age_1 >=23)
# print(my_age_0 >= 20 or my_age_1 >=23)
#
# sps = [1,2,3,4,5]
# print(2 in sps)

"""
#----------------------------------------------------------------------------------
"""
alien_color = "red"
if alien_color == "green":
    print("вы заработали 5 очков")

alien_color_2 = "red"
if alien_color_2 == "red":
    print("вы заработали 5 очков")

alien_color_3 = "green"
if alien_color_3 == "red":
    print("вы заработали 5 очков")
else:
    print("вы заработали 10 очков")

alien_color_3 = "green"
if alien_color_3 == "green":
    print("вы заработали 5 очков")
else:
    print("вы заработали 10 очков")

alien_color_3 = "green"
if alien_color_3 == "green":
    print("вы заработали 5 очков")
if alien_color_3 == "yellow":
    print("вы заработали 10 очков")
if alien_color_3 == "red":
    print("вы заработали 15 очков")

alien_color_3 = "yellow"
if alien_color_3 == "green":
    print("вы заработали 5 очков")
if alien_color_3 == "yellow":
    print("вы заработали 10 очков")
if alien_color_3 == "red":
    print("вы заработали 15 очков")

alien_color_3 = "red"
if alien_color_3 == "green":
    print("вы заработали 5 очков")
if alien_color_3 == "yellow":
    print("вы заработали 10 очков")
if alien_color_3 == "red":
    print("вы заработали 15 очков")

my_age = 2

if my_age > 0:
    if my_age < 2:
        print("младенец")
    elif my_age < 4:
        print("малыш")
    elif my_age < 13:
        print("ребёнок")
    elif my_age < 20:
        print("подросток")
    elif my_age < 65:
        print("взрослый")
    elif my_age >= 65:
        print("пожилой человек")
else:
    print("введите положительное число")

sps = ["банан", "вишня", "яблоко", "арбуз"]

if "арбуз" in sps:
    print("ok")
else:
    print("noy")

my_sps = ["банан", "яблоко", "арбуз"]

if "арбуз" in my_sps:
    print("вы очень любите бананы1")
if "яблоко" in my_sps:
    print("вы очень любите бананы2")
if "вишня" in my_sps:
    print("вы очень любите бананы3")