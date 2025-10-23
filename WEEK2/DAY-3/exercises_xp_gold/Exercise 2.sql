-- ============================================
-- PART 1 : Stores and their city/country
-- ============================================

SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

--s--

-- ============================================
-- PART 2 : Total viewing time (in minutes) per store
-- Excluding unreturned rentals
-- ============================================

SELECT s.store_id, SUM(f.length) AS total_viewing_minutes
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN film f ON i.film_id = f.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL OR r.rental_id IS NULL
GROUP BY s.store_id;

--s--

-- ============================================
-- PART 3 : All customers in the cities where stores are located
-- ============================================

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT ci2.city_id
    FROM store s
    JOIN address a2 ON s.address_id = a2.address_id
    JOIN city ci2 ON a2.city_id = ci2.city_id
);

--s--

-- ============================================
-- PART 4 : All customers in the countries where stores are located
-- ============================================

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT co2.country_id
    FROM store s
    JOIN address a2 ON s.address_id = a2.address_id
    JOIN city ci2 ON a2.city_id = ci2.city_id
    JOIN country co2 ON ci2.country_id = co2.country_id
);

--s--

-- ============================================
-- PART 5 : Safe movie list (no horror or scary words)
-- ============================================

CREATE VIEW safe_movies AS
SELECT f.film_id, f.title, f.description, f.length
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND LOWER(f.title) NOT LIKE '%beast%'
AND LOWER(f.title) NOT LIKE '%monster%'
AND LOWER(f.title) NOT LIKE '%ghost%'
AND LOWER(f.title) NOT LIKE '%dead%'
AND LOWER(f.title) NOT LIKE '%zombie%'
AND LOWER(f.title) NOT LIKE '%undead%';

--s--

-- ============================================
-- PART 6 : Total safe viewing time (minutes, hours, days)
-- ============================================

SELECT 
    SUM(length) AS total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS total_hours,
    ROUND(SUM(length) / 1440.0, 2) AS total_days
FROM safe_movies;

--s--

-- ============================================
-- PART 7 : Total general viewing time (minutes, hours, days)
-- ============================================

SELECT 
    SUM(length) AS total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS total_hours,
    ROUND(SUM(length) / 1440.0, 2) AS total_days
FROM film;
