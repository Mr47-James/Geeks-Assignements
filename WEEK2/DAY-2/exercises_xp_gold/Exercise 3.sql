-- ================================================
-- PART I : TABLE CREATION & DATA INSERTION
-- ================================================


CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    price INT
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50)
);
--s--


INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

--s--


INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

--s--


SELECT * FROM items;
SELECT * FROM customers;

--s--

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    item_id INT REFERENCES items(id),
    quantity_purchased INT
);

--s--

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Scott' AND lastname = 'Scott'),
    (SELECT id FROM items WHERE name = 'Fan'),
    1
);
--s--

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Melanie' AND lastname = 'Johnson'),
    (SELECT id FROM items WHERE name = 'Large Desk'),
    10
);

--s--

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Greg' AND lastname = 'Jones'),
    (SELECT id FROM items WHERE name = 'Small Desk'),
    2
);

--s--

SELECT * FROM purchases;

--s--

-- ================================================
-- PART II : DATA QUERIES & ANALYSIS
-- ================================================

SELECT * FROM purchases;
--s--

SELECT 
    purchases.id AS purchase_id,
    customers.firstname,
    customers.lastname,
    purchases.item_id,
    purchases.quantity_purchased
FROM purchases
JOIN customers ON purchases.customer_id = customers.id;

--s--

SELECT * 
FROM purchases
WHERE customer_id = 5;

--s--

SELECT * 
FROM purchases
WHERE item_id IN (
    SELECT id FROM items WHERE name IN ('Large Desk', 'Small Desk')
);

--s--

SELECT 
    c.firstname,
    c.lastname,
    i.name AS item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id
JOIN items i ON p.item_id = i.id;

--s--

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 1);
