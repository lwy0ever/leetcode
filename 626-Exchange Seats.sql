# Write your MySQL query statement below
select row_number() over(order by id - 1 + 2 * (id % 2)) as id,student from seat