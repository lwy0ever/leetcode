CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE m int;
  SET m = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select DISTINCT Salary from Employee order by Salary desc limit m,1
  );
END