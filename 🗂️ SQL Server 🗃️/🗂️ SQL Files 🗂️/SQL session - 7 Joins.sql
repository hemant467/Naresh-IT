/*=================== JOINS===========================

Information retrive methods

1. Selection : With where condition from a single table
2. Projection : With out where condition from a single table
3. Joins : Retrive the information from multiple tables


1Q)  what is the joining creteria 

             you want join based on any column
             you want join based on any common column


2Q)  When I join two tables is two tables has equal rows?
                 different table has different rows

3Q) after joining is duplicates allowed

Joins are two types

A) ANSI-Format : "ON" key word on join condition
                (i) Inner join
				(ii) Outer join:
				       --> Left outer join
					   --> Right outer join
					   --> Full outer join
				(iii) Cross join

B) Non-ANSI format: "Where" key word on join condition
                (i) Equi join
				(ii) Non-Equi Join
				(iii) self join


Will create two tables
1. Student_information
    {STID int, SNAME varchar,SMAIL varachar,COURSEID int}
2. Course_details
   {COURSEID int,CNAME varchar,CFEE decimal(6,2)}

    decimal(6,2): 4 digits and 2 decimals */


use nareshit_apr_2024

CREATE TABLE STUDENT_INFORMATION
(STDID INT, SNAME VARCHAR(50),SMAIL VARCHAR(100),COURSEID INT)

CREATE TABLE COURSE_DETAILS
(COURSEID INT,CNAME VARCHAR(20),CFEE DECIMAL(6,2))

insert into STUDENT_INFORMATION
values(1,'Akshay','akshay@gmail.com',111),
      (2,'Bunny','bunny@gmail.com',222),
	  (3,'Chinni','chinni@yahoo.com',333),
	  (4,'Darma','darma@outlook.com',444),
	  (5,'Veera','veera@gmail.com',555)

insert into COURSE_DETAILS
values (111,'Science',1000), -- 6digit = 4 digit+ 2 decimal points
       (222,'Commerce',800),
	   (333,'Arts',750)

select * from STUDENT_INFORMATION
select * from COURSE_DETAILS

/*=============== Inner join================================================

1. Common column
2. data type of common column must be same

syntax: 
select * from <t1> join key <t2>
ON
<joining condition>  

we are joining two tables by using "ON" keyword 
by using common column */

--============= Case-1: Same column=========================

select * from COURSE_DETAILS
select * from STUDENT_INFORMATION

select * from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.COURSEID=COURSE_DETAILS.COURSEID

select STDID,SAME,SMAIL,COURSEID,CFEE,CNAME 
from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.COURSEID=COURSE_DETAILS.COURSEID


--===================Case-2: Different column====================
select * from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.STDID=COURSE_DETAILS.COURSEID

-- Do one thing insert a one more row COURSE_DETAILS with COURSEID=5
--              insert one more row in student_inforamtion with stid=333

insert into COURSE_DETAILS values(5,'DS',2000)
insert into STUDENT_INFORMATION values(333,'Ankit','ankit@gmail.com',5)

select * from COURSE_DETAILS
select * from STUDENT_INFORMATION

select * from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.STDID=COURSE_DETAILS.COURSEID

-- joining what is left table and what is right tabel
-- inner join means common data 
-- if data is not common , inner join will give empty table

-- We can able to inner join with different column also

--===================CASE-3: different column with different data type========
-- Try to join two tables SMAIL from STUDENT_INFORMATION 
-- with COURSEID from COURSE_DETAILS

select * from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.SMAIL=COURSE_DETAILS.COURSEID

-- In order join two tables either use same column or different column
-- data type must be same

-- duplicates are allowed or not allowed?

-- insert a row COURSE DETAILS with courseid=111
insert into COURSE_DETAILS values(111,'IOT',1500)
insert into COURSE_DETAILS values(222,'Commerce',800)

select * from COURSE_DETAILS
select * from STUDENT_INFORMATION

select * from STUDENT_INFORMATION inner join COURSE_DETAILS
ON
STUDENT_INFORMATION.COURSEID=COURSE_DETAILS.COURSEID

-- Duplicates are allowed
-- Same data type must
-- No common column required


--====================== Left Outer Join=========================
use nareshit
select * from COURSE_DETAILS
select * from STUDENT_INFORMATION

-- both has equal rows
-- try to create two extra rows in any table

insert into COURSE_DETAILS values(555,'CS',3000),(666,'Block chain',4000)

-- CASE1:  SAME COLUMN

select * from COURSE_DETAILS
select * from STUDENT_INFORMATION
select * from COURSE_DETAILS left outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

-- where STUDENT_INFORMATION.COURSEID is Not NULL

-- what is the left table: COURSE DETIALS

-- Step-1: All the rows of left table will come ( 8rows)
-- Step-2:Left outer join try to get the all matching rows from left table with right table
--       based on specified column
-- step-3: ummatched rows from B tables displayed as NULL values

-- CASE-2: different column
select * from COURSE_DETAILS
select * from STUDENT_INFORMATION
select * from COURSE_DETAILS left outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.STDID

select COURSE_DETAILS.COURSEID,STDID 
from 
COURSE_DETAILS left outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.STDID


--================ Right Outer join=====================
-- CASE1:  SAME COLUMN

select * from COURSE_DETAILS
select * from STUDENT_INFORMATION
select * from COURSE_DETAILS full outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

select * from COURSE_DETAILS right outer join STUDENT_INFORMATION
ON
STUDENT_INFORMATION.COURSEID=COURSE_DETAILS.COURSEID



select * from COURSE_DETAILS left outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

select * from COURSE_DETAILS right outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

select * from COURSE_DETAILS full outer join STUDENT_INFORMATION
ON
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

/*============= Cross join
-- No condition required 
-- Table A has M rows and Table B has N rows
-- Final table has MxN rows will come */
select * from COURSE_DETAILS cross join STUDENT_INFORMATION



/*================= Non Ansi 
- Where conditions
---------------------------- Equi join-------------------
Retriving data from the mutiple tables based on equal (=)
1) where 
2) =   */

select * from STUDENT_INFORMATION
select * from COURSE_DETAILS
select * from STUDENT_INFORMATION,COURSE_DETAILS
where
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.COURSEID

select * from STUDENT_INFORMATION,COURSE_DETAILS
where
COURSE_DETAILS.COURSEID=STUDENT_INFORMATION.STDID



select * from STUDENT_INFORMATION,COURSE_DETAILS
where
COURSE_DETAILS.COURSEID != STUDENT_INFORMATION.COURSEID


select * from STUDENT_INFORMATION
select * from COURSE_DETAILS
select * from STUDENT_INFORMATION,COURSE_DETAILS
where
COURSE_DETAILS.COURSEID>STUDENT_INFORMATION.COURSEID

-- <,>,!,>=,<=

-- Try to explore how to join 3 tables task
-- 


































