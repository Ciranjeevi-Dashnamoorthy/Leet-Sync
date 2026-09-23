select e.reports_to as employee_id,m.name,count(e.name) as reports_count,
round(avg(e.age)) as average_age
from Employees e
join Employees m
on e.reports_to=m.employee_id
group by e.reports_to
order by e.reports_to asc;