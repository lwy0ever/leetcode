# Write your MySQL query statement below
select today.id
 from Weather today
 join Weather yesterday
 on DATEDIFF(today.RecordDate,yesterday.RecordDate) = 1
 where today.temperature > yesterday.temperature