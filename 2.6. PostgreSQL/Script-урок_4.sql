--1. Выбрать все уникальные города в которых "зарегестрированы" заказчики
select distinct c.city    
from customers c
where c.contact_name is not NULL;
-- клиенты
-- c.address - адрес
-- c.city - город
-- c.company_name - название компании
-- c.contact_name - имя контакта
-- c.contact_title - контактный_титл
-- c.country - страна;

----------------------------------------------------------------------------------------------------
--2. Выбрать все уникальные сочетания городов и стран в которых "зарегестрированы" заказчики
select distinct c.city, c.country    
from customers c
where c.contact_name is not NULL;
-- клиенты
-- c.address - адрес
-- c.city - город
-- c.company_name - название компании
-- c.contact_name - имя контакта
-- c.contact_title - контактный_титл
-- c.country - страна;
-----------------------------------------------------------------------------------------------------
--3. Посчитать кол-во заказчиков
select count(*)
from customers c
where c.company_name is not null;
-- клиенты
-- c.address - адрес
-- c.city - город
-- c.company_name - название компании
-- c.contact_name - имя контакта
-- c.contact_title - контактный_титл
-- c.country - страна;

----------------------------------------------------------------------------------------------------
--4. Выбрать максимальное кол-во единиц товара среди тех продуктов, цена которых больше 30.
select MAX(p.units_in_stock)
from products p
where p.unit_price > 30;
-- продукты
-- p.category_id - категория
-- p.discontinued - прекращено
-- p.product_id - продукт
-- p.product_name - название продукта
-- p.quantity_per_unit - количество на единицу
-- p.reorder_level - уровень повторного порядка
-- p.supplier_id - поставщик
-- p.unit_price - цена за единицу товара
-- p.units_in_stock - единицы в наличии
-- p.units_on_order - единицы по заказу

--проверка
select p.units_in_stock
from products p
where p.unit_price > 30;

------------------------------------------------------------------------------------------------------------------------
--5. Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
select avg(o.required_date - o.order_date)
from orders o
where o.ship_country = 'USA'; 
-- заказы
-- o.customer_id - o.идентификатор клиента
-- o.employee_id - o.идентификатор сотрудника_id
-- o.freight - груз
-- o.order_date - o.дата заказа
-- o.order_id - o.идентификатор заказа
-- o.required_date - o.требуемая дата
-- o.ship_address - o.адрес отправления
-- o.ship_city - город отправления
-- o.ship_country - o.страна отправления
-- o.ship_name - имя отправителя
-- o.ship_postal_code - o.почтовый код отправления
-- o.ship_region - o.регион отправления
-- o.ship_via - отправление через
-- o.shipped_date - o.дата отправления

-----------------------------------------------------------------------------------------------------------------
--6. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
select c.contact_name, o.order_id
from customers c 
left join orders o using(customer_id)
where o.order_id is null;

--------------------------------------------------------------------------------------------------------------------
--7. Переписать предыдущий запрос, использовав симметричный вид джойна (подсказка: речь о LEFT и RIGHT).
select c.contact_name, o.order_id
from customers c 
left join orders o using(customer_id)
where o.order_id is null;

--*******************************************************************************************************



