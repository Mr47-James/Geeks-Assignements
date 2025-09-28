-- 1. Fetch the last 2 customers in alphabetical order (A-Z), exclude id
SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC
LIMIT 2 OFFSET (
    (SELECT COUNT(*) FROM customers) - 2
);

-- 2. Delete all purchases made by Scott
DELETE FROM purchases
WHERE customer_id = (
    SELECT id FROM customers
    WHERE first_name = 'Scott'
);

-- 3. Check if Scott still exists in the customers table
SELECT *
FROM customers
WHERE first_name = 'Scott';

-- 4. Find all purchases joined with customers,
-- so Scott’s order appears but names are blank → LEFT JOIN
SELECT p.id AS purchase_id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.purchase_date
FROM purchases p
LEFT JOIN customers c
ON p.customer_id = c.id;

-- 5. Find all purchases joined with customers,
-- so Scott’s order does NOT appear → INNER JOIN
SELECT p.id AS purchase_id,
       c.first_name,
       c.last_name,
       p.item_id,
       p.purchase_date
FROM purchases p
INNER JOIN customers c
ON p.customer_id = c.id;
