"""
---------------------------------------------------------------------------------
переменные глобальные и локальные
---------------------------------------------------------------------------------
"""

x = 5 #---------------------------глобальная

def my_func():
    y = 5           # --------------------------локальная
    print(x)
    print(y)

my_func()

x1 = 5
def my_func():
    x1 += 1
print(x1) #-----------------------------ошибка так как нет локальной х


x = 5

def my_func():
    global x   ##--------------------------объявили ееё глобальной
    x += 1

print(x)

def my_func():
    x = 5
print(x) #будет ошибка так как принтуем глобальную переменную

#---------------------------------------------обозначение нонлокал
def outer():
    n = 5

    def inner():
        nonlocal n
        n = 25
        print(n)

    inner()
    print(n)

outer()    # --------------------------------nonlocal n становится в def outer()

def func():
    x = 5
    y = 10
    return x, y

result1, result2 = func()

print(result1, result2)

def func():
    x = 5
    return x
    print("sgfgdfg") #---------------------------------так нельзя

print(func())

res = lambda x:x+5
print(res(4))

# ---------------------------------------аналогично
def sum_(x):
    return x + 5

res = lambda x,y:x+y
print(res(4, 6))

# ----------------------------------------аналогично
def sum_(x, y):
    return x + y

def black_hole(*args):
    print(type(args))
    for i in args:
        print(i)

black_hole(0,5,6, "None", "adress", 2*5)

def black_hole(args):
    print(type(args))
    for i in args:
        print(i)
args = 0,5,6, "None", "adress", 2*5

black_hole(args)

#----------------------------------------------- именованные параметры

def black_hole_name(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(key)

black_hole_name(name="Nick", planet="Earth", galaxy="Milki way", num=123456)

def black_hole_name(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

black_hole_name(name="Nick", planet="Earth", galaxy="Milki way", num=123456)

def black_hole_name(*args, **kwargs):

    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key, value)

black_hole_name(0,5,6, "None", "adress", 2*5, name="Nick", planet="Earth", galaxy="Milki way", num=123456)

def black_hole_mix(var_1, var_2=3, *args, **kwargs):

    print("var_1",var_1)
    print("var_2", var_2)
    for i in args:
        print("args", i)
    for key, value in kwargs.items():
        print("dict", key, value)

black_hole_mix(0, 5,6, "None", "adress", 2*5, name="Nick", planet="Earth", galaxy="Milki way", num=123456)

#------------------------------------------распаковка

list_1 = [60, 2]

def way(v,t):
    way1 = v * t
    print(way1)

way(100, 30)
way(*list_1)
print(list_1)
print(*list_1)

list_1 = "60", 2

def way(v,t):
    way1 = v * t
    print(way1)

way(*list_1)
print(*list_1)

dict_1 = {"var_3":3, "var_4":4}
list_1 = [2]

def func(var_1, var_2, var_3, var_4):
    print(var_1, var_2, var_3, var_4)

func(1,*list_1,**dict_1)

dict_1 = {"var_1":1,"var_2":2,"var_3":3, "var_4":4}

def func(var_1, var_2, var_3, var_4):
    print(var_1, var_2, var_3, var_4)

func(**dict_1)



