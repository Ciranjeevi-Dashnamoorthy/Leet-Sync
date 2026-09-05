select user_id,count(prompt) as prompt_count , round(sum(tokens)/count(tokens),2) as avg_tokens
from prompts 
group by user_id
having count(prompt)>=3 and max(tokens)>round(sum(tokens)/count(tokens),2)
order by avg_tokens desc,user_id asc;

