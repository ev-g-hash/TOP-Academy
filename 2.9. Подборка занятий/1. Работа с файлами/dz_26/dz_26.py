"""
Задание 1
Дан текстовый файл. Необходимо создать новый файл,
в который требуется переписать из исходного файла все
слова, состоящие не менее чем из семи букв.
"""
print("\nЗадание 1 - информация записана в файл (my_output_1.txt) исходный файл(my_input_1.txt)")

my_input_1 = "my_input_1.txt"
my_output_1 = "my_output_1.txt"

with (open(my_input_1, "r", encoding="utf-8") as infile,
      open(my_output_1, "w", encoding="utf-8") as outfile):
    for line in infile:
        line = line.split()
        for i in line:
            if len(i) > 7:
                outfile.write(" ")
                outfile.write(i)

"""
Задание 2
Дан текстовый файл. Необходимо переписать его
строки в другой файл. Порядок строк во втором файле
должен совпадать с порядком строк в заданном файле.
"""
print("\nЗадание 2 - информация записана в файл (my_output_2.txt) исходный файл(my_input_2.txt)")

my_input_2 = "my_input_2.txt"
my_output_2 = "my_output_2.txt"

with (open(my_input_2, "r", encoding="utf-8") as infile,
      open(my_output_2, "w", encoding="utf-8") as outfile):
    for line in infile:
        outfile.write(line)


"""
Задание 3
Дан текстовый файл. Необходимо переписать его
строки в другой файл. Порядок строк во втором файле
должен быть обратным по отношению к порядку строк
в заданном файле.
"""
print("\nЗадание 3 - информация записана в файл (my_output_3.txt) исходный файл(my_input_3.txt)")

my_input_3 = "my_input_3.txt"
my_output_3 = "my_output_3.txt"

with (open(my_input_3, "r", encoding="utf-8") as infile,
      open(my_output_3, "w", encoding="utf-8") as outfile):
    y = []
    for line in infile:
        x = line.split()
        y.append(x)
        z = y[::-1]
    for i in z:
        outfile.write("\n")
        outfile.write(" ".join(i))


"""
Задание 4
Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************), 
поместив ее после последней
из строк, в которых нет запятой. Если таких строк нет,
то новая строка должна быть добавлена после всех строк
имеющегося файла. Результат записать в другой файл
"""
print("\nЗадание 4 - информация записана в файл (my_output_4.txt) исходный файл(my_input_4.txt)")

my_input_4 = "my_input_4.txt"
my_output_4 = "my_output_4.txt"

with (open(my_input_4, "r", encoding="utf-8") as infile,
      open(my_output_4, "wt", encoding="utf-8") as outfile):
    count = 0
    for line in infile:
        line_1 = line.split()
        if "," in line:
            outfile.write("\n")
            outfile.write(" ".join(line_1))
        else:
            count += 1
            outfile.write("\n")
            outfile.write(" ".join(line_1))
            outfile.write("\t************")

with (open(my_output_4, "at", encoding="utf-8") as outfile):
    if count == 0:
        outfile.write("\n")
        outfile.write("************")

"""
Задание 5
Дан текстовый файл. Подсчитать количество слов,
начинающихся с символа, который задаёт пользователь.
"""
print("\nЗадание 5 исходный файл для подсчёта слов (my_file_5.txt)")

x_5 = input("введите символ или букву (например ( п ): ")

my_file_5 = open("my_file_5.txt", encoding="utf-8")
y_5 = my_file_5.read().lower().split()
count_5 = 0
for i in y_5:
    if i[0] == x_5:
        count_5 +=1
        print(i)

print(f"количество слов {count_5}")

"""
Задание 6
Дан текстовый файл. Переписать в другой файл все его
строки с заменой в них символа * на символ & и наоборот.
"""
print("\nЗадание 6 информация записана в файл (my_output_6.txt) - исходный файл (my_input_6.txt)")

my_input = "my_input_6.txt"
my_output = "my_output_6.txt"

with (open(my_input, "r", encoding="utf-8") as infile,
      open(my_output, "w", encoding="utf-8") as outfile):
    for line in infile:
        for l in line:
            if l == "*":
                l = "&"
            elif l == "&":
                l = "*"
            outfile.write(l)


"""
Задание 7 Задание 8 (одинаковые)
Дан массив строк. Записать их в файл, расположив
каждый элемент массива на отдельной строке с сохранением порядка.
"""
print("\nЗадание 7 Задание 8 (одинаковые) - информация записана в файл file_7.txt")

my_mas = ["Дан массив строк", "Записать их в файл", "расположив", "каждый элемент массива",
          "на отдельной строке", "с сохранением порядка"]
print(my_mas)

file = open("file_7.txt", "wt", encoding="utf-8")

for i in my_mas:
    file.write("\n")
    file.write(i)


"""
Задание 9
Дан текстовый файл. Подсчитать количество символов в нём.
"""
print("\nЗадание 9 исходный файл (text_9.txt)")

count_symbol = 0

file = "text_9.txt"
with open(file, encoding="utf-8") as files:
    for line in files:
        x = line.split()
        for word in x:
            for symbol in word:
                count_symbol += 1

print(f"количество символов ---- {count_symbol}")

"""
Задание 10
Дан текстовый файл. Подсчитать количество строк
в нём.
"""
print("\nЗадание 10 исходный файл (text_10.txt)")

count_str = 0

file = "text_10.txt"
with open(file, encoding="utf-8") as files:

    for line in files:
        count_str +=1
        x = line.split()

print(f"количество строк ------- {count_str}")

















