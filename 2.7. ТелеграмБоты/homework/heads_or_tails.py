import telebot
import random 

bot = telebot.TeleBot("8205246773:AAGGgqep6sFmN7VEzgXNbhiDj_-_x12kniE") 

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "👋 Привет! Я бот игра Орёл или Решка")
    bot.send_message(message.chat.id, "Выбери Орёл или Решка?") 

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "орел":
        list=["Ура!!! Ты Выиграл", "Увы Ты Проиграл"]
        bot.send_message(message.chat.id, random.choice(list))
    elif message.text.lower() == "решка":
        list=["Ура!!! Ты Выиграл", "Увы Ты Проиграл"]
        bot.send_message(message.chat.id, random.choice(list)) 
    
bot.polling()