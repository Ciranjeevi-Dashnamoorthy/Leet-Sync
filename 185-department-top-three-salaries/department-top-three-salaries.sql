with cte as (select departmentId,name,salary,
dense_rank() over
(partition by departmentId order by salary desc)
as top
from Employee)

select d.name as Department ,c.name as Employee,c.salary as Salary
from cte c
join Department d
on c.departmentId=d.id
where top<=3;
