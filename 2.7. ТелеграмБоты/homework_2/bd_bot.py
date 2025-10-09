import telebot
import sqlite3


bot = telebot.TeleBot('TOKEN')

name = None
surname = None
email = None

#**************************************************************************************************
#--------------------------------------------создание бд-------------------------------------------
#**************************************************************************************************

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bd_users.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), surname varchar(50), email varchar(50), fhone varchar(50))')
    conn.commit()
    cur.close
    conn.close

    bot.send_message(message.chat.id, 'Привет, я бот обработки и хранения данных пользователя')
    
    markup = telebot.types.InlineKeyboardMarkup()   
    bot.send_message(message.chat.id, 'зарегистрировать пользователя /registration', reply_markup=markup)    
    bot.send_message(message.chat.id, 'нажми /search для поиска пользователя', reply_markup=markup)
    bot.send_message(message.chat.id, 'нажми /delete для удаления пользователя', reply_markup=markup)
    bot.send_message(message.chat.id, 'нажми /change для изменения данных пользователя', reply_markup=markup)

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список зарегистрированных пользователей', callback_data='users'))    
    bot.send_message(message.chat.id, 'Пользователи', reply_markup=markup)
#**************************************************************************************************
#-------------------------------------регистрация пользователя-------------------------------------
#**************************************************************************************************

@bot.message_handler(commands=['registration'])
def user_reg(message):
    bot.send_message(message.chat.id, 'Напиши имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Напиши фамилию')
    bot.register_next_step_handler(message, user_surname)

def user_surname(message):
    global surname
    surname = message.text.strip()
    bot.send_message(message.chat.id, 'Напиши email')
    bot.register_next_step_handler(message, user_email)

def user_email(message):
    global email
    email = message.text.strip()    
    bot.send_message(message.chat.id, 'Напиши телефон')
    bot.register_next_step_handler(message, user_fhone)

def user_fhone(message):
    fhone = message.text.strip()

    conn = sqlite3.connect('bd_users.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, surname, email, fhone) VALUES ('%s', '%s', '%s', '%s')" % (name, surname, email, fhone))
    conn.commit()
    cur.close
    conn.close

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список зарегистрированных пользователей', callback_data='users'))    
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)

#**************************************************************************************************
#-------------------------------------вывод всех пользователей ------------------------------------
#************************************************************************************************** 
  
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    conn = sqlite3.connect('bd_users.sql')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ''

    for user in users:
        info += f'имя: {user[1]}, фамилия: {user[2]}, email: {user[3]}, телефон: {user[4]}\n'

    bot.send_message(call.message.chat.id, info)
    
    markup = telebot.types.InlineKeyboardMarkup()   
    bot.send_message(call.message.chat.id, 'зарегистрировать снова нажми /registration', reply_markup=markup)    
    bot.send_message(call.message.chat.id, 'нажми /search для поиска пользователя', reply_markup=markup)
    bot.send_message(call.message.chat.id, 'нажми /delete для удаления пользователя', reply_markup=markup)
    bot.send_message(call.message.chat.id, 'нажми /change для изменения данных пользователя', reply_markup=markup)

    cur.close
    conn.close

#**************************************************************************************************
#-------------------------------------поиск пользователя по имени ---------------------------------
#************************************************************************************************** 

@bot.message_handler(commands=['search'])
def user_search(message):
    msg = bot.send_message(message.chat.id, 'Напиши имя пользователя для поиска')
    bot.register_next_step_handler(msg, process_user_search)
    
def process_user_search(message):
    try:
        user_name = message.text.strip()
        conn = sqlite3.connect('bd_users.sql')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()   
        info = ''
        for user in users:
            if user[1] == user_name:
                info += f'имя: {user[1]}, фамилия: {user[2]}, email: {user[3]}, телефон: {user[4]}\n'
        bot.send_message(message.chat.id, info)                   
    except:
        bot.send_message(message.chat.id, "Пользователь не найден")

    cur.close
    conn.close

    markup = telebot.types.InlineKeyboardMarkup() 
    bot.send_message(message.chat.id, 'зарегистрировать снова нажми /registration', reply_markup=markup)    
    bot.send_message(message.chat.id, 'нажми /search для поиска пользователя', reply_markup=markup)
    bot.send_message(message.chat.id, 'нажми /delete для удаления пользователя', reply_markup=markup)
    bot.send_message(message.chat.id, 'нажми /change для изменения данных пользователя', reply_markup=markup)

#**************************************************************************************************
#-------------------------------------удаление пользователя ---------------------------------
#************************************************************************************************** 

@bot.message_handler(commands=['delete'])
def user_delete(message):
    msg = bot.send_message(message.chat.id, 'Напиши имя пользователя для удаления')
    bot.register_next_step_handler(msg, process_user_delete)
    
def process_user_delete(message):
    try:
        user_name = message.text
        conn = sqlite3.connect('bd_users.sql')
        cur = conn.cursor()
        sq_delete = """DELETE FROM users WHERE name = ?"""
        cur.execute(sq_delete, (user_name, ))           
        conn.commit() 
        conn.close() 
        bot.reply_to(message, "Пользователь успешно удален")                      
    except:
        bot.reply_to(message, "Произошла ошибка попробуйте заново") 

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список зарегистрированных пользователей', callback_data='users'))    
    bot.send_message(message.chat.id, 'Пользователи', reply_markup=markup)

#**************************************************************************************************
#-------------------------------------изменение пользователя ---------------------------------
#************************************************************************************************** 

@bot.message_handler(commands=['change'])
def user_delete(message):
    msg = bot.send_message(message.chat.id, 'Напиши имя пользователя и номер телефона для изменения через пробел (например, коля 9999):')
    bot.register_next_step_handler(msg, process_user_change)
    
def process_user_change(message):
    try:
        name, fhone = message.text.split()
        fhone = str(fhone)
        conn = sqlite3.connect('bd_users.sql')
        cur = conn.cursor()
        sq_update = """UPDATE users SET fhone = ? WHERE name = ?"""
        cur.execute(sq_update, (fhone, name))           
        conn.commit() 
        conn.close() 
        bot.reply_to(message, "Пользователь успешно изменён")                      
    except:
        bot.reply_to(message, "Произошла ошибка попробуйте заново") 
        
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список зарегистрированных пользователей', callback_data='users'))    
    bot.send_message(message.chat.id, 'Пользователи', reply_markup=markup)

    

bot.polling(non_stop=True)