select * from categories c;

select * from customer_customer_demo ccd;

select * from customer_demographics cd;

select * from customers c;

select * from employee_territories et;

select * from employees e;

select * from order_details od;

select * from orders o;

select * from products p;

select * from region r;

select * from shippers s;

select * from suppliers s;

select * from territories t;

select * from us_states us;


select product_id, product_name, unit_price * units_in_stock as itogo from products p;

select title from employees e;

select distinct title from employees e;

select distinct (country, title) from employees e;

select count(*) from employees e;

select * from employees e;

select count(distinct country) from employees e;

select company_name, contact_name, phone, country
from customers c
where country = 'USA';

select * from products p
where unit_price > 20;

select count(*) 
from products p 
where unit_price < 20;

select count(*) 
from products p; --проверка

select * from products p 
where p.discontinued = 1;

select * 
from customers c 
where city <> 'Berlin';

select *
from orders o 
where o.order_date >= '1998-03-01';

select *
from products p 
where p.unit_price > 25 and p.units_in_stock > 40;


select *
from orders o 
where o.shipped_date > '1998-04-30' and (o.freight < 75 or o.freight > 150);

select *
from orders o 
where o.freight >= 20 and o.freight <= 40;

select *
from orders o 
where o.freight between 20 and 40;


select count(*)
from orders o 
where o.freight >= 20 and o.freight < 40;

select *
from orders o 
where o.order_date between '1998-03-30' and '1998-04-03';

select *
from orders o  
where o.order_date > '1998-03-30' and o.order_date < '1998-04-03';

select * 
from customers c 
where c.country = 'Mexico' or c.country = 'Germany' or c.country = 'USA' or c.country = 'Canada';


select *
from customers c 
where c.country in ('Mexico', 'Germany', 'USA', 'Canada');

select *
from customers c 
where c.country not in ('Mexico', 'Germany', 'USA', 'Canada');  -- отрицание

select *
from products p 
where p.category_id in (1, 3, 5, 7);

select *
from products p 
where p.category_id not in (1, 3, 5, 7);  -- отрицание

select 
distinct c.country 
from customers c
order by c.country asc;


select 
distinct c.country 
from customers c
order by c.country desc;

select 
distinct c.country, c.city 
from customers c 
order by c.country desc, c.city desc;

select o.ship_city, o.order_date 
from orders o 
where o.ship_city = 'London'
order by o.order_date;

select min(o.order_date)
from orders o  
where o.ship_city = 'London';

select max(o.order_date)
from orders o  
where o.ship_city = 'London';


select o.ship_city, o.order_date 
from orders o 
where o.ship_city = 'London'
order by o.order_date desc;

select AVG(p.unit_price)
from products p  
where p.discontinued <> 1;

select SUM(p.units_in_stock)
from products p 
where p.discontinued <> 1;

select e.last_name, e.first_name 
from employees e 
where e.first_name like 'S%';

select e.last_name, e.first_name 
from employees e 
where e.first_name like '_t%';
















































