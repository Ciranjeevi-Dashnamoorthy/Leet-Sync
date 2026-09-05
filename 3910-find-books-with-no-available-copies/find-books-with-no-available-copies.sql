
select b.book_id ,b.title,b.author,b.genre,b.publication_year,b.total_copies as current_borrowers
from library_books b
where b.total_copies = (
    select count(1) from borrowing_records r
    where r.book_id=b.book_id and r.return_date is null
)
order by b.total_copies desc, b.title asc;
