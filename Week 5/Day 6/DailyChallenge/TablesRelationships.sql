CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	customer_id INT,
	CONSTRAINT fk_customer
		FOREIGN KEY(customer_id)
			REFERENCES customer(id)
);

INSERT INTO customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

SELECT * FROM customer;

INSERT INTO customer_profile (isLoggedIn, customer_id) VALUES
(TRUE, 1),
(FALSE, 2);

-- The first_name of the LoggedIn customers
SELECT cu.first_name
FROM customer_profile AS cp
JOIN customer AS cu ON cp.customer_id = cu.id
WHERE cp.isloggedin = TRUE
LIMIT 1;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT cu.first_name, cp.id, cp.isLoggedIn, cp.customer_id
FROM customer_profile AS cp
RIGHT JOIN customer AS cu ON cp.customer_id = cu.id;

-- The number of customers that are not LoggedIn
SELECT COUNT(id)
FROM customer_profile
WHERE isLoggedIN = FALSE
