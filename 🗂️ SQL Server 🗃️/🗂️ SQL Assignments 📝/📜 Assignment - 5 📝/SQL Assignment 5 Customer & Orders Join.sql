/*
SQL Assignment 5: Customer & Orders – JOIN Practice

Dataset :

Customers

| CustID | CustName | City    |
|        |          |         |
| 1      | Raj      | Mumbai  |
| 2      | Meena    | Delhi   |
| 3      | Arjun    | Chennai |

Orders

| OrderID | CustID | OrderDate  | Amount |
|         |        |            |        |
| 101     | 1      | 2023-06-01 | 5000   |
| 102     | 2      | 2023-06-02 | 3000   |
| 103     | 1      | 2023-06-03 | 7000   |

*/

use nareshit_apr_2024
select * from Customer_and_Orders

-- Customers Table
CREATE TABLE Customerss (
    CustID INT PRIMARY KEY,
    CustName VARCHAR(100),
    City VARCHAR(100)
);

INSERT INTO Customerss (CustID, CustName, City) VALUES
(1, 'Raj', 'Mumbai'),
(2, 'Meena', 'Delhi'),
(3, 'Arjun', 'Chennai');

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustID INT,
    OrderDate DATE,
    Amount INT,
    FOREIGN KEY (CustID) REFERENCES Customerss(CustID)
);

-- Sample Data for Orders
INSERT INTO Orders (OrderID, CustID, OrderDate, Amount) VALUES
(101, 1, '2023-06-01', 5000),
(102, 2, '2023-06-02', 3000),
(103, 1, '2023-06-03', 7000);

DROP TABLE IF EXISTS Orders;

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustID INT,
    OrderDate DATE,
    Amount INT,
    FOREIGN KEY (CustID) REFERENCES Customerss(CustID)
);

INSERT INTO Orders (OrderID, CustID, OrderDate, Amount) VALUES
(101, 1, '2023-06-01', 5000),
(102, 2, '2023-06-02', 3000),
(103, 1, '2023-06-03', 7000);

-- 1. List all customer names with their order amount
SELECT c.CustName, o.Amount
FROM Customerss c
INNER JOIN Orders o ON c.CustID = o.CustID;

-- 2. Show all orders placed in June 2023
SELECT * FROM Orders
WHERE OrderDate BETWEEN '2023-06-01' AND '2023-06-30';

-- 3. List customers who placed more than one order
SELECT c.CustName, COUNT(o.OrderID) AS OrderCount
FROM Customerss c
INNER JOIN Orders o ON c.CustID = o.CustID
GROUP BY c.CustName
HAVING COUNT(o.OrderID) > 1;   --- Raj has 2 orders

-- 4. Find total order amount by each customer
SELECT c.CustName, SUM(o.Amount) AS TotalAmount
FROM Customerss c
INNER JOIN Orders o ON c.CustID = o.CustID
GROUP BY c.CustName;            --- Meena : 3000/-   ; Raj : 12000/-

-- 5. Display customers who never placed an order
SELECT c.CustName
FROM Customerss c
LEFT JOIN Orders o ON c.CustID = o.CustID
WHERE o.OrderID IS NULL;        --- Arjun