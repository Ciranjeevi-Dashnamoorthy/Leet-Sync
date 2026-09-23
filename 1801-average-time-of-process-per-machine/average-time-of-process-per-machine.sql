select a.machine_id,
        round((select avg(p.timestamp)
        from Activity p
        where p.activity_type='end' and p.machine_id=a.machine_id)
        -
        (select avg(p.timestamp)
        from Activity p
        where p.activity_type='start' and p.machine_id=a.machine_id),3)
        as processing_time
from Activity a
group by a.machine_id;