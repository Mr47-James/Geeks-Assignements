-- ============================================
-- PART 1 : Retrieve all G or PG films not currently rented
-- ============================================

SELECT DISTINCT f.film_id, f.title, f.rating
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G', 'PG')
AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);

--s--

-- ============================================
-- PART 2 : Create waiting list table for children’s movies
-- ============================================

CREATE TABLE children_waitlist (
    wait_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES film(film_id) ON DELETE CASCADE,
    child_name VARCHAR(100) NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--s--

-- ============================================
-- PART 3 : Retrieve number of people waiting per children’s DVD
-- ============================================

SELECT f.title, COUNT(w.wait_id) AS waiting_count
FROM film f
LEFT JOIN children_waitlist w ON f.film_id = w.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.title
ORDER BY waiting_count DESC;
