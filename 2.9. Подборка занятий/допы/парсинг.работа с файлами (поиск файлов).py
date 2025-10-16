"""
работа с файлами
z_i - путь к папке и всем вложенным папкам
z_j - сами папки и наличие других папок в них
z_z - наличие файлов в папках
"""
# import os
#
# z_i = []
# z_j = []
# z_z = []
# for i, j, z in os.walk(r'C:\Users\Евгений\Desktop\пример'):
#     z_i.append(i)
#     z_j.append(j)
#     z_z.append(z)
#
# print(z_i)
# print(z_j)
# print(z_z)

"""
работа с файлами
все адреса к файлам в папке пример основная функция ( os.path.join(adress, i) )
смотри пример
генерация адресов
-------
"""
# import os
#
# spisok = []
# for adress, papka, files in os.walk(r'C:\Users\Евгений\Desktop\пример'):
#     for i in files:
#         spisok.append(os.path.join(adress, i))
# print(spisok)

"""
работа с файлами
все адреса к файлам в папке пример основная функция ( os.path.join(adress, i) )
смотри пример
генерация адресов
записываем в переменую ( у )
например можно отфильтровать через else (например нам нужны только (txt расширение)
смотри пример
-------
"""
# import os
#
# spisok = []
# for adress, papka, files in os.walk(r'C:\Users\Евгений\Desktop\пример'):
#     for i in files:
#         y = os.path.join(adress, i)
#         if ".txt" in y:
#             spisok.append(y)
# print(spisok)

"""
работа с файлами
сортировка по времени
"""
import os
import time

spisok = []
for adress, papka, files in os.walk(r'C:\Users\Евгений\Desktop\пример'):
    for i in files:
        y = os.path.join(adress, i)
        if time.time() - os.path.getctime(y) < 5400:
            spisok.append(y)
print(spisok)












