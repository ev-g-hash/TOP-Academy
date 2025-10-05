import telebot
import secrets
import string

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Привет! Я бот генерации паролей напиши /generate или нажми /generate.")


@bot.message_handler(commands=['generate'])
def generate_password(message):    
    msg = bot.reply_to(message, "Введите длину пароля:")
    bot.register_next_step_handler(msg, process_password_length)

def process_password_length(message):
    try:       
        password_length = int(message.text)
        
        if password_length < 1:
            raise ValueError
       
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
       
        bot.reply_to(message, f"Вот твой новый пароль: {password}")

    except ValueError:        
        bot.reply_to(message, "Некорректная длина пароля.nВведите целое число от 1.")
        generate_password(message)

bot.polling()
