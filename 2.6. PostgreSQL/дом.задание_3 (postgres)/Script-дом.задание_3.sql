--1. Выбрать все данные из таблицы customers
select * 
from customers c;

--2. Выбрать все записи из таблицы customers, но только колонки "имя контакта" и "город"
select 
c.contact_name, c.city 
from customers c;

--3. Выбрать все записи из таблицы orders, но взять две колонки: идентификатор заказа и колонку,
--значение в которой мы рассчитываем как разницу между датой отгрузки и датой формирования заказа.
-- shipped_date - дата отгрузки
-- order_date - дата формирования заказа
select 
o.order_id, 
age(o.shipped_date, o.order_date) as date_difference 
from orders o;

--4. Выбрать все заказы из стран France, Austria, Spain
select *
from orders o
where o.ship_country in ('France', 'Austria', 'Spain');

--5. Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
-- shipped_date - дата отгрузки
select *
from orders o  
order by o.required_date desc, o.shipped_date asc;

--6. Выбрать минимальную цену среди тех продуктов, которых в продаже более 30 единиц. 
-- unit_price - цена за единицу товара
-- units_in_stock - единиц на складе
select min(p.unit_price)
from products p
where units_in_stock > 30;

--7. Выбрать максимальное кол-во единиц товара среди тех продуктов, цена которых больше 30.
-- units_in_stock - единиц на складе
-- unit_price - цена за единицу товара
select max(p.units_in_stock)
from products p
where p.unit_price > 30;



	




























