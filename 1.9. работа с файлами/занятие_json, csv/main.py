
"""
---------------------------------------------------------------------------------
создание и чтение файла
---------------------------------------------------------------------------------
"""
with open("1.txt", encoding="utf-8") as file:
    str1 = file.read()
print(str1)

with open("1.txt", encoding="utf-8") as file:
    str1 = file.readlines()
    print(str1)

#-----------------------------------------------------------------------мой вариант
with open("1.txt", encoding="utf-8") as file:
    for line in file:
        print(line.split())

"""
JSON - это текстовый формат обмена данных основанных на JS.
используется при передачи и получении данных в сети. API и парсер.

"""

import json

filename = "file.json"
info = {
    "ФИО": "Иванов Иван Иванович",
    "Оценки": {
        "Математика": 4,
        "Физика": 5,
        "Информатика": 5,
    },
    "Хобби": ["Программирование", "Плавание"],
    "Возраст": 14,
    "Дом.Животное": None
}
#----------------------------------------------------------------------запись
with open(filename, "w", encoding="utf-8") as file:
    file.write(json.dumps(info, ensure_ascii=False, indent=4))

#-----------------------------------------------------------------------чтение

with (open(filename, "r", encoding="utf-8") as file):
    info2 = json.loads(file.read())

print(info2)

"""
ensure_ascii=False ----------------- если равен Фолс запись не ASCII, запись как есть 
                                     без преобразования UNICOD
indent ----------------------------- величина отступа для вложенных структур

json.dumps ------------------------- сериализация в формат json
json.loads ------------------------- обратная сериализация (десериализация)
"""
#--------------------------самостоятельно
import json

my_filename = "my_file.json"

my_info = {
    "Обувь":{
        "Обувь зимняя": {
            "Валенки": 3,
            "Унты": 4,
        },
        "Обувь летняя": {
            "макасины": 2,
            "туфли": 4,
        }
    },
    "Одежда": {
        "Зимняя": {
            "Пальто": 1,
            "Шуба": 2,
        },
        "Летняя": {
            "футболка": 10,
            "шорты": 7,
        }
    }
}

with open(my_filename, "w", encoding="utf-8") as file:
    file.write(json.dumps(my_info, ensure_ascii=False, indent=4))

with (open(my_filename, "r", encoding="utf-8") as file):
    info_3 = json.loads(file.read())


print(info_3)

"""
CSV - облегченный формат эксель
CSV - текстовый формат для представления табличных данных
XML - расширяемый язык разметки
YAML - аналог JSON
в примере я переделал словарь на список
"""

import csv

filename = "test.csv"

shop_list = ["картофель","2","100"],["яблоки","3","250"], ["морковь","1","35"]

#запись
with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["наименование", "вес", "цена/кг"])

    for name, values in enumerate(shop_list):
        writer.writerow(values)

    writer.writerow(["мука", "4", "78"])

# чтение
with open(filename, encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)

for row in rows:
    print(row)

"""
Написать программу, которая запрашивает у пользователя имя и возраст и записывает в словарь.
Ввод продолжается до тех пор, пока количество пар(ключ/значение) в словаре не равно 3.
Если пользователь ввел повторное имя, то программа должна вывести соответствующее сообщение.
После окончания ввода данные записываются в файл test.txt в формате json.
"""
import json

dict_person = {}
while len(dict_person) != 3:
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    if name not in dict_person:
        dict_person[name] = age
    else:
        print("существует")

with open("text.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps(dict_person, ensure_ascii=False, indent=4))

"""
Написать программу список дел, которая спрашивает у пользователя значение n, 
после этого запрашивает на ввод n строк различных дел и сохраняет их в список, 
а после записывает значения из списка через одно в файл в одну строку
"""
n = int(input())
todo_list = []
for i in range(n):
    todo_list.append(input())
with open("text.txt", "a") as file:
    for todo in range(0, len(todo_list), 2):
        file.write(todo_list[todo])


"""
CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) — текстовый формат, предназначенный для представления табличных данных. Строка таблицы соответствует строке текста, которая содержит одно или несколько полей, разделенных запятыми. 
В Python работа с CSV-файлами поддерживается стандартным модулем csv

Основные методы:
----------------------------------------------------------------------------------------
csv.reader - Создает и возвращает объект для чтения последовательности из CSV-файла.
Синтаксис:
csv.reader(csvfile, dialect='excel', **fmtparams)
csvfile – итерируемый объект, возвращающий строку на каждой итерации (например, файловый объект в текстовом режиме доступа);
dialect – диалект CSV (набор специальных параметров);
fmtparams – дополнительные настройки (совокупность кавычек, разделителей и т.д.).
-----------------------------------------------------------------------------------------
csv.writer - создает и возвращает объект для записи последовательности в CSV-файл.
Синтаксис:
csv.writer(csvfile, dialect='excel', **fmtparams)
csvfile – любой объект, поддерживающий метод записи write()
dialect – аналогично csv.reader()
fmtparams – аналогично csv.reader()
-------------------------------------------------------------------------------------------
classcvs.DictReader - Создает и возвращает объект для чтения данных из CSV-файла как словаря значений.
Синтаксис:
classcsv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
csvfile – итерируемый объект, возвращающий строку на каждой итерации (например, файловый объект в текстовом режиме доступа)
fieldnames – список наименований столбцов (если не задан, используется первая строка файла).
--------------------------------------------------------------------------------------------
classcsv.DictWriter - Создает и возвращает объект для записи данных как словаря значений в CSV-файл.
classcsv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
csvfile – любой объект, поддерживающий метод записи write()
fieldnames – список наименований столбцов.
------------------------------------------------------------------------------------------
classcsv.Writer
writerow(row) - Записывает последовательность row в CSV-файл.
writerows(rows) - Записывает список последовательностей rows в CSV-файл.
-----------------------------------------------------------------------------------------
classcsv.DictWriter
writeheader() - Записывает в файл заголовки файла, переданные при создании класса.
writerow(row) - Записывает словарь row в CSV-файл.
writerows(rows) - Записывает список словарей rows в CSV-файл.
exceptioncsv.Error - Класс исключения, возбуждаемый при ошибке в работе любой из функций модуля.

Рассмотрим несколько вариантов работы с csv: построчно и запись в словарь
Построчно:
import csv

filename = "test.csv"

shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as file:
   writer = csv.writer(file, quoting=csv.QUOTE_ALL)
   writer.writerow(["Наименование", "Вес", "Цена/кг."])  # Заголовки столбца
   for name, values in sorted(shop_list.items()):
       writer.writerow([name, *values])
   writer.writerow(["мука", "4", "70"])  # Допишем произвольную запись

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as file:
   reader = csv.reader(file)
   rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
   print(row)


В словарь
import csv

filename = "test.csv"
# список покупок
shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
   writer.writeheader()  # Записывает заголовки в файл
   for name, values in sorted(shop_list.items()):
       writer.writerow(dict(name=name, weight=values[0], price=values[1]))

# Чтение файла
rows = []
with open(filename, "r", encoding="utf-8") as file:
   reader = csv.DictReader(file)
   rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

for row in rows:
   print(row)


Учитель: Чтение/запись простых типов (например, чисел или строк) не представляет большого 
труда, однако с увеличением объема информации появляется необходимость эффективно 
сохранять/загружать более сложные структуры данных (например, словари). Кроме того, 
очень часто нам необходимо обмениваться данными между разными модулями, а также между 
приложениями в целом, для чего необходимо иметь возможность удобно обмениваться данными.

Сериализация — процесс перевода какой-либо структуры данных в последовательность битов. 
Десериализация, соответственно обратный процесс.
Чаще всего сериализация используется для сохранения объектов в файлы или передачи их по 
сети.

Одним из вариантов, позволяющий сериализовать/десериализовать данные в Python, 
является использование стандартного модуля pickle, при помощи которого можно сохранять 
любой объект Python в двоичном файле, а затем извлекать его обратно.

Рассмотрим основные возможности pickle.
pickle.dump Сериализует объект obj и записывает его в файл file.

Синтаксис
pickle.dump(obj, file, protocol=None, *, fix_imports=True) 
obj – объект для записи;
file – файловый объект;
protocol – версия формата pickle.

pickle.load - Читает и десериализует содержимое файла file, возвращая созданный объект

Синтаксис
pickle.load(file, *, fix_imports=True, encoding='ASCII', errors='strict')
file – файловый объект.

Рассмотрим небольшой пример
import pickle

filename = "test.txt"

shop_list = {"овощи": ["картофель", "капуста"],
           "бакалея": ["мука"],
           "бюджет": 500}

# Запись в файл
with open(filename, "wb") as file:
   pickle.dump(shop_list, file)  # помещаем объект в файл

# Считываем из хранилища
shop_list_2 = []
with open(filename, "rb") as file:
   shop_list_2 = pickle.load(file)  # загружаем объект из файла
print(shop_list_2)


Если мы посмотрим содержимое текстового файла, мы увидим 


Простота работы с модулем, является явным плюсом, но существуют и минусы использования 
pickle специфичен для Python (не может быть использован, если файл будет читаться с 
использованием других языков программирования); небезопасен (десериализация готовых 
конструкций языка может привести к выполнению ненадежного кода).


2. Решение задач
Задача 1
Написать программу, которая запрашивает у пользователя имя и возраст и записывает в словарь. Ввод продолжается до тех пор, пока количество пар(ключ/значение) в словаре не равно 3. Если пользователь ввел повторное имя, то программа должна вывести соответствующее сообщение. После окончания ввода данные записываются в файл test.txt в формате json. 

Решение
import json

dict_person = {}
while len(dict_person) != 3:
   name = input('Введите имя: ')
   age = input('Введите возраст: ')
   if name not in dict_person:
       dict_person[name] = age
   else:
       print('Данное имя уже существует')

with open('text.txt', "w", encoding="utf-8") as file:
   file.write(json.dumps(dict_person, ensure_ascii=False, indent=4))





Дополнительно
Если на уроке остается время, то ученикам можно предложить начать прорешивать домашнее 
задание. 

Домашняя работа
Задача 1
Написать программу список дел, которая спрашивает у пользователя значение n, после этого 
запрашивает на ввод n строк различных дел и сохраняет их в список, а после записывает 
значения из списка через одно в файл в одну строку 

Решение
n = int(input())
todo_list = []
for i in range(n):
    todo_list.append(input())
with open('example5.txt', 'a') as file:
    for todo in range(0, len(todo_list), 2):
        file.write(todo_list[todo])
"""


"""
https://docs.google.com/document/d/1maHtCF4FQQlmgETPA_kQO-DXjcVWtISK/edit?tab=t.0
"""



