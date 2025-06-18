

use nareshit_eve_march

select * from bank     

-- 1Q)  Top 20 rows

select top 20 * from bank
-- select top 20 all the columns from bank table

--selet * from bank limit 20

-- Mysql  SqlServer  Oracle  PostgreSQl
-- 90% syntax will be same


--2Q) No of rows in a table 
-- will use count

select count(*) from bank

-- the output is in a tabular form
-- column and row
-- Column: No column name
-- row :  count value

select count(*) as no_of_rows from bank
-- here column name: no_of_rows

select count(*) count_of_data from bank
-- column name: count_of_data

-- All together

select count(*) from bank  -- with out column
select count(*) as no_of_rows from bank
select count(*) count_of_data from bank

--3Q) Select top5 rows of balance column
select balance from bank -- all the data
select top 5 balance from bank -- top5


--4Q)  Find the sum of balance   keyword: sum
select count(balance) from bank
select sum(balance) as total_balance from bank

-- 5Q) Find the max of balance   keyword: max

select max(balance) as max_balance from bank

-- 6Q) Find min  of balance      keyword: min

select min(balance) as min_balance from bank

-- 7Q) Find average balance

select avg(balance) as avg_balance from bank
select round(avg(balance),3) as avg_balance from bank


-- 8Q) Find count of balance

select count(balance) as count_balance from bank

-- 9Q) Do all at one place

select count(balance) as count_balance,
       sum(balance)  as  total_balance,
	   max(balance)  as  max_balance,
	   min(balance)  as  min_balance,
	   avg(balance)  as  avg_balance from bank


select sum(balance),
       count(balance),
       sum(balance)/count(balance) from bank



--10Q) How many types of jobs available
--    EDA we use unique
--    SQL  distinct

select job from bank   -- entire data  4521

select distinct job from bank -- unique data will display 12

select count(job) as total_count from bank -- entire data count 4521

select count(distinct job) as unique_job_count from bank -- unique count

select APPROX_COUNT_DISTINCT(job) from bank


select * from bank

--11Q) Retrive the balance for those have age 80

select balance from bank where age=80

-- 12Q) Retrive the average balance for those have age =80

select avg(balance) as balance_80 from bank where age=80

-- do the same two queries for 79 78

select avg(balance) as balance_80 from bank where age=80
select avg(balance) as balance_79 from bank where age=79
select avg(balance) as balance_78 from bank where age=78


--cant we group the people based on age in a single query
------------------GROUPBY------------------------------

select age from bank group by age  -- same as below query
select distinct(age) from bank     -- same as above query
select age,count(age) age_count from bank group by age
select age,count(balance) as count from bank group by age
select age,avg(balance) as avg from bank group by age

select job from bank group by job
select job,count(job) from bank group by job

-- on which column you want work
-- which column you want to divide
-- i want group the people based on age


select job from bank group by job
select job from bank group by marital -- error

-- whenever you do group by slect that column only first
select marital from bank group by marital
--Note: which column you want group select that column first
--      if you want to use any other coumn use aggregations way only

select age from bank group by age -- this query divides age into differnt groups

select age, balance as age_average_balance
from bank group by age

select age, avg(balance) as age_average_balance
from bank group by age

select avg(balance) as age_average_balance
from bank group by age


-- First decide which column you want to divide into groups
select age,count(age) age_count from bank group by age


select age,count(age) count_age,
           sum(balance) sum_balance,
		   max(balance) max_balance,
		   min(balance) min_balance,
		   avg(balance) avg_balance,
		   sum(balance)/count(balance) as avg_math from bank 
group by age

-- from output data age=80  where clause
select age,count(age) count_age,
           sum(balance) sum_balance,
		   max(balance) max_balance,
		   min(balance) min_balance,
		   avg(balance) avg_balance from bank 
where age in (60,70,80)
group by age


--==================== ORDER BY========================

select age from bank group by age order by age  -- default ascending order

-- if you want descending order use desc
select age from bank group by age order by age desc

-- if you want ascending order use asc
select age from bank group by age order by age asc

-- job ascending descending

select job from bank group by job 
order by job

-- first order by
select age from bank where age=80 
order by age

select age,balance from bank where age=80 
order by balance

-- where condition ====> group by ====> order by  

select age,count(age) count_age,
           sum(balance) sum_balance,
		   max(balance) max_balance,
		   min(balance) min_balance,
		   avg(balance) avg_balance from bank 
group by age
order by avg_balance

-- 13Q) get the average balance of unemployed people


select job,avg(balance) avg_balance from bank 
group by job

-- step:1  will group by job
-- step-2: avg balance of each group
-- step-3: extract only unemployed data (where)

select job,avg(balance) avg_balance from bank 
where job='unemployed'
group by job

select job,avg(balance) avg_balance from bank 
group by job
where job='unemployed' -- modify by using having

-- 14Q)  get the max, min,avg balance of 
--        different group of age people where y=0
-- step-1: groupby age
-- step-2: get the aggregations of balance
-- step-3: implement the where condition y=0
select age, avg(balance), 
		max(balance), 
		min(balance) from bank
where y=0
group by age














































