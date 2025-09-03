def double_ex(x):
    return x * 2

numbers = [1, 2, 3, 4, 5, 6]

double_numbers = map(double_ex, numbers)

print(list(double_numbers))


numbers = [1, 2, 3, 4, 5, 6]
sq_numbers = map(lambda  x:x ** 2, numbers)
print(list(sq_numbers))

def func(x,y):
    return x + y
list_1 = [1,2,3]
list_2 = [3,4,5]

result = map(func, list_1, list_2)
print(list(result))

word = ["hello", "world", "python"]
upper_words = map(str.upper, word)
print(list(upper_words))

people = [{"name":"Alice", "age":30},{"name":"Bob", "age":25},]
names = map(lambda person:person["name"], people)
print(list(names))

string_numbers = ["1", "2", "3", "4"]
my_int = map(lambda x:int(x), string_numbers)
print(list(my_int))

numbers = [1,2,3,4,5,6]
result = map(lambda x:x ** 2, map(lambda x:x * 2, numbers))
print(list(result))

names = ["егор", "артём", "николай"]
ages = [30,25,35]
people_dict = dict(map(lambda name_age:(name_age[0], name_age[1]), zip(names, ages)))
print(people_dict)

numbers = [1, 2, 3, 4, 5, 6]

def even(n):
    return n % 2 == 0

even_numbers = filter(even, numbers)

print(list(even_numbers))


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x:x % 2 == 0, numbers)
print(list(even_numbers))

names = ["ег", "артём", "николай"]
sps = filter(lambda str_my:len(str_my) > 3, names)
print(list(sps))

data = [0, "", None, "Hello", 42]
filtered_data = filter(None, data)
print(list(filtered_data))

numbers = range(30)
filtered_numbers = filter(lambda x:x%3 ==0 and x < 20, numbers)
print(list(filtered_numbers))

numbers = [-10, -5, 0, 5, 10]
pos_num = filter(lambda x:x<0, numbers)
print(list(pos_num))

#----------------------------------------------------------------------задачки
names = ["егор", "артём", "николай"]
ages = [30,25,35]
people_dict = dict(map(lambda name_age:(name_age[0], name_age[1]), zip(names, ages)))
print(people_dict)

numbers = [1,2,3,4,5,6]
result = map(lambda x:x ** 2, map(lambda x:x * 2, numbers))
print(list(result))

#возведение в куб
numbers = [1,2,3,4,5,6]
result = map(lambda x:x ** 3, numbers)
print(list(result))

#строка в нижний регистр
word = ["heLLo", "worLd", "pyThon"]
upper_words = map(str.lower, word)
print(list(upper_words))

#умножение 4 списков
def func(a,b,c,d):
    return a * b * c * d
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3]
list_4 = [1, 2, 3]

result = map(func, list_1, list_2, list_3, list_4)
print(list(result))

#цельсий в фаренгейт
ccc = [10, 20, 30]
result = map(lambda x:x * 2 + 30, ccc)
print(list(result))

#удаление пробелов
word_1 = ["heLLo worLd pyThon"]
upper_words_1 = map(str, word_1.replace(""))
print(list(upper_words_1))

#извлечение по ключу из словаря
people = [{"name":"Alice"},{"name":"Bob"}]
names = map(lambda person:person["name"], people)
print(list(names))

