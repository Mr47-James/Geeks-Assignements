CREATE DATABASE bootcamp;
\c bootcamp;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

INSERT INTO students (id, first_name, last_name, birth_date) VALUES
(1, 'Marc', 'Benichou', '1998-11-02'),
(2, 'Yoan', 'Cohen', '2010-12-03'),
(3, 'Lea', 'Benichou', '1987-07-27'),
(4, 'Amelia', 'Dux', '1996-04-07'),
(5, 'David', 'Grez', '2003-06-14'),
(6, 'Omer', 'Simpson', '1980-10-03');

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Latros', 'AI', '2000-05-15');

--s--
SELECT * FROM students;

--s--
UPDATE students
SET birth_date = '1998-11-02'
WHERE (first_name = 'Lea' AND last_name = 'Benichou')
   OR (first_name = 'Marc' AND last_name = 'Benichou');

--s--
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

--s--
DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';

--s--
SELECT COUNT(*) AS total_students FROM students;

--s--
SELECT COUNT(*) AS born_after_2000
FROM students
WHERE birth_date > '2000-01-01';


--s--
ALTER TABLE students
ADD COLUMN math_grade INT;

--s--
UPDATE students
SET math_grade = 80
WHERE id = 1;

--s--
UPDATE students
SET math_grade = 90
WHERE id IN (2, 4);

--s--
UPDATE students
SET math_grade = 40
WHERE id = 6;
--s--
SELECT * FROM students;

--s--
SELECT COUNT(*) AS grade_above_83
FROM students
WHERE math_grade > 83;

--s--
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT first_name, last_name, birth_date, 70
FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;

--s--
SELECT * FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson';


--s--
SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name
ORDER BY first_name;

--s--
SELECT SUM(math_grade) AS total_grades_sum
FROM students;
