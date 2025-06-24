
-- ========================================
-- Q1) CREATE TABLE: Employees
-- ========================================
CREATE TABLE Employe (
    EmpID INT IDENTITY(1,1) PRIMARY KEY,          -- Auto-incremented primary key
    Name VARCHAR(50) NOT NULL,                    -- Name cannot be NULL
    Department VARCHAR(30) NOT NULL,              -- Department cannot be NULL
    JoiningDate DATE DEFAULT GETDATE(),           -- Default to current date
    Salary DECIMAL(10,2) DEFAULT 25000.00         -- Default salary if not provided
);
GO

-- ========================================
-- Q2) INSERT RECORDS (omit EmpID and JoiningDate)
-- ========================================
INSERT INTO Employe (Name, Department, Salary)
VALUES ('Ramesh', 'HR', 30000.00);

INSERT INTO Employe (Name, Department)
VALUES ('Suresh', 'IT');  -- Salary will use default 25000.00

INSERT INTO Employe (Name, Department, Salary)
VALUES ('Priya', 'Finance', 28000.00);
GO

-- ========================================
-- Q3a) Display all employee records
-- ========================================
SELECT * FROM Employe;
GO

-- ========================================
-- Q3b) Display employees with salary above 26000
-- ========================================
SELECT * FROM Employe
WHERE Salary > 26000;
GO

-- ========================================
-- Q3c) Drop the Employees table
-- ========================================
DROP TABLE IF EXISTS Employe;
GO

-- ========================================
-- Q3d) Recreate the table and reinsert data
-- ========================================
CREATE TABLE Employe (
    EmpID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Department VARCHAR(30) NOT NULL,
    JoiningDate DATE DEFAULT GETDATE(),
    Salary DECIMAL(10,2) DEFAULT 25000.00
);
GO

-- Reinserting same data
INSERT INTO Employe (Name, Department, Salary)
VALUES ('Ramesh', 'HR', 30000.00);

INSERT INTO Employe (Name, Department)
VALUES ('Suresh', 'IT');

INSERT INTO Employe (Name, Department, Salary)
VALUES ('Priya', 'Finance', 28000.00);
GO

-- ========================================
-- Q3e) TRUNCATE and show the difference
-- ========================================
-- View before TRUNCATE
SELECT * FROM Employe;
GO

-- TRUNCATE removes data but keeps structure
TRUNCATE TABLE Employe;
GO

-- View after TRUNCATE (should return 0 rows)
SELECT * FROM Employe;
GO

-- Note:
-- TRUNCATE: Deletes all rows, keeps structure
-- DROP: Deletes both data and structure
