-- Can use COALESCE , but mySQl doesnt support it 
-- Can do Full Join , also doesnt support
--  simlate full join using union by simple select or left or right join

select employee_id 
from Employees 
where employee_id not in (
    select employee_id from Salaries
)

union

select employee_id 
from Salaries
where employee_id not in (
    select employee_id from Employees
)

order by employee_id;

