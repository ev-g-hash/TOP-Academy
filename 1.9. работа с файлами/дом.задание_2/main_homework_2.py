"""
Задача 1: Сериализация объекта Python в JSON
Создайте словарь с информацией о книге (название, автор, год издания) и
сохраните его в файл в формате JSON.
"""
import json

my_file = "my_file.json"

my_dict = {
    "название": "Грокаем алгоритмы",
    "автор": "Адитья Бхаргава",
    "год издания": "2024"
}

with open(my_file, "w", encoding="utf-8") as file:
    file.write(json.dumps(my_dict, ensure_ascii=False, indent=4))

print("\nЗадача 1: Сериализация объекта Python в JSON")
print("информация сохранена my_file.json")
"""
Задача 2: Десериализация JSON в объект Python
Прочитайте JSON-файл, созданный в предыдущей задаче, и преобразуйте его обратно в словарь.
Выведите информацию о книге на экран.
"""
print("\nЗадача 2: Десериализация JSON в объект Python")

with (open(my_file, "r", encoding="utf-8") as file):
    my_dict_1 = json.loads(file.read())

print(my_dict_1)

"""
Задача 3: Работа с массивами в JSON
Создайте список словарей, представляющих несколько книг, и сохраните его в JSON-файл.
Затем прочитайте этот файл и выведите информацию о каждой книге.
"""
print("\nЗадача 3: Работа с массивами в JSON (информация сохранена my_file_list.json) ")

import json

my_file_list = "my_file_list.json"

my_list_dict = [
    {"название": "Грокаем алгоритмы",
    "автор": "Адитья Бхаргава",
    "год издания": "2024"},
    {"название": "Изучаем Python",
     "автор": "Эрик Мэтиз",
     "год издания": "2025"},
    {"название": "Трейдинг основанный на интуиции",
     "автор": "Куртис Фейс",
     "год издания": "2010"},
    {"название": "Непонятное исскуство",
     "автор": "Уилл Гомперц",
     "год издания": "2012"},
]
with open(my_file_list, "w", encoding="utf-8") as file:
    file.write(json.dumps(my_list_dict, ensure_ascii=False, indent=4))

with (open(my_file_list, "r", encoding="utf-8") as file):
    my_list_dict_1 = json.loads(file.read())

for i in my_list_dict_1:
    print(i)

"""
Задача 4: Запись и чтение вложенных структур
Создайте сложную структуру данных (например, словарь с вложенными списками и словарями),
сохраните её в JSON-файл и затем прочитайте обратно.
"""
print("\nЗадача 4: Запись и чтение вложенных структур (информация сохранена my_file_mag.json)")

import json

my_file_mag = "my_file_mag.json"

my_dict_mag = {"Магазин": {
    "Продукты": {
                "Молоко": 10,
                "Хлеб": 15,
                "Мясо": 50
                },
    "Фрукты и овощи": {
                "Клубника": 5,
                "Капуста": 2,
                "Картофель": 30
                },
    "Другое": [
                "Бытовая химия",
                "Алкоголь"
                ]
    }
    }

with open(my_file_mag, "w", encoding="utf-8") as file:
    file.write(json.dumps(my_dict_mag, ensure_ascii=False, indent=4))

with (open(my_file_mag, "r", encoding="utf-8") as file):
    my_dict_mag_1 = json.loads(file.read())

#print(my_dict_mag_1)
for i, j in my_dict_mag_1.items():
    print(i, j)

"""
Задача 5: Запись данных в CSV-файл
Создайте список словарей с информацией о студентах (имя, возраст, курс) 
и сохраните его в CSV-файл.
"""
print("\nЗадача 5: Запись данных в CSV-файл (информация сохранена my_file_stud.csv)")
import csv

my_file_stud = "my_file_stud.csv"

my_dict_stud = [
    {"имя": "Евгений", "возраст": 46, "курс": "питон"},
    {"имя": "Ксения", "возраст": 38, "курс": "дизайнер"},
    {"имя": "Олег", "возраст": 33, "курс": "искуственный интелект"},
    {"имя": "Николай", "возраст": 29, "курс": "менеджер"}
    ]

with open(my_file_stud, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["имя", "возраст", "курс"])

    for item in my_dict_stud:
        writer.writerow(list(item.values()))


"""
Задача 6: Чтение данных из CSV-файла
Прочитайте CSV-файл, созданный в предыдущей задаче, 
и выведите информацию о каждом студенте на экран.
"""
print("\nЗадача 6: Чтение данных из CSV-файла")
with open(my_file_stud, encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows:
        if row == ['имя', 'возраст', 'курс']:
            continue
        print(f"студент - {row}")
"""
Задача 7: Работа с вложенными структурами
Создайте список студентов с их оценками (вложенные списки) и сохраните его в CSV-файл.
Затем прочитайте этот файл и выведите информацию о каждом студенте и его оценках.
"""
print("\nЗадача 7: Работа с вложенными структурами (информация сохранена students.csv)")
import csv

my_file_stud_1 = "students.csv"

my_dict_stud_1 = [
    {"имя": "Евгений", "возраст": 46, "курс": "питон", "оценки": [5,4,5,5,5]},
    {"имя": "Ксения", "возраст": 38, "курс": "дизайнер", "оценки": [4,4,4,5,5]},
    {"имя": "Олег", "возраст": 33, "курс": "Аискуственный интелект", "оценки": [3,4,5,3,5]},
    {"имя": "Николай", "возраст": 29, "курс": "менеджер", "оценки": [3,4,3,3,4]}
    ]

with open(my_file_stud_1, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["имя", "возраст", "курс", "оценки"])

    for item in my_dict_stud_1:
        writer.writerow(list(item.values()))

with open(my_file_stud_1, encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows:
        if row == ['имя', 'возраст', 'курс','оценки']:
            continue
        print(f"студент - {row}")

"""
Задача 8: Фильтрация данных
Прочитайте файл students.csv, отфильтруйте студентов по курсу и сохраните отфильтрованные 
данные в новый CSV-файл.
"""
print("\nЗадача 8: Фильтрация данных (информация сохранена students_new.csv)")


with open("students.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(sorted(reader, key=lambda x : x ["курс"]))
    print(rows)

with open("students_new.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["имя", "возраст", "курс", "оценки"])

    for item in rows:
        writer.writerow(list(item.values()))