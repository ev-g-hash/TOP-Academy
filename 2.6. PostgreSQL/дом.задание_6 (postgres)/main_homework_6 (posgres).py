
import psycopg2
print()

# создание базы данных для управления клиентами
from modul import bd
bd()
print()

# таблица с клиентами
from modul import users
users()
print()

# таблица с телефонами клиентов
from modul import phones
phones()
print()

# внесение данных в таблицу клиентов
from modul import users_info
users_info()
print()

# внесение данных в таблицу телефоны клиентов
from modul import phones_info
phones_info()
print()

# изменение данных о клиенте
from modul import user_change
user_change()
print()

# удалeние телефона для существующего клиента
from modul import phone_delete
phone_delete()
print()

# удаление существующего клиента
from modul import user_delete
user_delete()
print()

# нахождение клиента по его данным (имени, фамилии, email-у или телефону)
from modul import user_search
user_search()

