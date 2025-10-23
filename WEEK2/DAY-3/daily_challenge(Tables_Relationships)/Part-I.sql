-- ============================================
-- PART I : CUSTOMER AND CUSTOMER PROFILE
-- ============================================

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE REFERENCES customer(id) ON DELETE CASCADE
);

--s--

-- Insert customers
INSERT INTO customer (first_name, last_name)
VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

--s--

-- Insert customer profiles (using subqueries)
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
(TRUE, (SELECT id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')),
(FALSE, (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

--s--

-- LoggedIn customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

--s--

-- All customers and their login status
SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

--s--

-- Number of customers not logged in
SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;
