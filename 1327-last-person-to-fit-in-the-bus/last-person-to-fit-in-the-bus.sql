
with t1 as (select person_name,sum(weight) over(order by turn) as total from Queue)

select person_name
from t1
where total<=1000
order by total desc
limit 1;