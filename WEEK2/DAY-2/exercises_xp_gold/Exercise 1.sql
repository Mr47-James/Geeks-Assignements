SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC;

--s--

SELECT film_id, title, rating
FROM film
WHERE rating IN ('G', 'PG-13');

--s--

SELECT title, rating, length, rental_rate
FROM film
WHERE rating IN ('G', 'PG-13')
  AND length < 120
  AND rental_rate < 3.00
ORDER BY title ASC;

--s--

SELECT * FROM customer WHERE customer_id = 5;

UPDATE customer
SET first_name = 'Latros',
    last_name = 'Smith',
    email = 'latros.smith@example.com'
WHERE customer_id = 5;
--s--
SELECT address_id
FROM customer
WHERE customer_id = 5;

SELECT * FROM address WHERE address_id = (SELECT address_id FROM customer WHERE customer_id = 5);

UPDATE address
SET address = '123 Elm Street',
    address2 = 'Apartment 4B',
    district = 'Central City',
    postal_code = '40000',
    phone = '555-1234'
WHERE address_id = (SELECT address_id FROM customer WHERE customer_id = 5);
