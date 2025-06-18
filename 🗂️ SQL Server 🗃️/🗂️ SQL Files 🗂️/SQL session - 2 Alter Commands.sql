
/* Assume that you already created a column
   we can do following opertions on columns

   A) We can add a new column
   B) We can drop a column
   C) We can modify the data type of a column
   D) We can rename the column 

   That means some thing we are changing already an existed table

   The main keyword here is :ALTER  */

-- First check which data base you are using
use nareshit_apr_2024  -- type your database name

select * from student_details


/*================= Case-1:  Add a Column=====================================
--syntax:
-- alter table <table_name> add <column_name> <data_type>  */

ALTER table student_details 
add city varchar(30)

select * from student_details

-- you can add multiple columns
-- syntax:
-- alter table <table_name> add <column_name1> <data_type1>,<column_name2> <data_type2>

Alter table student_details
add student_fee float,
    student_department char

select * from student_details


/*============= CASE-2 : Drop the columns===========================

-- syntax:
-- alter table <table_name> drop column <column_name>
-- alter table <table_name> drop column <column_name1>,column <column_name2>  */

alter table student_details
drop column city 

select * from student_details


alter table student_details
drop column student_fee,
     column student_department

select * from student_details



/*==================CASE-3: Modify the column

-- modify columns means changing the data type
-- student details student_id data type is int
-- If we want to change int type to char

-- syntax
-- alter table <table_name> alter column <column_name> <change_data_type>  */
-- changes reflected after refresh

alter table student_details
alter column student_id char

select * from student_details
-- get back to int type and check the detail
alter table student_details
alter column student_id int


/*================CASE-4: Rename the column=================================

-- In MS SQL server we have stored procedures
-- It is like a packages in python
-- 10% syntax changes will be there Mysql/MSSQL/Oracle
-- Stored procedures (SP) is a collection of sql statements and sql commnads
-- Which are already compiled and stored in database

===========================STORED PROCEDURE(sp)======================================
- SP are set of SQL statments that are saved and stored in a database
- These can be resued and executed whenever we want, with out rewriting the same SQL syntax
- For complex operations SQLServer has written some SQL statments and they saved
- This is called as Stored Procedures
- It is similar anlaogy with python : Packages



-- syntax

-- sp_rename '<table_name>.<old_column_name>','<new_column_name>' , 'column'  */


select * from student_details    

--change student_name to SNAME

sp_rename 'student_details.student_name','SNAME','column'
select * from student_details 


EXEC sp_rename 'student_details.SNAME','student_name','column'



--------------------- Rename the table-----------------------
-- syntax
-- sp_rename '<old_table_name>', '<new_table_name>'


sp_rename 'student_details','STUDENT_DETAILS1'


select * from student_details
select * from STUDENT_DETAILS1

EXEC sp_rename  'STUDENT_DETAILS1','student_details'


/*======================= ALL Together====================================
A)  Add a new column
B)  Drop a column
C)  modify the column
D)  rename the column */

ALTER table student_details add city varchar(30)

alter table student_details drop column city 

alter table student_details alter column student_id char

EXEC sp_rename 'student_details.student_name','SNAME','column'




















































