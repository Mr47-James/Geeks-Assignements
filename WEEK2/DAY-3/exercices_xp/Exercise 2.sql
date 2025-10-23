-- ============================================
-- PART 1 : Update language of some films
-- ============================================

UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

--s--

-- ============================================
-- PART 2 : Foreign keys defined for customer table
-- ============================================

-- Check foreign key references
\d customer;

--s--

-- ============================================
-- PART 3 : Drop customer_review table
-- ============================================

DROP TABLE customer_review;

--s--

-- ============================================
-- PART 4 : Find how many rentals are still outstanding
-- ============================================

SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

--s--

-- ============================================
-- PART 5 : Find the 30 most expensive outstanding movies
-- ============================================

SELECT f.film_id, f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

--s--

-- ============================================
-- PART 6 : 1st film - about a sumo wrestler, actor Penelope Monroe
-- ============================================

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope'
  AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

--s--

-- ============================================
-- PART 7 : 2nd film - short documentary (< 1h) rated “R”
-- ============================================

SELECT title
FROM film
WHERE length < 60
  AND rating = 'R'
  AND description ILIKE '%documentary%';

--s--

-- ============================================
-- PART 8 : 3rd film - rented by Matthew Mahan, paid > $4, returned between 28 July and 1 Aug 2005
-- ============================================

SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew'
  AND c.last_name = 'Mahan'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

--s--

-- ============================================
-- PART 9 : 4th film - watched by Matthew Mahan, title/description contains "boat", expensive to replace
-- ============================================

SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew'
  AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;
