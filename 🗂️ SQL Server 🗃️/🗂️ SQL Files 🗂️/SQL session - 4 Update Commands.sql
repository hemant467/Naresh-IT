----- Change the data base

use nareshit_apr_2024

select * from student_details

/* ========== Update =====================
 update is used to update the rows 
       - specific rows
	   - on specific column
	   - by using some conditions  

 update means simply update(modify) the rows 

 -- All the values in a specific column will update
 syntax:
 update <table_name>
 set <column_name>=value 
 
 -- Update multiple columns values
 update <table_name>
 set  <column1>=value,
      <column2>=value  */


-- insert 3 more rows
insert into student_details
values (1,'Chandu',200), 
       (4,'Srilekha',100),
	   (5,'Bhaskar',300)

select * from student_details

/*============= Case-1===========================
update all the student_marks is 500 */

update student_details set student_marks = 500
select * from student_details

-- student marks =200
update student_details set student_marks=200

/*=================== Case-2 (On single condition)==========================
I want to update a specific row
I want update only Chandu marks as 300
student name      stuent marks

update student_details set student_marks=300
here will use condition : Where clause 

-- syntax:
update <table_name> set <column_name> where <condition>   */

update student_details  set student_marks=300
where student_name='Chandu'

select * from student_details

-- update student marks= 400 where student_id=1
update student_details  set student_marks=400
where student_id=1

select * from student_details

/*============ Case-3(Two conditions)=============
I want change the student_name='Neha' based on student_id=3 and 
student_marks=500   */

-- and means : two conditions should satisfy
update student_details  set student_name='Neha'
where student_id=3 and student_marks=500

select * from student_details

update student_details  set student_name='Neha'
where student_id=3 or student_marks=500

select * from student_details


-- student_id=3  and student_marks=300
update student_details  set student_name='Neha'
where student_id=3 and student_marks=300
-- The specific condition is not satisfying
-- so No error but it display as 0 rows are affected

-- student_name='Ankit'
-- student_id=3 or student_marks=400
update student_details  set student_name='Ankit'
where student_id=3 or student_marks=400
select * from student_details


-- Or means: any one condition satisfy is enough
update student_details  set student_name='Ankit'
where student_id=3 or student_marks=300

select * from student_details

-- student_id=1(2)  or student_marks=200 (4) =6
update student_details  set student_name='Akhil'
where student_id=1 or student_marks=200

select * from student_details

/*================= CASE-4(Update null values)=================
 update the null values 
 create a new column sudent_city , if city already there create
 another column
 by using alter command */

alter table student_details add city varchar(20)

select * from student_details



update student_details set city='Hyd'
select * from student_details

-- create one more column base_location
alter table student_details add base_location varchar(20)
select * from student_details

-- update base_location with hyd 
-- where base_location has null values and student_marks=400
update student_details 
set base_location='Hyd'
where student_marks=400 and base_location is NULL 

select * from student_details

-- whenever Null is there under where use  'is' operator

/*=========== Case-5: Update with Null values==========
-- Wherever Student id=1 
--I want to update student name with NULL */

update student_details set student_name=NULL
where student_id=1

select * from student_details

/*============== Case-6(In Operator) =============

I want update city with Bengaluru only for ids 2,4,5 */

update student_details set city='Blr'
where student_id in (2,4,5)

select * from student_details

/*============= Case-7 (not in operator)===========*/
update student_details set city='Chennai'
where student_id not in (2,4,5)   -- 1(2times),3

select * from student_details

/*=========== Case-8(Between operator)============*/
update student_details set student_name='Sai'
where student_id between 2 and 5 -- 2,3,4,5 (4 rows)

select * from student_details

/*============== Case-9 ( >,< operators)===========
 update student marks with Null , where student id > 3*/

update student_details set student_marks=null
where student_id>3

select * from student_details


update student_details 
set student_marks=100,
    city='Mumbai' 
where student_id<=3  --Multiple columns updation

select * from student_details







































