/*

SQL Assignment 7: Library Database – Subqueries

Objective: Practice subqueries (in WHERE, IN, EXISTS).  

Questions:
List books that have never been borrowed.
Find authors whose books are borrowed more than once.
Show book titles borrowed in December 2024.
List all borrowers who borrowed “Python Basics”.
Display all books that were borrowed by more than one person.


DATASET :

Books

| BookID | Title         | Author    | Copies |
|        |               |           |        |
| 1      | Python Basics | Omkar Sir | 5      |
| 2      | AI for All    | Elon Musk | 2      |
| 3      | SQL Secrets   | Sam       | 10     |


Borrowed

| BorrowID | BookID | Borrower | Date       |
|          |        |          |            |
| 1        | 1      | Ravi     | 2024-12-01 |
| 2        | 2      | Meena    | 2024-12-03 |
| 3        | 1      | Arjun    | 2024-12-05 |

*/

use nareshit_apr_2024
drop table Boooks
-- Create Books table
create table Boooks(
    BookId int primary key,
    Title varchar(20),
    Author varchar(20),
    Copies int
)

drop table Borrowedd
-- Create Borrowed table
create table Borrowedd(
    BorrowedID int primary key,
    BookID int,
    Borrower varchar(20),
    date DATE,
    foreign key (BookID) references Boooks(BookID)
);

-- Insert Data

-- Insert into Books
INSERT INTO Boooks (BookID, Title, Author, Copies) VALUES
(1, 'Python Basics', 'Omkar Sir', 5),
(2, 'AI for All', 'Elon Musk', 2),
(3, 'SQL Secrets', 'Sam', 10);

-- Insert into Borrowed
INSERT INTO Borrowedd (BorrowedID, BookID, Borrower, Date) VALUES
(1, 1, 'Ravi', '2024-12-01'),
(2, 2, 'Meena', '2024-12-03'),
(3, 1, 'Arjun', '2024-12-05');

select * from Boooks
select * from Borrowedd

-- List books that have never been borrowed.
select * from Boooks
where BookId not in(
    select distinct BookId from Borrowedd);

-- Find authors whose books are borrowed more than once.
SELECT Author FROM Boooks b
JOIN Borrowedd br ON b.BookId = br.BookID
GROUP BY Author
HAVING COUNT(*) > 1;
---- O/p : Omkar Sir



-- Show book titles borrowed in December 2024.

SELECT DISTINCT b.Title
FROM Boooks b
JOIN Borrowedd br ON b.BookID = br.BookID
WHERE br.Date BETWEEN '2024-12-01' AND '2024-12-31';
/*
O/p : 

AI for All
Python Basics
*/

-- List all borrowers who borrowed “Python Basics”.
SELECT br.Borrower
FROM Borrowedd br
JOIN Boooks b ON br.BookID = b.BookID
WHERE b.Title = 'Python Basics';
/*
O/p: Borrower
Ravi
Arjun
*/

-- Display all books that were borrowed by more than one person.
SELECT b.BookID, b.Title
FROM Boooks b
JOIN Borrowedd br ON b.BookID = br.BookID
GROUP BY b.BookID, b.Title
HAVING COUNT(DISTINCT br.Borrower) > 1;
/*
O/p:
BookID : 1  ||  Title : Python Basics
*/