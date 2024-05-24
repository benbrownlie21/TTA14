CREATE TABLE Book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	author VARCHAR(100) NOT NULL
);

INSERT INTO Book (title, author) VALUES
('Alice in Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

CREATE TABLE Student (
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE,
	age INT CHECK (age <= 15)
);

INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

CREATE TABLE Library (
	book_id INT,
	student_id INT,
	borrowed_date DATE,
	CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_student FOREIGN KEY(student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO library (student_id, book_id, borrowed_date) VALUES
(1, 1, '2022-02-15'),
(4, 3, '2021-03-03'),
(2, 1, '2021-05-23'),
(4, 2, '2021-08-12');

-- Select all the columns from the junction table
select * from library;

-- Select the name of the student and the title of the borrowed books
SELECT su.name, bo.title
FROM library AS li
JOIN student AS su ON li.student_id = su.student_id
JOIN book AS bo ON li.book_id = bo.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT ROUND(AVG(su.age),1) AS avg_age
FROM library AS li
JOIN student AS su ON li.student_id = su.student_id
JOIN book AS bo ON li.book_id = bo.book_id
WHERE bo.title = 'Alice in Wonderland';

--Delete a student from the Student table, what happened in the junction table ? --> records for student 2 have been removed from the library table
DELETE FROM student
WHERE student_id = 2;

SELECT * FROM library;