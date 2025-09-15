select p.product_name, p.unit_price 
from products p
where p.discontinued <> 1
order by p.unit_price desc 
limit 10;

select o.ship_city, o.ship_region, o.ship_country  
from orders o
where o.ship_region is not null;

select o.ship_country, count(*)
from orders o 
where o.freight > 50
group by ship_country
order by count(*) desc;

select p.category_id , sum(p.units_in_stock)
from products p 
group by p.category_id
order by sum(p.units_in_stock)
limit(5);								

select p.category_id, sum(p.unit_price * p.units_in_stock)
from products p
where p.discontinued <> 1
group by p.category_id 									-- group by формирует одинаковые значения в одну строку
having sum(p.unit_price * p.units_in_stock) > 5000		-- условие
order by sum(p.unit_price * p.units_in_stock) desc;


select p.category_id, sum(p.unit_price * p.units_in_stock) as itogo 
from products p
group by p.category_id;

select p.category_id 
from products p;			

--------------------------------------------------------------

select c.country
from customers c 
union all				--Объединение запросов выводит все
select e.country 
from employees e; 


select c.country
from customers c 
union					--Объединение запросов выводит уникальные
select e.country 
from employees e; 

select distinct c.country  
from customers c 
union all
select distinct e.country 
from employees e;

select c.country  
from customers c 
intersect					-- пересечение (ешё можно добавлять all)
select country 
from suppliers s;


select c.country  
from customers c 
except 		 				-- "кроме" (противоположое intersect) ешё можно добавлять all
select country 
from suppliers s;

---------------- join-----------------------------

select p.product_name, s.company_name, p.units_in_stock 
from products p 
inner join suppliers s on p.supplier_id = s.supplier_id -- supplier единицы измерения на складе
order by p.units_in_stock desc;


select p.supplier_id
from products p; 

select supplier_id 
from suppliers s;   

----------------------------------------------------------

select c.category_name, sum(p.units_in_stock)
from products p 
inner join categories c on p.category_id = c.category_id 
where p.discontinued <> 1
group by c.category_name 
having sum(p.units_in_stock * p.unit_price) > 5000
order by sum(p.units_in_stock * p.unit_price) desc;

--------------------------------------------------------------

select o.order_date, p.product_name, o.ship_country, od.unit_price, od.quantity, od.discount
from orders o 
inner join order_details od on od.order_id = o.order_id 
inner join products p on od.product_id = p.product_id; 

-------------------------------------------------------------

select s.company_name, p.product_name
from suppliers s 
left join products p on p.supplier_id = p.supplier_id; 




