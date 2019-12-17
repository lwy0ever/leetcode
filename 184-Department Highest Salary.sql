# Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary from department d
 join employee e on d.id = e.departmentid
 where (e.salary,e.departmentid) in
 (select max(salary), departmentid from employee
 group by departmentid)