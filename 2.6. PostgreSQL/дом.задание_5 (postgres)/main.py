import psycopg2

conn = psycopg2.connect(dbname="postgres", user='postgres', password='root', host='127.0.0.1')

cursor = conn.cursor()

conn.autocommit = True

sql = "CREATE DATABASE test_bd_postgress"

#запрос

cursor.execute(sql)

print('база данных успешно создана')

cursor.close()
conn.close()