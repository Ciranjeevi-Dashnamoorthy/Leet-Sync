# Write your MySQL query statement below
(select u.name as results
from MovieRating m
join Users u
on m.user_id=u.user_id
group by m.user_id
order by count(m.user_id) desc,u.name asc
limit 1
)
union all

(select u.title as results
from MovieRating m
join Movies u
on m.movie_id=u.movie_id
where month(m.created_at)=2 and year(m.created_at)=2020
group by u.movie_id
order by avg(m.rating) desc,u.title asc
limit 1
)
