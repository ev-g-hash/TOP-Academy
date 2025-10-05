import telebot
import datetime
import threading

# Создаем объект бота и передаем ему токен нашего бота
bot = telebot.TeleBot('8135889436:AAGSxzqkF7G--ff1cKxrAJAC8MoCGNLst9g')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
# Отправляем сообщение пользователю
    bot.send_message(message.chat.id, 'Привет! Я бот-список дел. Введите /reminder, или нажмите /reminder, и я вам напомню о вашем деле.')

# Обработчик команды /reminder
@bot.message_handler(commands=['reminder'])
def reminder_message(message):
# Запрашиваем у пользователя название напоминания и дату и время напоминания
    bot.send_message(message.chat.id, 'Введите название дела:')
    bot.register_next_step_handler(message, set_reminder_name)

# Функция, которую вызывает обработчик команды /reminder для установки названия напоминания
def set_reminder_name(message):
    user_data = {}
    user_data[message.chat.id] = {'reminder_name': message.text}
    bot.send_message(message.chat.id, 'Введите дату и время, когда вы хотите получить напоминание о вашем деле в формате ГГГГ-ММ-ДД чч:мм:сс.')
    bot.register_next_step_handler(message, reminder_set, user_data)

# Функция, которую вызывает обработчик команды /reminder для установки напоминания
def reminder_set(message, user_data):
    try:
    # Преобразуем введенную пользователем дату и время в формат datetime
        reminder_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        delta = reminder_time - now
    # Если введенная пользователем дата и время уже прошли, выводим сообщение об ошибке
        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, 'Вы ввели прошедшую дату, попробуйте еще раз.')
    # Если пользователь ввел корректную дату и время, устанавливаем напоминание и запускаем таймер
        else:
            reminder_name = user_data[message.chat.id]['reminder_name']
            bot.send_message(message.chat.id, 'Напоминание "{}" установлено на {}.'.format(reminder_name, reminder_time))
            reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [message.chat.id, reminder_name])
            reminder_timer.start()
    # Если пользователь ввел некорректную дату и время, выводим сообщение об ошибке
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели неверный формат даты и времени, попробуйте еще раз.')

# Функция, которая отправляет напоминание пользователю
def send_reminder(chat_id, reminder_name):
    bot.send_message(chat_id, 'Время получить ваше напоминание о вашем деле "{}"!'.format(reminder_name))

# Обработчик любого сообщения от пользователя
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.send_message(message.chat.id, 'Я не понимаю, что вы говорите. Чтобы создать напоминание, введите /reminder.')

# Запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)