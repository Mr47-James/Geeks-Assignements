-- ============================================
-- PART 1 : Get all languages
-- ============================================

SELECT * FROM language;

--s--
-- ============================================
-- PART 2 : Get all films joined with their languages
-- ============================================

SELECT 
    f.title AS film_title,
    f.description,
    l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- This shows every film with its description and the language it was made in.

-- ============================================
-- PART 3 : Get all languages, even if there are no films
-- ============================================

SELECT 
    f.title AS film_title,
    f.description,
    l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;

-- LEFT JOIN ensures we see all languages,
-- even if no film exists in that language (film_title will appear as NULL).

-- ============================================
-- PART 4 : Create a new table called new_film
-- ============================================

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Add some new films
INSERT INTO new_film (name)
VALUES
('The Matrix Rebooted'),
('Toy Story Infinity'),
('Fast & Curious');

-- Check the data
SELECT * FROM new_film;

-- ============================================
-- PART 5 : Create a table for customer reviews
-- ============================================

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--s--

-- ============================================
-- PART 6 : Add 2 movie reviews (linked to valid films/languages)
-- ============================================

--s--
SELECT * FROM language;

--s--

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(1, 1, 'Amazing Sci-Fi Sequel', 9, 'Loved the visuals and deep story themes.'),
(2, 1, 'A fun continuation!', 8, 'Toy Story Infinity brings back nostalgia with humor.');

--s--
SELECT * FROM customer_review;

-- ============================================
-- PART 7 : Delete a film that has a review
-- ============================================

DELETE FROM new_film
WHERE id = 1;

--s--
SELECT * FROM customer_review;

