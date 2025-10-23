"""
циклы - for
"""
# pizza = ["пеперонни", "ташир", "ассорти", "венеция"]
#
# for i in pizza:
#     print(f"я люблю пиццу {i}")
# print("я очень люблю вкусно поесть особенно пиццу!")
#
# my_animal = ["собака", "хомяк", "кошка"]
# for i in my_animal:
#     print(f"{i} - отличное домашнее животное")
# print("любое из этих животнох - отличное домашнее животное")

#----------------------------------------------------------------------

# for i in range(20):
#     print(i)

# my_numbers = list(range(1_000_001))
# print(my_numbers)

# for i in my_numbers:
#     print(i)

# print(min(my_numbers))
# print(max(my_numbers))
# print(sum(my_numbers))

# for i in range(1, 20 , 2):
#     print(i, end=" ")

# for i in range(3, 30 , 3):
#     print(i, end=" ")

# y = []
# for i in range(1, 10):
#     y.append(i ** 3)
# print(y)
#
#
# my_cub = [i ** 3 for i in range(1, 10)]
# print(my_cub)

#-------------------------------------------------------------------срезы

# my_num = [1,2,3,4,5,6,7,8,9,10]
# print(f"первые три цифры это - {my_num[:3]}")
# print(f"середина это - {my_num[3:6]}")
# print(f"последние три цифры это - {my_num[-3:]}")

# my_pizza = ["пеперонни", "ташир", "ассорти", "венеция"]
# friend_pizza = my_pizza[:]
# my_pizza.append("помидорная")
# friend_pizza.append("колбасная")
# print(my_pizza)
# print(friend_pizza)
#
# for i in my_pizza:
#     print(f"мои любимые пиццы - {i}")
#
# for i in friend_pizza:
#     print(f"любимые пиццы моего друга - {i}")