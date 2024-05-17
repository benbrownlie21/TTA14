-- TABLE FOR ITEMS OF STORE
CREATE TABLE items (
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(100) NOT NULL,
	item_catalog VARCHAR(100) NOT NULL,
	price INT NOT NULL,
	stock_level INT NOT NULL
);

-- TABLE FOR CUSTOMERS OF STORE
CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	age INT NOT NULL,
	created DATE DEFAULT CURRENT_DATE
);

-- REMOVE COLUMN age (not part of task --> it was crashing pgAdmin when trying to add the data)
ALTER TABLE customers
DROP COLUMN dob;


INSERT INTO items (item_name, item_catalog, price, stock_level)
VALUES ('Small Desk', 'Furniture', 100, 1200),
('Large Desk', 'Furniture', 300, 75),
('Fan', 'Electronics', 80, 120);


INSERT INTO customers (first_name, last_name, email)
VALUES ('Greg', 'Jones', 'greg@gmail.com'),
('Sandra', 'Jones', 'sandra@gmail.com'),
('Scott', 'Scott', 'scott@yahoo.com'),
('Trevor', 'Green', 't.green@hotmail.com'),
('Melanie', 'Johnson', 'mel@pmail.net');

-- PART 3
SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith'; -- no records found

SELECT * FROM customers WHERE last_name = 'Jones';

SELECT * FROM customers WHERE first_name <> 'Scott';