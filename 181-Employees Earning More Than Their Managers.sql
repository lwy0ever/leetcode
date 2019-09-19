# Write your MySQL query statement below
select em.Name as Employee from Employee em join Employee ma on em.ManagerId = ma.Id where em.Salary > ma.Salary