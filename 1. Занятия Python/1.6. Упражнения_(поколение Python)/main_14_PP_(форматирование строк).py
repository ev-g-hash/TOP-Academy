"""
Форматирование строк
"""

# name = 'Leto Atreides'
# planet = 'Caladan'
# text = 'Duke {1} is the ruler of the planet {0}.'.format(planet, name)
#
# print(text)

# name = 'Dune'
# text = f'The novel "{name}" was published in 1965 by Frank Herbert.'
#
# print(text)

# name = 'Imperium'
# text = 'For the {name} spice is used by the navigators to find safe paths between the stars.'
#
# print(text)

"""
Используя метод format(), дополните приведённый ниже код так, чтобы он вывел текст:

In 2010, someone paid 10k Bitcoin for two pizzas.
"""
# a = 2010
# b = "10k"
# c = "Bitcoin"
#
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(a, b, c)
#
# print(s)

#--------------------------
# s = 'In {0}, someone paid {1} {2} for two pizzas.'
#
# print(s.format(2010, '10k', 'Bitcoin'))


"""
Используя f-строку, дополните приведённый ниже код так, чтобы он вывел текст:

In 2010, someone paid 10K Bitcoin for two pizzas.
"""

# s = f'In {"2010"}, someone paid {"10K"} {"Bitcoin"} for two pizzas.'
# print(s)

#-------------------------------------------
# s1, s2, s3 = '2010', '10K', 'Bitcoin'
# s = f'In {s1}, someone paid {s2} {s3} for two pizzas.'
#
# print(s)


"""
Курсы валют 💹
Вследствие кибератаки на банк «Разбогатеем вместе» сломался алгоритм, 
выводящий курсы валют для определённой даты в мобильном приложении. 
Технический отдел банка просит вас исправить ситуацию и наладить вывод. 
На вход программе подаются следующие значения:

дата (в формате ДД-ММ-ГГГГ)
курс евро (сколько российских рублей стоит 1 евро)
курс юаня (сколько российских рублей стоит 1 юань)
Напишите программу, которая выводит строку, показывающую, сколько российских рублей стоит 
1 евро и 1 юань на указанную дату в формате:

На <дата>: 1€ = <курс евро>₽, 1¥ = <курс юаня>₽
"""
# data = input()
# euro = float(input())
# uan = float(input())
#
# print(f"На {data}: 1€ = {euro}₽, 1¥ = {uan}₽")

"""
Сумма кубов 🆚 Куб суммы
Очень часто студенты "Поколения Python" путают понятия «сумма кубов» и «куб суммы». 
Для того чтобы внести ясность в этот извечный математический вопрос, 
предлагаем вам решить следующую задачу.

На вход программе подаются два целых числа a и b. 
Ваша программа должна посчитать для этих чисел сумму их кубов и 
куб их суммы и вывести результат вычислений в следующем формате:

Для чисел <число a> и <число b>:
  Сумма кубов: <число a>**3 + <число b>**3 = <сумма кубов a и b>
  Куб суммы: (<число a> + <число b>)**3 = <куб суммы a и b>
"""
# a, b = int(input()), int(input())
# print(f"""
# Для чисел {a} и {b}:
#   Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}
#   Куб суммы: ({a} + {b})**3 = {(a + b)**3}""")

"""
(Не) Активное похудение

"""
# # Ввод данных
# day = int(input())
# current_weight = float(input())
#
# # Начальный вес и конечная цель
# initial_weight = 100
# target_weight = 88
#
# # Общее количество дней
# total_days = 60
#
# # Вычисляем дневную норму похудения
# daily_loss = (initial_weight - target_weight) / total_days
#
# # Целевой вес на текущий день
# target_weight_today = initial_weight - daily_loss * day
#
# # Проверяем, выполняется ли план
# if current_weight <= target_weight_today:
#     print("Все идет по плану")
# else:
#     print("Что-то пошло не так")
#
# # Выводим информацию о текущем дне и весе
# print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {
#       current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight_today:.1f} кг")














