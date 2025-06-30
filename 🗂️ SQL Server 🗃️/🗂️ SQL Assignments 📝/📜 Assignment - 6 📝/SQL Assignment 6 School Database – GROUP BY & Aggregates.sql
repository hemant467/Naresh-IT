/*

SQL Assignment 6: School Database – GROUP BY & Aggregates

Database : 

Students


| StuID | Name   | Class | Marks |
| ----- | ------ | ----- | ----- |
| 1     | Aman   | 10    | 88    |
| 2     | Ravi   | 10    | 76    |
| 3     | Neha   | 9     | 90    |
| 4     | Simran | 9     | 72    |
*/
use nareshit_apr_2024
select * from School_Database

SELECT Class,
       AVG(Marks) AS AvgMarks
FROM School_Database
GROUP BY Class;

----- Drop extra columns
alter table School_Database
drop column column1;
select * from School_Database

alter table School_Database
drop column column6;
select * from School_Database


-- Delete rows where StuID is NULL
DELETE FROM School_Database
WHERE StuID IS NULL;
select * from School_Database

--- 1. Find average marks per class.
SELECT Class, AVG(Marks) AS AvgMarks
FROM School_Database
GROUP BY Class;
select * from School_Database

---             Avg Marks
--- class 9  :     81
--- class 10 :     82


--- Count how many students are in each class.
SELECT Class,
       COUNT(*) AS StudentCount
FROM School_Database
GROUP BY Class;
select * from School_Database

--- class 9  : 2 students
--- class 10 : 2 students



--- Find the class with the highest total marks.
SELECT TOP 1 Class,
       SUM(Marks) AS TotalMarks
FROM School_Database
GROUP BY Class
ORDER BY TotalMarks DESC;

--- class 10 TotalMarks 88 + 76 = 164
--- class  9 TotalMarks 90 + 72 = 162



--- Show students who scored above class average.
SELECT s.Name,
       s.Class,
       s.Marks
FROM School_Database s
JOIN (
    SELECT Class,
           AVG(Marks) AS AvgMarks
    FROM School_Database
    GROUP BY Class
) a
  ON s.Class = a.Class
WHERE s.Marks > a.AvgMarks;

--- Neha Class 9   Marks : 90 - TOP
--- Aman Class 10  Marks : 88 - TOP


--- Show top scorer from each class.

SELECT Name,
       Class,
       Marks
FROM School_Database s
WHERE Marks = (
    SELECT MAX(Marks)
    FROM School_Database
    WHERE Class = s.Class
);
--- Aman Class 10  Marks : 88 - TOP
--- Neha Class 9   Marks : 90 - TOP