-- ============================================
-- PART 1 : CREATE TABLES
-- ============================================

CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

--s--

-- ============================================
-- PART 2 : SAMPLE DATA
-- ============================================

INSERT INTO product_orders (order_date) VALUES (CURRENT_DATE), (CURRENT_DATE);

INSERT INTO items (order_id, item_name, price)
VALUES
(1, 'Laptop', 800.00),
(1, 'Mouse', 20.00),
(1, 'Keyboard', 50.00),
(2, 'Monitor', 200.00),
(2, 'HDMI Cable', 15.00);

--s--

-- ============================================
-- PART 3 : FUNCTION - TOTAL PRICE FOR A GIVEN ORDER
-- ============================================

CREATE OR REPLACE FUNCTION get_order_total(order_id_input INT)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC;
BEGIN
    SELECT SUM(price) INTO total_price
    FROM items
    WHERE order_id = order_id_input;
    RETURN COALESCE(total_price, 0);
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- SELECT get_order_total(1);

--s--

-- ============================================
-- BONUS PART 4 : USERS AND RELATIONSHIP
-- ============================================

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

ALTER TABLE product_orders
ADD COLUMN user_id INT REFERENCES users(user_id) ON DELETE CASCADE;

--s--

-- ============================================
-- PART 5 : FUNCTION - TOTAL PRICE FOR A USER'S GIVEN ORDER
-- ============================================

CREATE OR REPLACE FUNCTION get_user_order_total(user_id_input INT, order_id_input INT)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC;
BEGIN
    SELECT SUM(i.price) INTO total_price
    FROM items i
    JOIN product_orders o ON i.order_id = o.order_id
    WHERE o.user_id = user_id_input
      AND o.order_id = order_id_input;
    RETURN COALESCE(total_price, 0);
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- SELECT get_user_order_total(1, 1);
