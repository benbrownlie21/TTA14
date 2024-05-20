SELECT * FROM ORDERS;
SELECT * FROM CUSTOMERS;

-- All items, ordered by price (lowest to highest).
SELECT * FROM ORDERS
ORDER BY price ASC;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM ORDERS
WHERE price > 80
ORDER BY price DESC;

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT first_name, last_name, dob, signup_date, email
FROM CUSTOMERS
ORDER BY first_name ASC
LIMIT 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name
FROM CUSTOMERS
ORDER BY last_name DESC;
