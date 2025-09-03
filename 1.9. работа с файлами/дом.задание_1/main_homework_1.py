"""
Задание 1: Чтение файла
Напишите программу, которая читает текстовый файл input.txt и выводит на экран
количество строк, слов и символов в этом файле.
"""
print("\nЗадание 1: Чтение файла: ")

count_str = 0
count_word = 0
count_symbol = 0

file = "input.txt"
with open(file, encoding="utf-8") as files:

    for line in files:
        count_str +=1
        print(line.split())
        x = line.split()

        for word in x:
            count_word += 1

            for symbol in word:
                count_symbol += 1

print(f"количество строк ------- {count_str}")
print(f"количество слов -------- {count_word}")
print(f"количество символов ---- {count_symbol}")

"""
Задание 2: Запись в файл
Создайте программу, которая запрашивает у пользователя несколько строк текста
(например, имя и возраст) и записывает эти данные в файл output.txt.
Каждая запись должна быть на новой строке.
"""
print("\nЗадание 2: Запись в файл:")

files = open("output.txt", "a")
my_name = input("Введите ваше имя: ")
files.write(f"\n{my_name}")
my_age = input("Введите ваш возраст: ")
files.write(f"\n{my_age}")

files = open("output.txt")
print(files.read())
files.close()

"""
Задание 3: Копирование файла
Напишите программу, которая копирует содержимое одного текстового файла в другой.
Имя исходного файла и имя целевого файла должны задаваться пользователем.
"""
print("\nЗадание 3: Копирование файла: ")

my_input = input("Введите файл откуда надо скопировать текст (my_input.txt): ")
my_output = input(f"""Введите файл куда надо скопировать текст,
если такого файла не существует файл создастся автоматически (my_output.txt): """)

with open(my_input, "r") as infile, open(my_output, "w") as outfile:
    for line in infile:
        outfile.write(line)
    print(f"\nинформация скопирована из {my_input} в {my_output}")