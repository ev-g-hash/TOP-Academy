import psycopg2
# ***********************************************************************************************
#                               СОЗДАНИЕ БАЗЫ ДАННЫХ 
# ***********************************************************************************************
def bd():
    print("Создание базы данных")

    conn = psycopg2.connect(dbname="postgres", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()
    conn.autocommit = True

    sql = "CREATE DATABASE bd_info_users"

    cursor.execute(sql)

    print('база данных "bd_info_users" успешно создана')

    cursor.close()
    conn.close()


# *********************************************************************************************** 
#                               СОЗДАНИЕ ТАБЛИЦЫ КЛИЕНТОВ 
# ***********************************************************************************************
def users():    
    print("Создание таблицы с клиентами ")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users " \
    "(user_id SERIAL PRIMARY KEY," \
    "name VARCHAR(50)," \
    "surname VARCHAR(50)," \
    "email VARCHAR(50))")

    conn.commit()
    print('таблица c клиентами "users" успешно создана')

    cursor.close()
    conn.close()

# ***********************************************************************************************
#                               СОЗДАНИЕ ТАБЛИЦЫ ТЕЛЕФОНЫ КЛИЕНТОВ
# ***********************************************************************************************
def phones():
    print("Создание таблицы с телефонами клиентов")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE phones " \
    "(phone_id SERIAL PRIMARY KEY," \
    "user_id INTEGER," \
    "phone VARCHAR(20)," \
    "FOREIGN KEY (user_id) REFERENCES users(user_id))")

    conn.commit()
    print('таблица c телефонами клиентов "phones" создана')

    cursor.close()
    conn.close()

# ***********************************************************************************************
#                               ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ КЛИЕНТОВ
# ***********************************************************************************************
def users_info():
    print("Внесение данных в таблицу клиентов")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    #внесение данных
    users = [('Иван', 'Пупкин', 'pppp@gmail.com'), ('Зина', 'Золотова', ''), ('Ося', 'Митина', '@gmail.com')]

    cursor.executemany("INSERT INTO users (name, surname, email) "
                "VALUES (%s, %s, %s)", users)

    conn.commit()
    print('данные в таблицу "users" внесены')

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    cursor.close()
    conn.close()

# ***********************************************************************************************
#                               ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ ТЕЛЕФОНЫ КЛИЕНТОВ
# ***********************************************************************************************
def phones_info():
    print("Внесение данных в таблицу телефоны клиентов")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    phones = [(1, '+7(999)888-00-00'), (1, '+7(222)444-55-55'), (3, '+7(777)999-44-44')]
    #внесение данных
    cursor.executemany("INSERT INTO phones (user_id, phone) "
                "VALUES (%s, %s)", phones)

    conn.commit()
    print('данные телефонов клиентов внесены')
        
    cursor.execute("SELECT u.surname, p.phone FROM users u JOIN phones p on u.user_id = p.user_id")
    print(cursor.fetchall())

    cursor.close()
    conn.close()

# *********************************************************************************************** 
#                                  ИЗМЕНЕНИЕ ДАННЫХ О КЛИЕНТЕ
# ***********************************************************************************************
def user_change():
    print("Изменение данных о клиенте 'Зина Золотова'")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    #внесение данных
    cursor.execute("UPDATE users " "SET name = 'Зинаида' WHERE name = 'Зина'")
    cursor.execute("UPDATE users " "SET surname = 'Зинаидова' WHERE surname = 'Золотова'")
    cursor.execute("UPDATE users " "SET email = 'zina@gmail.com' WHERE email = ''")

    conn.commit()

    print("изменения клиента 'Зина Золотова' внесены")        
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    cursor.close()
    conn.close()

# *********************************************************************************************** 
#                         УДАЛЕНИЕ ТЕЛЕФОНА ДЛЯ СУЩЕСТВУЮЩЕГО КЛИЕНТА         
# ***********************************************************************************************
def phone_delete():
    print("удаление телефона 'Ивана Пупкина +7(222)444-55-55'")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    #внесение данных
    cursor.execute("DELETE FROM phones " "WHERE phone_id = 2")

    conn.commit()

    print("телефон 'Ивана Пупкина +7(222)444-55-55' удалён")        
    cursor.execute("SELECT u.surname, p.phone FROM users u JOIN phones p on u.user_id = p.user_id")
    print(cursor.fetchall())

    cursor.close()
    conn.close()


# *********************************************************************************************** 
#                         УДАЛЕНИЕ СУЩЕСТВУЮЩЕГО КЛИЕНТА         
# ***********************************************************************************************
def user_delete():
    print("удаление существующего клиента 'Ивана Пупкина'")

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    #внесение данных
    cursor.execute("DELETE FROM phones " "WHERE user_id = 1 ")
    cursor.execute("DELETE FROM users " "WHERE user_id = 1 ")

    conn.commit()

    print("существующий клиент 'Иван Пупкин' удалён")        
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    cursor.close()
    conn.close()

# *********************************************************************************************** 
#           НАХОЖДЕНИЕ КИЕНТА ПО ЕГО ДАННЫМ (ИМЕНИ, ФАМИЛИИ, EMAIL-У или ТЕЛЕФОНУ)
# ***********************************************************************************************
def user_search():    

    conn = psycopg2.connect(dbname="bd_info_users", user='postgres', password='root', host='127.0.0.1')
    cursor = conn.cursor()

    #поиск клиента
    print("Поиск по имени 'Зинаида'")
    cursor.execute("SELECT * FROM users " "WHERE name = 'Зинаида'")
    conn.commit()
    print(cursor.fetchall())

    print("Поиск по фамилии 'Митина'")
    cursor.execute("SELECT * FROM users " "WHERE surname = 'Митина'")
    conn.commit()
    print(cursor.fetchall())
 
    print("Поиск по email 'zina@gmail.com'")
    cursor.execute("SELECT * FROM users " "WHERE email = 'zina@gmail.com'")
    conn.commit()
    print(cursor.fetchall())

    print("Поиск по номеру телефона '+7(777)999-44-44'")
    cursor.execute("SELECT * FROM phones " "WHERE phone = '+7(777)999-44-44'")    
    conn.commit()
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM users " "WHERE user_id = 3")
    conn.commit()
    print(cursor.fetchall())


    cursor.close()
    conn.close()










