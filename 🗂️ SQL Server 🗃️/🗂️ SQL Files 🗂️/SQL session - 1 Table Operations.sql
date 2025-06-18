-- when you open new query page , a white board will pop up

-- if you write any thing in this page, this belongs to master database

-- create a new database

/* ---------- syntax--------------*/

-- create database <database_name>

-- syntax is not case sensitive

create database nareshit_apr_2024

-- we created a new data base : naresh it

-- now we want use the nareshit database

-- use <database_name>
use nareshit_apr_2024

-- database we can change manually or by using query

/*
create table <table_name>(column1 <data_type>,
                          column2 <data_type>,
                          column3 <dat_type>)  
*/

create table student_details(
student_id int,
student_name varchar(255),  --variable character 255
student_marks float)



--select *  from <table_name>
select * from student_details    -- all the columns
select student_id,student_name from student_details -- selected columns

-- insert values

/* insert into <table_name>  
values  (row1), (row2),(row3)*/

insert into student_details values 
(1,'Harsh',100),
(2,'Hemanth',200),
(3,'Shashi',300)


-- Query the table

select * from student_details


--======================= All Together =================================
-- Create a database
-- Use database
-- Create a table
-- instert values
-- query the table
create database nareshit
use nareshit
create table student_details(student_id int,student_name varchar(255),student_marks float)
insert into student_details values (1,'Harsh',100),(2,'Hemanth',200),(3,'Shashi',300)
select * from student_details
-----------------------------------------------------------------------------------------
--Case-1
--=============================== Identity columns==================================
/* identity(1,1)    start=1  increment=1      1,2,3,4
   identity(5,2)    start=5  increment=2      5,7,9,11 */
-- create new table
create table empoyee_details(Eid int identity(1,1),
                            Ename varchar(30),
							Esalary float)

insert into empoyee_details values ('Mukesh',50000.50), 
                                    ('Ganesh',60000)

select * from empoyee_details

insert into empoyee_details values (70000) -- error
insert into empoyee_details(Esalary) values (70000)
select * from empoyee_details
insert into empoyee_details values (Null,70000)

insert into empoyee_details values (10,Null,70000) --error

select * from empoyee_details

/*
Eid(int,notnull)===== >
                     1) it is a integer data type
                     2) and null values are not allowed
Esalary(float,null)===>
                     1) It is a float data type
					 2) Null values are allowed   */

------- CASE-2:
/*===================== Not NULL column==============*/

-- not null means the specified column should not contain null values

create table product(
product_id int identity(1,1),
product_name varchar(30),
product_city varchar(25) not null)

insert into product values ('car','Mumbai')

select * from product
insert into product(product_name) values ('Bus')

insert into product values ('bus',Null)
insert into product values ('car',Null)  -- error(bcz city column does not takes null vales)

insert into product values (10,'car','Mumbai')


-- Case-3
/*===================== default column name==============
suppose assume all the items are from same city i.e  'Hyd'
then we can use 'Hyd' value as default value for city column
*/

create table product1(
product_id int identity(1,1),  -- identity column
product_name varchar(30) not null, -- not null
product_city varchar(25) default 'Hyd') -- default column

-- product id value automatically will come
-- product city always 'Hyd'
-- so we need to mention Explicitly which value we want insert

insert into product1 values ('Car'), ('Bus') ,('Train')  --error

insert into product1(product_name) values 
           ('Car'), ('Bus') ,('Train')
select * from product1

insert into product1 values ('car','Mumbai')

select * from product1

insert into product1(product_name,product_city) 
            values ('Bus','Mumbai')

insert into product1 values ('Bus','Mumbai')

insert into product1(product_city) values ('blr')

-- so you can overrite default values
-- from table property I understood


/* Drop the table vs Truncate the Table

-- DROP TABLE <table_name1>,<table_name2>

-- you will loss all the information

-- it will completely the table vanish */

drop table product

select * from product

/*=============== Truncate the table==========*/

-- truncate TABLE <table_name1>,<table_name2>
-- delete all the rows
-- table will exist
-- using truncate we can not delete a specific rows 

truncate table product1

select * from product1



/*===================== Recap Excercise==========================================
1) Create a database
2) Use database
3) Create a table
     - not null column
	 - identity column
	 - default column
4) Insrert the values
5) Query the table
6) Truncate the table and drop the table (get the difference)*/



-- There are so many tables will be avialable in particular database

/*========== Getting Schema of tables and columns===============*/

use nareshit
select * from INFORMATION_SCHEMA.TABLES

select * from sys.tables

select * from INFORMATION_SCHEMA.COLUMNS  -- * means all the columns

select TABLE_NAME, COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS




















































