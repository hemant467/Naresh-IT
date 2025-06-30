/*
SQL Assignment 8: Advanced – Foreign Keys & Joins

Objective: Practice advanced joins, foreign key understanding.  

Questions:
List department names with their employees.
Show total salary expense for each department.
Which department has highest average salary?
List employees who work in Finance.
Count how many employees are in each department.

DATASET : 

Departments

| DeptID | DeptName |
| ------ | -------- |
| 1      | HR       |
| 2      | IT       |
| 3      | Finance  |


Employees

| EmpID | Name  | DeptID | Salary |
| ----- | ----- | ------ | ------ |
| 1     | Ravi  | 1      | 60000  |
| 2     | Meena | 2      | 70000  |
| 3     | Raj   | 2      | 72000  |
| 4     | Divya | 3      | 68000  |

*/

use nareshit_apr_2024

-- Create Departments table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

-- Create Employees table
CREATE TABLE Employ_ee (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    DeptID INT,
    Salary INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);

-- Insert into Departments
INSERT INTO Departments (DeptID, DeptName) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

-- Insert into Employees
INSERT INTO Employ_ee (EmpID, Name, DeptID, Salary) VALUES
(1, 'Ravi', 1, 60000),
(2, 'Meena', 2, 70000),
(3, 'Raj', 2, 72000),
(4, 'Divya', 3, 68000);

select * from Departments
select * from Employ_ee

-- List department names with their employees.
SELECT 
    d.DeptName,
    e.Name AS EmployeeName
FROM 
    Employ_ee e
JOIN 
    Departments d ON e.DeptID = d.DeptID;

-- Show total salary expense for each department.
SELECT 
    d.DeptName,
    SUM(e.Salary) AS TotalSalaryExpense
FROM 
    Employ_ee e
JOIN 
    Departments d ON e.DeptID = d.DeptID
GROUP BY 
    d.DeptName;

-- Which department has highest average salary?
SELECT TOP 1
    d.DeptName,
    AVG(e.Salary) AS AvgSalary
FROM 
    Employ_ee e
JOIN 
    Departments d ON e.DeptID = d.DeptID
GROUP BY 
    d.DeptName
ORDER BY 
    AvgSalary DESC;

-- List employees who work in Finance
SELECT 
    e.Name
FROM 
    Employ_ee e
JOIN 
    Departments d ON e.DeptID = d.DeptID
WHERE 
    d.DeptName = 'Finance';

-- Count how many employees are in each department
SELECT 
    d.DeptName,
    COUNT(e.EmpID) AS EmployeeCount
FROM 
    Employ_ee e
JOIN 
    Departments d ON e.DeptID = d.DeptID
GROUP BY 
    d.DeptName;