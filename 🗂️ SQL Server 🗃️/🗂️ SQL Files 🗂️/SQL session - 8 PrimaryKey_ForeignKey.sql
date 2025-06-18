--working with Primary key and Foreign key constarints

-- Foreign key is used to make relationship between two or more
-- than two tables

-- Conditions:

	--1) One table should contains PK
	--2) another table contains Foreign key
	--3) Need a common column in Both tables
	--4) Common column data type Must be same in both tables
	
-- Step-1:
Create table DEPARTMENT(DEPTNO INT PRIMARY KEY, 
                         DNAME VARCHAR(40),
                        LOCATION VARCHAR(40)) -- PARENT TABLE
--STEP-2:
INSERT INTO DEPARTMENT VALUES(10,'ECE','HYD'),
                       (20,'EEE','BLR'),
					   (30,'CSE','CHENNAI')

SELECT * FROM DEPARTMENT

--STEP-3:
-- In parent table on which column we apply pk contrain
-- that column only we need to provide 
-- data type also should same
-- then apply FK
CREATE TABLE EMPLOYEE(EMPID INT,
                       ENAME VARCHAR(40),
                       SALARY MONEY,
                      DEPTNO INT FOREIGN KEY REFERENCES DEPARTMENT(DEPTNO)
					  ) --CHILD TABLE

SELECT * FROM DEPARTMENT
SELECT * FROM EMPLOYEE

-- 10,20,30 ONLY SUPPORT IN CHILD TABLE
-- IF YOU GIVE 40 IT WILL NOT ACCEPT
-- WHICH MEANS RELATION EXIST

INSERT INTO EMPLOYEE VALUES(101,'RAMESH',50000,10)
SELECT * FROM EMPLOYEE

INSERT INTO EMPLOYEE VALUES(101,'RAMESH',50000,40)









