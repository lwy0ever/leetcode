# Write your MySQL query statement below
select T.request_at Day,
 round(sum(case T.status
           when 'completed' then 0
           else 1 end) / count(T.status),2) 'Cancellation Rate'
from (select request_at,status from Trips t
 join users u on t.client_id = u.users_id
 where u.banned = 'No') T
 where request_at between '2013-10-01' and '2013-10-03' 
 group by T.request_at
/*
select allTrip.request_at day,round(ifnull(canceled.n,0) / allTrip.n,2) 'Cancellation Rate'
from
(select request_at,count(*) as n from Trips
 where request_at between '2013-10-01' and '2013-10-03'
 and Client_Id not in (select Users_Id from Users where Banned = 'Yes')
 and Driver_Id not in (select Users_Id from Users where Banned = 'Yes')
 group by request_at) allTrip
left join
(select request_at,count(*) as n from Trips
 where request_at between '2013-10-01' and '2013-10-03'
 and status <> 'completed'
 and Client_Id not in (select Users_Id from Users where Banned = 'Yes')
 and Driver_Id not in (select Users_Id from Users where Banned = 'Yes')
 group by request_at) canceled
 on canceled.request_at = allTrip.request_at
*/