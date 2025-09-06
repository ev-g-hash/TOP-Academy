"""
Коды PostgreSQL
"""

"""
----------------------------------------------------- Скрипт создания таблицы Postgres

CREATE TABLE IF NOT EXISTS my_schema.books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    author VARCHAR(50),
    price DECIMAL(8, 2),
    stock INTEGER
);

-----------------------------------------------------------Заполнение данными Postgres
INSERT INTO my_schema.books (title, author, price, stock)
VALUES
    ('1984', 'Джордж Оруэлл', 15.99, 20),
    ('Гордость и предубеждение', 'Джейн Остин', 12.99, 30),
    ('Мастер и Маргарита', 'Михаил Булгаков', 19.99, 15),
    ('Война и мир', 'Лев Толстой', 29.99, 10),
    ('Граф Монте-Кристо', 'Александр Дюма', 24.99, 25),
    ('Ромео и Джульетта', 'Уильям Шекспир', 9.99, 40),
    ('Анна Каренина', 'Лев Толстой', 25.99, 12),
    ('Дон Кихот', 'Мигель де Сервантес', 22.99, 18),
    ('Идиот', 'Фёдор Достоевский', 16.99, 28),
    ('Собака Баскервилей', 'Артур Конан Дойл', 14.99, 32);
    
-------------------------------------------------------------------------
CREATE TABLE users (
    id INTEGER,                 // Только целые числа
    name VARCHAR(50),           // Только текстовые символы
    email VARCHAR(100),         // Строго формат почты
    age SMALLINT,               // Только числа возраста
    salary NUMERIC(10,2),       // Число с копейками
    registration_date DATE,     // Только дата
    is_active BOOLEAN           // Только true/false
);



-------------------------------------------------------------DBeaver
типы даных

integer - числовое хранение данных
smallint - (-32768 до 32768)
real - 3,141414 (6 знаков после запятой)
double precision (15 знаков после запятой)
char - (строка фиксированной длины)
varchar(100) - (max 100 символов)
text - (строка произвольной длины)
date - (2025-09-06)
time - (16:56:45)
boolean - (True, False)
point - (точку с координатами x,y)

CREATE TABLE - создавать, удалять таблицы




----------------------------DDL создание таблицы

CREATE TABLE public.rrr (
	id serial4 NOT NULL,
	"name" text NULL,
	department int4 NULL,
	salary numeric NULL,
	hare_date date NULL,
	CONSTRAINT rrr_pkey PRIMARY KEY (id)
);

---------------------------DML заполнение таблицы
insert into rrr (name, department, salary)
values ('Alice', 1, 2000.0);

внести изменения
update rrr set salary = 1000;

посмотреть результат
select * from rrr r;

удалить данные
delete from rrr;

-------------------------DCL (назначать права у начальника одни у инженера другие)

-------------------------TCL (транзакции)









"""







