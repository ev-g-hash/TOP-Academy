"""
----------------------------игра кидание монетки (мартингейл)--------------------------
"""
# import random    #библиотека рандом
#
# HEADS = "heads" #орел
# TAILS = "tails" #решка
# COIN_VALUES = [HEADS, TAILS] #список куда добавляются данные
#
# #функция которая определяет бросок монетки
# def flip_coin():
#     return random.choice(COIN_VALUES) #возвращает случайные числа из рандом
# # print(flip_coin()) #проверка бросков
#
# def play_martingale(*, starting_fund: int, min_bet: int, max_bet: int) -> int:
# # описание функции
# # starting_fund - стартовые средства игрока
# # min_bet - минимальная ставка
# # max_bet - максимальная ставка
# # int - количество бросков монет
#     steps_to_loose = 0      #количество шагов до поражения
#     current_funds = starting_fund  #текущие средства игрока в начале равны стартовому
#     current_bet = min_bet  #текущая ставка старт
#
#     while current_funds > 0:       #пока теущие средства больше нуля
#         # print("==========")
#         steps_to_loose += 1         # игра стартанула +1
#         current_funds -= current_bet   # из текущих средств вычитаем текущую ставку
#         # print(f"{current_funds=}, {current_bet=}")
#         flip_coin_value = flip_coin() # в переменную присваиваем функцию кидания монетки
#         if flip_coin_value == HEADS:            #далее пошло условие(развилка)
#             win = current_bet * 2 #фиксируем выигрыш и удваиваем ставку
#             # print(f"{win=}")
#             current_funds += win #увеличиваем текущие средства на (win)
#             current_bet = min_bet #текущая ставка становится минимальной
#         else:                     #если мы проигрываем
#             # print("loose")
#             current_bet *= 2 #текущую ставка увеличиваем вдвое
#             if current_bet > max_bet:  #откат текующая ставка должна стать минимальной
#                 current_bet = min_bet   #присваиваем минимальную ставку
#             if current_bet > current_funds: #если тек.ставка становится больше тек.средств
#                 current_bet = current_funds #тек.ставка = тек.средств
#     return steps_to_loose
#
# # print(play_martingale(starting_fund=100, min_bet=1, max_bet=100))
#
# #cимуляция 100 игроков принты в игре закоментированы
#
# def simulate_martingale_n_players(*, starting_fund: int, min_bet: int, max_bet: int, n_games: int) -> float:
#     total_steps_to_loose = 0
#     for i in range(n_games):
#         step_to_loose = play_martingale(
#             starting_fund=starting_fund,
#             min_bet=min_bet,
#             max_bet=max_bet
#         )
#         total_steps_to_loose += step_to_loose
#     return total_steps_to_loose / n_games
#
# print(
#     simulate_martingale_n_players(
#         n_games=10,
#         starting_fund=100,
#         min_bet=1,
#         max_bet=100
#     )
#     )
##--------------------------------------КОНЕЦ-----------------------------------------------

"""
##------------------------------------угадай число------------------------------------------
"""
# import math
# import random
#
# secret_number = random.randint(1,101)
# attempts = 5
#
# print(f"это программа угадай число.")
#
# while attempts > 0:
#     print(f"попыток {attempts}")
#     attempts = attempts - 1
#
#     user_number = input("введите число от 1 до 100: ")
#     if user_number.isdigit():
#         y = int(user_number)
#         if y > secret_number:
#             print("загаданное число меньше")
#         if y < secret_number:
#             print("загаданное число больше")
#         if y == secret_number:
#             print("вы угадали!")
#             break
#         if attempts == 0:
#             print("вы проиграли")
#     else:
#         print(f"""пожалуйста будьте внимательны, введеное вами значение "{user_number}"
#     не является числом, попробуйте заново """)
#         break
##--------------------------------------КОНЕЦ-----------------------------------------------

"""
---------------------------------угадай число 2------------------------------------------

"Игра Угадай число. Предложить пользователю загадать число от 0 до 100 и
отгадать его следующим способом: каждую итерацию цикла делите диапазон чисел пополам,
записываете результат в N и спрашиваете у пользователя Ваше число > N, < N или == N?.
В зависимости от того, что указал пользователь, уменьшаете диапазон. Начальный диапазон
от 0 до 100, поделили пополаи и получили 50. Если пользователь указал, что его число > 50,
то изменили диапазон на от 51 до 100. И так до те пор, пока пользователь не выберет == N.");
--------------------------------------------------------------------------------------------
"""
# import math
# import random
# print(f"это программа угадай число.")
# print(f"попыток - бесконечно\n")
#
# secret_number = input("введите секретное число (которое надо угадать) от 0 до 10: ")
# attempts = 1
# while attempts <= 3:
#
#     user_number = input("введите число чтобы угадать секретное число: \n")
#     if user_number == "stop":
#         break
#
#     elif user_number > secret_number:
#         print(f"секретное число меньше введёного")
#     elif user_number  < secret_number:
#         print("секретное число больше введёного")
#     elif user_number == secret_number:
#         print("вы угадали!")
#         break
##--------------------------------------КОНЕЦ-----------------------------------------------

"""
----------------------------------------------------------------------------------------
игра упражение квест или акция
----------------------------------------------------------------------------------------
"""
# import random
#
# list_of_question = [
# "Do you have a word that you invented yourself?",
# "Have you ever lied about your age?",
# "What's the biggest joke you've ever made?",
# "Do you have a weird / special talent?",
# "Do you sing in the bathroom?",
# "How do you cheat by trying to avoid helping with the housework?",
# "Are you afraid of ghosts?",
# "Have you ever watered a plant with milk?",
# "Have you ever broken something without telling anyone about it?",
# "If you had 1 minute to quickly get out of the house, what would you take with you?"
# ]
#
# list_of_action = [
# "Can't blink for a minute",
# "Run around the house three times",
# "Hug your letterbox (or tree / lawn decoration) for 20 seconds",
# "Speak with your tongue sticking out",
# "Take an action as the next player to select the Action category",
# "Send someone a message using just your nose",
# "Pretend like you're playing air guitar",
# "Sing a nursery rhyme",
# "Speak and behave like a robot",
# "After everything you say, add the words 'Wow… I'm good!' within the next 15 minutes"
#        ]
# gamer_list = []
#
# def gamers(list):
#     while True:
#         name = input("Введите имя игрока (имя должно содержать более двух букв) –  ")
#         if 0 < len(name) <= 2:
#             continue
#         list.append(str.capitalize(name))
#         if len(list)>=1:
#             need_next_player = input("Добавить игрока (Y - да, N - нет)? – Y/N ")
#
#             if need_next_player == str.lower("y") or need_next_player == str.lower("yes"):
#                 continue
#             else:
#                 break
#
# gamers(gamer_list)
#
# def game(list_of_question, list_of_action, *args):
#     while True:
#         next_step = None
#         for gamer in args:
#             print(gamer)
#             user_choise = input("Вопрос или действие (q - действие, а - action): ")
#             if user_choise == str.lower("q") or user_choise == str.lower("question"):
#                 question_index = random.randint(0, len(list_of_question)-1)
#                 print(list_of_question[question_index])
#                 list_of_question.pop(question_index)
#
#             elif user_choise == str.lower("a") or user_choise == str.lower("action"):
#                 action_index = random.randint(0, len(list_of_action)-1)
#                 print(list_of_action[action_index])
#                 list_of_action.pop(action_index)
#             else:
#                 print("Do and answer")
#                 question_index = random.randint(0,len(list_of_question)-1)
#                 print(list_of_question[question_index])
#                 list_of_question.pop(question_index)
#                 action_index = random.randint(0, len(list_of_action)-1)
#                 print(list_of_action[action_index])
#                 list_of_action.pop(action_index)
#
#             if args[-1] == gamer:
#                 break
#
#         # next_step = input("Next player? – Y/N ")
#         #
#         # if next_step == str.lower("y") or next_step == str.lower("yes"):
#         #     continue
#         # else:
#         #     print("Game is over")
#         #     break
#
#         select = input("New round? – Y/N ")
#
#         if select == str.lower("y") or select == str.lower("yes"):
#             continue
#         else:
#             break
#
# game(list_of_question,list_of_action,*gamer_list)