"""
---------------------------------------------------------------------------------------
найти в словаре ключ с наибольшим значением
(соpтируешь и в конце будет максимум)
-------------------------------------------------------------------------------------
"""
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:1]
#
# print(result)


"""
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются слова, а значениями — количество их вхождений в строку.
"""
# def my_count_keys(input_list):
#     keys_count = {}
#     for i in input_list:
#         if i in keys_count:
#             keys_count[i] += 1
#         else:
#             keys_count[i] = 1
#     return keys_count
#
# str_input = "привет питон люблю питон питон класс".split()
# str_out = my_count_keys(str_input)
#
# print(str_out)

"""
Необходимо объединить два словаря в один, чтобы значения с 
одинаковыми ключами суммировались.
"""
# def my_dict_summ(dict_1, dict_2):
#
#     summ_dict = dict_1.copy()
#
#     for key, value in dict_2.items():
#         if key in summ_dict:
#             summ_dict[key] += value
#         else:
#             summ_dict[key] = value
#
#     return summ_dict
#
# dict_input_1 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 1}
# dict_input_2 = {'до свидание': 1, 'питон': 3, 'люблю': 1, 'класс': 1}
#
# print(my_dict_summ(dict_input_1, dict_input_2))
#
# #----------------------------------------------------------------решение 2
# def my_dict():
#     return {i: dict_1.get(i, 0) + dict_2.get(i, 0) for i in set(dict_1) | set(dict_2)}
#
# dict_1 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 1}
# dict_2 = {'до свидание': 1, 'питон': 3, 'люблю': 1, 'класс': 1}
#
# print(my_dict())

"""
Требуется написать функцию, которая принимает словарь и 
возвращает ключ с максимальным значением.
"""
# def my_dict_max(input_dict):
#     max_key = max(input_dict, key=input_dict.get)
#     return max_key
#
# dict_4 = {'привет': 1, 'питон': 2, 'люблю': 3, 'класс': 4}
# print(my_dict_max(dict_4))
#
# #-----------------------------------------------------------решение2
# def my_dict_max(my_dict_3):
#
#     sorted_my_dict = sorted(my_dict_3.items(), key=lambda elem: elem[1])
#     max_my_dict = sorted_my_dict[-1:]
#
#     return dict(max_my_dict)
#
# dict_3 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 2}
#
# print(my_dict_max(dict_3))

"""
Напишите функцию, которая принимает на вход словарь и значение, 
а затем возвращает список ключей, соответствующих этому значению.
"""
# def my_dict_key(input_dict, value):
#     my_dict_sps_val = [key for key, val in input_dict.items() if val == value]
#     return my_dict_sps_val
#
# dict_input = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
#
# print(my_dict_key(dict_input, 5))

"""
Реализуйте функцию, которая удаляет из словаря все пары ключ-значение, 
где значение меньше заданного порога.
"""
# def my_dict_del_el(input_dict, el):
#     del_el = [key for key, value in input_dict.items() if value <= el]
#     for key in del_el:
#         del input_dict[key]
#     return input_dict
#
# dict_input = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
#
# print(my_dict_del_el(dict_input, 5))

"""
Напишите функцию, которая принимает словарь и ключ, и возвращает True, 
если такой ключ уже существует в словаре, и False в противном случае.
"""
# def my_dict_check_key(input_dict, key):
#     return key in input_dict
#
# dict_input = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
#
# print(my_dict_check_key(dict_input, "привет"))

"""
Напишите функцию, которая принимает на вход два словаря и возвращает список ключей, 
которые присутствуют в обоих словарях.
"""
# def my_dict_key(dict_1, dict_2):
#     common_keys = [key for key in dict_1.keys() if key in dict_2]
#     return common_keys
#
# dict_input_1 = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
# dict_input_2 = {'привет': 5, 'егор': 7, 'вася': 3, 'класс': 6}
#
# print(my_dict_key(dict_input_1, dict_input_2))

"""
Реализуйте функцию, которая обновляет значение по заданному ключу в словаре. 
Если ключ не существует, он должен быть добавлен в словарь.
"""
# def my_dict_update_val(input_dict, key, new_value):
#     input_dict[key] = new_value
#     return input_dict
#
# dict_input_1 = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
#
# print(my_dict_update_val(dict_input_1, "вата", 5))

"""
Напишите функцию, которая принимает на вход словарь и возвращает новый словарь, 
отсортированный по значениям (по возрастанию или убыванию).
"""
# def my_dict_sort(input_dict):
#     sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1])[::-1])
#     return sorted_dict
#
# dict_input = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}
#
# print(my_dict_sort(dict_input))

"""
Напишите функцию, которая принимает на вход словарь, 
содержащий числовые значения, и возвращает среднее значение этих чисел
"""
# def my_dict_sr(input_dict):
#     if len(input_dict) == 0:
#         return 0
#     return sum(input_dict.values()) / len(input_dict)
#
# dict_input = {'привет': 5, 'питон': 5, 'люблю': 5, 'класс': 5}
#
# print(my_dict_sr(dict_input))

"""
Реализуйте функцию для проверки идентичности двух словарей, то есть проверку на то, 
что они содержат одни и те же ключи и значения.
"""
# def my_dict_dict(dict_1, dict_2):
#     return dict_1 == dict_2
#
# dict_input_1 = {'привет': 5, 'питон': 5, 'люблю': 5, 'класс': 5}
# dict_input_2 = {'привет': 5, 'питон': 5, 'люблю': 5, 'класс': 5}
#
# print(my_dict_dict(dict_input_1, dict_input_2))

"""
Напишите функцию, которая принимает на вход словарь и список ключей, 
и возвращает новый словарь, содержащий только указанные ключи.
"""
# def my_dict_lst_key(input_dict, keys_list):
#     my_dict = {key: input_dict[key] for key in keys_list if key in input_dict}
#     return my_dict
#
# dict_input = {'привет': 5, 'питон': 5, 'люблю': 5, 'класс': 5}
# list_input = ['питон', 'класс']
#
# print(my_dict_lst_key(dict_input, list_input))

"""
Реализуйте функцию, которая принимает на вход список словарей и объединяет значения 
с одинаковыми ключами в новом словаре.
"""
# def my_dict_key_val(dict_list):
#     merged_dict = {}
#     for d in dict_list:
#         for key, value in d.items():
#             if key in merged_dict:
#                 merged_dict[key] += value
#             else:
#                 merged_dict[key] = value
#     return merged_dict
#
# dict_input = {'п': 'привет '},{'п': 'питон '},{'л': 'люблю '},{'п': 'питон '},{'п': 'питон '},{'к': 'класс '}
#
# print(my_dict_key_val(dict_input))

"""
Напишите функцию, которая принимает на вход список кортежей (ключ, значение) 
и возвращает словарь, в котором значения группируются по ключам (если поменять
key на value, а value на key то будет группировка по значению).
"""
# def my_dict_group(input_list):
#     group_dict = {}
#     for key, value in input_list:
#         if key in group_dict:
#             group_dict[key].append(value)
#         else:
#             group_dict[key] = [value]
#     return group_dict
#
# dict_input = ('п', 'привет '),('п', 'привет ')
#
# print(my_dict_group(dict_input))

"""
Реализуйте функцию для проверки наличия дубликатов значений в словаре
(возвращает Тру или Фолс если есть одинаковые значения).
"""
# def my_dict_dupl(input_dict):
#     values_set = set()
#     for value in input_dict.values():
#         if value in values_set:
#             return True
#         else:
#             values_set.add(value)
#
#     return False
#
# dict_input = {'привет': 5, 'питон': 3, 'люблю': 2, 'класс': 2}
#
# print(my_dict_dupl(dict_input))

"""
Напишите функцию, которая принимает на вход словарь и возвращает новый словарь, 
в котором ключи и значения поменяны местами.
"""
# def my_dict_r(input_dict):
#     rev_dict = {v: k for k, v in input_dict.items()}
#     return rev_dict
#
# dict_input = {'привет': 5, 'питон': 1, 'люблю': 2, 'класс': 3}
#
# print(my_dict_r(dict_input))

"""
Напишите функцию, которая принимает на вход словарь и возвращает ключ 
с наибольшим значением.
"""
# def find_key_with_max_value(input_dict):
#     if not input_dict:
#         return None
#     max_value = max(input_dict.values())
#     key = [k for k, v in input_dict.items() if v == max_value][0]
#     return key
#
# dict_input = {'привет': 5, 'питон': 1, 'люблю': 2, 'класс': 3}
#
# print(find_key_with_max_value(dict_input))
#
# #----------------------------------------------------------------решение 2
# def my_dict_max(input_dict):
#
#     max_key = max(input_dict, key=input_dict.get)
#
#     return max_key
#
# dict_input_3 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 2}
#
# print("\nЗадача 3 функция: возвращает ключ с максимальным значением: ")
# print(my_dict_max(dict_input_3))

"""
Реализуйте функцию, которая принимает на вход несколько словарей и объединяет их, 
обновляя значения для одинаковых ключей.
"""
# def merge_dictionaries(*dicts):
#     merged_dict = {}
#     for d in dicts:
#         for key, value in d.items():
#             if key in merged_dict:
#                 merged_dict[key] += value
#             else:
#                 merged_dict[key] = value
#     return merged_dict
#
# str_input = {1: 'привет ', 2: 'питон'}
# str_input_1 = {3: 'люблю',1: 'питон'}
# print(merge_dictionaries(str_input, str_input_1))

"""
Напишите функцию, которая принимает на вход словарь и условие, 
а затем возвращает новый словарь, содержащий только те элементы, 
которые удовлетворяют условию, (т.е. если condition чему то равен
или неравен или ещё что-то тогда словарь выводим).
"""
# def my_dict_filter_bool(input_dict, condition):
#     filtered_dict = {k: v for k, v in input_dict.items() if condition == 2}
#     return filtered_dict
#
# str_input = {1: 'привет ', 2: 'питон'}
#
# print(my_dict_filter_bool(str_input, 2))

"""
Реализуйте функцию, которая принимает на вход два списка — один для ключей, 
другой для значений, и возвращает словарь, созданный из этих списков.
"""
# def my_dict_is_lict(keys, values):
#     combined_dict = dict(zip(keys, values))
#     return combined_dict
#
# my_keys = [1,2,3,4,5,6,7]
# my_values = ["a","b","c","d","e","f","g"]
# print(my_dict_is_lict(my_keys, my_values))

"""
Напишите функцию, которая принимает на вход словарь и подстроку, 
а затем возвращает список ключей, у которых значения содержат указанную подстроку
(с числами не работает).
"""

# def my_dict_sps_keys(input_dict, substring):
#     my_keys = [key for key, value in input_dict.items() if substring in value]
#     return my_keys
#
# my_dict = {"g": 'питон', 'п': 'пит'}
#
# print(my_dict_sps_keys(my_dict, 'питон'))

"""
Напишите функцию, которая принимает на вход список словарей и ключ, 
а затем возвращает словарь, содержащий объединенные значения всех списков 
по указанному ключу.
"""
# def merge_values_by_key(dict_list, key):
#     merged_dict = {}
#     for d in dict_list:
#         if d[key] in merged_dict:
#             merged_dict[d[key]].extend(d.values())
#         else:
#             merged_dict[d[key]] = list(d.values())
#     return merged_dict
#
# my_dict_list = {"g": 'питон', 'п': 'пит'},{"g": 'вася', 'п': 'коля'},
#
# print(merge_values_by_key(my_dict_list, 'g'))

"""
Реализуйте функцию, которая принимает на вход словарь с числовыми значениями 
и возвращает разницу между максимальным и минимальным значением.
"""
# def calculate_difference_between_max_and_min(input_dict):
#     values = list(input_dict.values())
#     difference = max(values) - min(values)
#     return difference
#
# dict_input = {'привет': 5, 'питон': 1, 'люблю': 2, 'класс': 3}
#
# print(calculate_difference_between_max_and_min(dict_input))

"""
Напишите функцию, которая принимает на вход список словарей и условие, 
а затем возвращает новый список, содержащий только те словари, удовлетворяющие условию.
"""
# def filter_list_of_dictionaries_by_condition(list_of_dicts, condition):
#     filtered_list = [d for d in list_of_dicts if condition == "a"]
#     return filtered_list
#
# my_dict_list = {"g": 'питон', 'п': 'пит'},{"g": 'вася', 'п': 'коля'}
#
# print(filter_list_of_dictionaries_by_condition(my_dict_list, 'a'))

"""
Напишите функцию, которая принимает на вход слово и возвращает словарь, 
содержащий уникальные буквы слова в качестве ключей и количество их появлений в слове 
в качестве значений.
"""
# def count_unique_letters(word):
#     letter_count = {}
#     for letter in word:
#         if letter in letter_count:
#             letter_count[letter] += 1
#         else:
#             letter_count[letter] = 1
#     return letter_count
#
# my_word = 'питонист'
#
# print(count_unique_letters(my_word))

"""
Реализуйте функцию, которая принимает на вход два словаря и возвращает True, 
если они содержат одинаковые ключи и значения, и False в противном случае.
"""
# def compare_dictionaries(dict1, dict2):
#     return dict1 == dict2
#
# my_dict_1 = {"g": 'питон', 'п': 'пит'}
# my_dict_2 = {"g": 'питон', 'п': 'пит'}
# print(compare_dictionaries(my_dict_1, my_dict_2))

"""
Напишите функцию, которая принимает на вход словарь с числовыми значениями 
и возвращает ключ с минимальным значением.
"""
# def find_key_with_min_value(input_dict):
#     if not input_dict:
#         return None
#     min_value = min(input_dict.values())
#     key = [k for k, v in input_dict.items() if v == min_value][0]
#     return key
#
# dict_input = {'привет': 5, 'питон': 1, 'люблю': 2, 'класс': 3}
#
# print(find_key_with_min_value(dict_input))

"""
Напишите функцию, которая принимает на вход словарь с числовыми значениями 
и возвращает сумму всех значений словаря.
"""
# def calculate_sum_of_values(input_dict):
#     return sum(input_dict.values())
#
# dict_input = {'привет': 5, 'питон': 1, 'люблю': 2, 'класс': 3}
#
# print(calculate_sum_of_values(dict_input))









