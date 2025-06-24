---- ASSIGNMENT - 3 Like Operators ---

---- https://www.w3schools.com/sql/sql_like.asp

use nareshit_apr_2024
select * from bank       --- Complete Bank Dataset

/*
SYNTAX :

SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
*/

--- Select the education column where the status starts with the letter "t":
SELECT education
FROM bank
WHERE education LIKE 't%';

--- Ends with "y":
SELECT education
FROM bank
WHERE education LIKE '%y';

--- Case-insensitive match (SQL Server is case-insensitive by default unless configured otherwise):
SELECT education
FROM bank
WHERE education LIKE 'T%';

/*
The _ Wildcard
The _ wildcard represents a single character.

It can be any character or number, but each _ represents one, and only one, character.

Example
Return all customers from a city that starts with 'L' followed by one wildcard character, then 'nd' and then two wildcard characters:

SYNTAX - 1:
SELECT * FROM Customers
WHERE city LIKE 'L_nd__';

SYNTAX - 2:
SELECT column_name
FROM table_name
WHERE column_name LIKE 'pattern_with_underscore';

*/

-- 1. Match any value where the second letter is 'e':
SELECT education
FROM bank
WHERE education LIKE '_e%';
--- Matches: "tertiary", "secondary", etc.

-- 2. Match values that are exactly 8 characters long:
SELECT education
FROM bank
WHERE education LIKE '________';    --- Tertiary

SELECT * from bank

-- 3. Match values that are exactly 9 characters long:
SELECT education
FROM bank
WHERE education LIKE '_________';   --- Secondary

-- 4. Return all the customers from CONTACT that starts with "te" followed by one wild character, then "eph" and then two wild characters and END with "e"0
SELECT * from bank
where contact like 'te_eph__e';

select * from bank

-- 5. Contains
-- To return records that contains a specific letter or phrase, add the % both before * after the letter or phrase
SELECT * from bank
where poutcome like '%ilu%';     ---- Failure

SELECT * from bank
where contact like '%kno%';     ---- Unknown

-- 6. Combine Wildcards
-- Any wildcard, like % and _, can be used in combination with other wildcards
SELECT * from bank
where poutcome like 'o___%';     ---- other

SELECT * from bank
where education like 't___%';     ---- tertiary

-- Return all records that have "r" in the second position
SELECT * from bank
where job like '_e%';

-- 7. Without Wildcard
-- If no wildcard is specified, the phrase has to have an exact match to return a result
select * from bank
where job like 'self-employed';

-- 8. Return all the records that ends with 'ur'
SELECT * from bank
where job like '%ur';     ---- entrepreneur

-- 9. Return all the records that contains the pattern 'emp'
SELECT * from bank
where job like '%emp%';     ---- self-employed & unemployed

SELECT * from bank
where job like '%sel%';     ---- self-employed

SELECT * from bank
where job like '%u%';     ---- unemployed ; blue-collar ; entrepreneur ; student ; housemaid ; 

SELECT * from bank
where job like '%une%';     ---- unemployed

-- 10. Return all the records with education staring with any character followed by "ertiary"
SELECT * from bank
where education like '_ertiary';     ---- tertiary

-- 11. Return all the records with marital staring with "s", followed by any 3 characters, ending with "le"
SELECT * from bank
where marital like 's___le';     ---- single

-- 12. Using the [] Wildcard : Return all the records starting with either 'u', 's' or 'b'
SELECT * from bank
where job like '[usb]%';   ---- unemployed ; services ; blue-collar

-- 13. Using the - Wildcard : The '-' wildcard allows you to specify a range of characters inside the [] wildcard
-- Return all the records starting with "m","n","o","p","q","r","s","t"
SELECT * from bank
where job like '[m-t]%';   ---- management ; student ; services ; self-employed ; technician ; retired

-- 14. Combine Wildcards : Any wildcard, like % and _, can be used in combination with other wildcards
SELECT * from bank
where job like 'a__%';   ---- admin

-- 15. Combine Wildcards : Return all the records that have "r" in the third position
SELECT * from bank
where education like '__r%';   ---- tertiary

--- 16. Without Wildcard : If no wildcard is specified, the phrase has to have an exact match to return a result
SELECT * from bank
where contact like 'unknown';   ---- Return all the records of contact having the value "unknown"