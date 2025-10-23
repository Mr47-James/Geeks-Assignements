-- ============================================
-- PART 1 : Rentals which are out (not returned)
-- ============================================

SELECT *
FROM rental
WHERE return_date IS NULL;

--s--

-- ============================================
-- PART 2 : Customers who have not returned rentals
-- ============================================

SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS unreturned_count
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name;

--s--

-- ============================================
-- PART 3 : Action films with Joe Swank
-- ============================================

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe'
  AND a.last_name = 'Swank'
  AND c.name = 'Action';

--s--

-- ============================================
-- PART 4 : Shortcut using a VIEW
-- ============================================

CREATE VIEW unreturned_rentals AS
SELECT r.rental_id, r.customer_id, r.inventory_id, r.rental_date
FROM rental r
WHERE r.return_date IS NULL;
