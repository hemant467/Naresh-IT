-- 🔸 DROP vs TRUNCATE

-- DROP:
-- • Removes the entire table including structure and data
-- • Cannot be rolled back
-- • Removes all constraints and permissions
-- • TOTAL table will be deleted
-- • SYNTAX : DROP TABLE table_name;

-- TRUNCATE:
-- • Deletes only the data, keeps table structure
-- • Cannot be rolled back (DDL)
-- • Resets IDENTITY by default
-- • Only rows will be DELETED but table remains the SAME
-- • SYNTAX : TRUNCATE TABLE table_name;

-- 🔸 NULL vs NOT NULL

-- NULL:
-- • Allows column to be empty
-- • Used for optional fields

-- NOT NULL:
-- • Does NOT allow empty values
-- • Used for required fields

-- • SYNTAX :

-- Creating a table with NULL and NOT NULL constraints
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,   -- Required field
    email VARCHAR(100) NULL       -- Optional field
);

-- Inserting with NULL value (allowed)
INSERT INTO employees (id, name, email)
VALUES (1, 'Suresh', NULL);

-- Inserting with missing NOT NULL field (will fail)
-- This will raise an error:
-- INSERT INTO employees (id, email) VALUES (2, 'test@example.com');


-- 🔸 DEFAULT vs Hardcoded INSERT

-- DEFAULT:
-- • Defined in table schema
-- • Automatically used when value is omitted

-- Hardcoded:
-- • Manually specified in every INSERT
-- • Needs to be updated everywhere if changed

-- • SYNTAX :
-- DEFAULT: Define default value in table schema
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'Pending'  -- Default value
);

-- Insert using DEFAULT (status will be 'Pending')
INSERT INTO orders (order_id) VALUES (101);

-- Hardcoded INSERT: Manually provide value
INSERT INTO orders (order_id, status) VALUES (102, 'Shipped');