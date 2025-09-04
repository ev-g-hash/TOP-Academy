"""
1) Создайте класс Student с атрибутами name (имя) и grade (оценка).
Переопределите методы сравнения (__eq__, __lt__, __gt__ и др.),
чтобы можно было сравнивать студентов по их оценке.
"""
print("\nЗадание 1 методы сравнения")
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        if self.grade < other.grade:
            return f"У студента - {self.name} наибольшая оценка"

id1 = Student("Василий", 5)
id2 = Student("Николай", 10)


print(id1 < id2)

"""
2) Николаю требуется проверить, возможно ли из представленных отрезков условной
длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""
print("\nЗадание 2 - метод is_triangle()")
class TriangleChecker:
    pass

    def is_triangle(self, a, b, c):
        if a == str(a) or b == str(b) or c == str(c):
            print("Нужно вводить только числа!")
        elif a == 0 or b == 0 or c == 0:
            print("Жаль, но из этого треугольник не сделать")
        elif a == abs(a) and b == abs(b) and c == abs(c):
            print("Ура, можно построить треугольник!")
        elif a != abs(a) or b != abs(b) or c != abs(c):
            print("С отрицательными числами ничего не выйдет!")

id1 = TriangleChecker()
id2 = TriangleChecker()
id3 = TriangleChecker()
id4 = TriangleChecker()

id1.is_triangle(1, 1, 3)
id2.is_triangle(1, 1, -3)
id3.is_triangle(1, 1, "f")
id4.is_triangle(1, 1, 0)

"""
3) Николай – оригинальный человек. 
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: 
имя и возраст. Но на этом он не успокоился. 
Не важно, какое имя передаст пользователь при создании экземпляра, 
оно всегда будет содержать “Николая”. 
В частности - если пользователя на самом деле зовут Николаем, 
то с именем ничего не произойдет, а если его зовут, например, Максим, 
то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, 
даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить 
к экземпляру свойство «отчество» или метод «приветствие», то ничего у такого 
хитреца не получится).
"""
print("\nЗадание 3 класс Nikola")
class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        if object.__getattribute__(self, item) == "Николай":
            return f"Привет {object.__getattribute__(self, item)}"
        else:
            return f"Я не {object.__getattribute__(self, item)}, а Николай"

    # def __setattr__(self, name, value):
    #     if name == "name" and value != "Николай":
    #         raise ValueError(f"Имя не может быть изменено")
    #     else:
    #         super().__setattr__(name, value)



user1 = Nikola("Николай", 38)
user2 = Nikola("Юля", 38)

print(user1.name)
print(user2.name)


















