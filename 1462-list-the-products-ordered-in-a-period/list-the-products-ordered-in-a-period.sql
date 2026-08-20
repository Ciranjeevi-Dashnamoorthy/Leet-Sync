# Write your MySQL query statement below

select p.product_name, sum(unit) as unit 
from Products p
join Orders o
on o.product_id=p.product_id
where month(o.order_date)=2 and year(o.order_date)=2020
group by p.product_id
having sum(o.unit)>=100;
