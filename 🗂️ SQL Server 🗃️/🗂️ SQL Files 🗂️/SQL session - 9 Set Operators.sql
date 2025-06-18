
/* ====================== SET operators=====================

when we want to combine two or more select statements use set opeartors

- union
- union all
- intersect
- except

- RULES:
  1. No of columns should be same in both select statements
  2. While you are selecting data types of two columns should match
  3. While you are selecting data order of the columns should same

First we will create two tables emp1 emp2
with same columns eid ename esalary 3 values  */

-- emp1 table

use nareshit_batch1

create table emp1 ( eid int, ename varchar(255), esalary decimal)
create table emp2 ( eid int, ename varchar(255), esalary decimal)

insert into emp1 values (1,'Maha',50000),
                        (2,'Nivi',60000),
						            (3,'Honey',70000)
insert into emp2 values (1,'virinchi',80000),
                        (4,'varshith',90000),
						            (5,'Rishi',75000)

select * from emp1  
select * from emp2


select * from emp1  
union 
select * from emp2

select eid,ename from emp1
union 
select eid,ename from emp2   --- 3 RULES follows or not? Yes


select ename,eid from emp1
union 
select eid,ename from emp2  --- 3 Rules follows or not? Order of the columns

select eid from emp1
union 
select ename from emp2   ---- 3 Rules follwos or not? datatypes or not matching

-- Union means  A OR B combning all

------------------------Intersect--------------------------

select * from emp1 intersect select * from emp2

insert into emp1 values(4,'varshith',90000)

select * from emp1
select * from emp2

select * from emp1 union select * from emp2
select * from emp1 intersect select * from emp2

---------------------- Except------------------------------
-- A-B : It will return from A which are not found in B
-- B-A : It will return from B which are not found in A
select * from emp1
select * from emp2
select * from emp1 except select * from emp2
select * from emp2 except select * from emp1