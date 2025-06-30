/*
SQL Assignment 4: Employee Database Basics
*/
use nareshit_apr_2024
select * from Employee_Database_Basicss

-- Select all employees from the IT department.
SELECT * FROM Employee_Database_Basicss WHERE Dept = 'IT';

select * from Employee_Database_Basicss

-- List employees who joined after 2020.
SELECT * FROM Employee_Database_Basicss WHERE JoinDate > '2020';

select * from Employee_Database_Basicss

-- Find employees earning more than ?60,000.

SELECT * FROM Employee_Database_Basicss WHERE Salary > 60000;

-- Show top 3 highest-paid employees.

select top 3 * from Employee_Database_Basicss ORDER BY Salary DESC;

-- Display employees ordered by JoinDate descending.

SELECT * FROM Employee_Database_Basicss ORDER BY JoinDate DESC;