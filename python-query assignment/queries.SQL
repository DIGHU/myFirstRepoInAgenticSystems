-- Create Table
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER,
    passed INTEGER,
    class INTEGER
);

-- Insert Data
INSERT INTO students (id, name, score, passed, class) VALUES
(1, 'Aarav', 92, 1, 10),
(2, 'Diya', 76, 1, 10),
(3, 'Rohan', 65, 0, 9),
(4, 'Meera', 88, 1, 10),
(5, 'Kabir', 54, 0, 9),
(6, 'Ananya', 95, 1, 10),
(7, 'Rahul', 81, 1, 9),
(8, 'Sneha', 73, 1, 9),
(9, 'Arjun', 84, 1, 10),
(10, 'Kavya', 69, 0, 9);

-- Queries
SELECT * FROM students;

SELECT * FROM students WHERE passed = 1;

SELECT * FROM students WHERE passed = 0;

SELECT * FROM students ORDER BY score DESC;

SELECT * FROM students ORDER BY score DESC LIMIT 1;

SELECT AVG(score) FROM students;

SELECT id, name, score,
RANK() OVER (ORDER BY score DESC) AS rank
FROM students;

SELECT * FROM students WHERE class = 10;