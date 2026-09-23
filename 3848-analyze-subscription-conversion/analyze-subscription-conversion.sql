
select a.user_id,
        round((select avg(p.activity_duration)
        from  UserActivity p
        where p.activity_type ='free_trial' and p.user_id=a.user_id),2)
        as trial_avg_duration,
        round((select avg(p.activity_duration)
        from  UserActivity p
        where p.activity_type ='paid' and p.user_id=a.user_id),2)
        as paid_avg_duration

from UserActivity a
group by a.user_id
having count(case when a.activity_type='free_trial' then 1 end)>0
and count(case when a.activity_type='paid' then 1 end)>0
order by a.user_id asc; 