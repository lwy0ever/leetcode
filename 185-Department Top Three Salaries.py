# Write your MySQL query statement below
select d.name as Department,e1.name as Employee,e1.salary as Salary from Employee e1
join department d on d.id = e1.departmentid
where 3 > (
    select count(distinct e2.salary) from employee e2
    where e2.salary > e1.salary and e2.departmentid = e1.departmentid
)