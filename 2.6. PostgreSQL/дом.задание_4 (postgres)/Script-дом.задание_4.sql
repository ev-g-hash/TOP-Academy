select c.category_id, c.category_name, c.description, c.picture  
from categories c; 
-- категории
-- c.category_id - идентификатор категории
-- c.category_name - название категории
-- c.description - описание
-- c.picture - изображение;

select ccd.customer_id, ccd.customer_type_id  
from customer_customer_demo ccd; 
-- пользователь_демо
-- ccd.customer_id - идентификатор клиента
-- ccd.customer_type_id - идентификатор_типа клиента;

select cd.customer_desc, cd.customer_type_id  
from customer_demographics cd;
-- демографические данные клиентов
-- cd.customer_desc - пользователь_desc
-- cd.customer_type_id - идентификатор_типа клиента;

select c.address, c.city, c.company_name, c.contact_name, c.contact_title
, c.country, c.customer_id, c.fax, c.phone, c.postal_code, c.region  
from customers c;
-- клиенты
-- c.address - адрес
-- c.city - город
-- c.company_name - название компании
-- c.contact_name - имя контакта
-- c.contact_title - контактный_титл
-- c.country - страна;

select et.employee_id, et.territory_id  
from employee_territories et;
-- служащие_территории
-- et.employee_id - идентификатор сотрудника_id
-- et.territory_id - идентификатор территории

select e.extension, e.address, e.birth_date, e.city, e.country, e.employee_id, e.first_name
, e.hire_date, e.home_phone, e.last_name, e.notes, e.photo, e.photo_path, e.postal_code 
, e.region, e.reports_to, e.title, e.title_of_courtesy 
from employees e;
-- служащие
-- e.extension - e.расширение
-- e.addres - e.адреса
-- e.birth_date - e.дата рождения
-- e.city - e.город
-- e.country - страна
-- e.employee_id - e.идентификатор сотрудника_id
-- e.first_name - e.имя-отчество
-- e.hire_date - e.дата приема на работу
-- e.home_phone - e.домашний телефон
-- e.last_name - e.фамилия
-- e.notes - e.примечания
-- e.photo - фотография
-- e.photo_path - e.путь к фотографии
-- e.postal_code - e.почтовый индекс
-- e.region - e.регион
-- e.reports_to - e.отчеты для
-- e.title - e.название
-- e.title_of_courtesy - e.вежливое название

select od.discount, od.order_id, od.product_id, od.quantity, od.unit_price 
from order_details od;
-- детали заказа
-- od.discount - дополнительная скидка
-- od.order_id - od.идентификатор заказа
-- od.product_id - od.идентификатор продукта_id
-- od.quantity - наружное количество
-- od.unit_price - цена за единицу измерения

select o.customer_id, o.employee_id, o.freight, o.order_date, o.order_id, o.required_date, o.ship_address 
, o.ship_city, o.ship_country, o.ship_name, o.ship_postal_code, o.ship_region, o.ship_via, o.shipped_date 
from orders o;
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

select p.category_id, p.discontinued, p.product_id, p.product_name, p.quantity_per_unit, p.reorder_level 
, p.supplier_id, p.unit_price, p.units_in_stock, p.units_on_order
from products p;
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

select r.region_description, r.region_id  
from region r;
-- region - область
-- r.region_description - описание региона
-- r.region_id - идентификатор региона

select s.company_name, s.phone, s.shipper_id 
from shippers s;
-- shippers - грузоотправители
-- s.phone - телефон
-- s.shipper_id - идентификатор грузоотправителя

select s.address, s.city, s.company_name, s.contact_name, s.contact_title, s.country, s.fax 
, s.homepage, s.phone, s.postal_code, s.region, s.supplier_id, s.
from suppliers s;
-- поставщики
-- s.address - адрес
-- s.city - город
-- s.company_name - имя компании
-- s.contact_name - контактное имя
-- s.contact_title - контактный заголовок
-- s.countr - страна
-- s.fax - факс
-- s.homepage - домашняя страница
-- s.phone - телефон
-- s.postal_code - почтовый индекс
-- s.region - область
-- s.supplier_id - идентификатор поставщика

select t.region_id, t.territory_description, t.territory_id 
from territories t;
-- территории
-- t.territory_description - описание территории
-- t.territory_id - идентификатор территории

select us.state_abbr, us.state_id, us.state_name, us.state_region 
from us_states us;
-- государства США
-- us.state_abbr - абревиатура государства
-- us.state_id - идентификатор состояния
-- us.state_name - название состояния
-- us.state_region - государственный регион

--**************************************************************************************************************

--1. Выбрать все записи заказов в которых наименование страны отгрузки начинается с 'U'
-- заказы
-- o.ship_country - страна отправления
select *
from orders o 
where left (o.ship_country, 1) = 'U'; 

--2. Выбрать записи заказов (включить колонки идентификатора заказа, идентификатора заказчика, веса и страны отгузки), 
--которые должны быть отгружены в страны имя которых начинается с 'N', отсортировать по весу (по убыванию)
--и вывести только первые 10 записей.

select o.order_id, o.customer_id, o.freight, o.ship_country
from orders o
where left (o.ship_country, 1) = 'N'
order by o.freight desc
limit 10;

--3. Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
select e.first_name, e.last_name, e.home_phone, e.region
from employees e
where e.region is NULL;

--4. Подсчитать кол-во заказчиков регион которых известен
select count(*)
from customers c 
where c.region is not null;

--5. Подсчитать кол-во поставщиков в каждой из стран и отсортировать результаты группировки по убыванию кол-ва
select s.country, count(*)
from suppliers s
group by s.country 
order by s.country desc;

--6. Найти заказчиков и обслуживающих их заказы сотрудников таких, что и заказчики и сотрудники из города London, 
--а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.

select c.company_name, concat(e.first_name, ' ', e.last_name)
from orders o
join customers c using(customer_id)
join employees e using(employee_id)
join shippers s on o.ship_via = s.shipper_id
where c.city = 'London' and e.city = 'London' and s.company_name = 'Speedy Express';


--7. Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, 
--которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, 
--имя контакта поставщика и его телефонный номер.

select s.contact_name, s.phone
from products p 
join categories c using(category_id)
join suppliers s using(supplier_id)
where c.category_name in ('Beverages', 'Seafood') and p.discontinued = 0 and p.units_in_stock < 20
order by p.units_in_stock;

--8. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.

select c.contact_name, o.order_id
from customers c 
left join orders o using(customer_id)
where o.order_id is null;




























