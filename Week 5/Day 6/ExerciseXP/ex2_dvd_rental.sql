SELECT * FROM film;
SELECT * FROM language;

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 3
WHERE film_id = 384

UPDATE film
SET language_id = 5
WHERE film_id = 98

UPDATE film
SET language_id = 4
WHERE film_id = 26

SELECT * FROM film WHERE film_id IN (384, 98, 26);

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- the customer_address_id is the foreign key it references the address table and address_id column and the update is cascaded but delete is restricted

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;
-- this was easy as the foreign key wasn't restricted

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(rental_id) AS NUM_OUTSTANDING
FROM rental
WHERE return_date IS NULL;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT fi.film_id, fi.title, fi.rental_rate, fi.replacement_cost
FROM rental AS re
JOIN inventory AS inv ON re.inventory_id = inv.inventory_id
JOIN film AS fi ON inv.film_id = fi.film_id
WHERE re.return_date IS NULL
ORDER BY replacement_cost DESC
LIMIT 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
SELECT * FROM film;
SELECT * FROM film_actor;
SELECT * FROM actor;
SELECT * FROM film_category;
SELECT * FROM category;
SELECT * FROM customer;
SELECT * FROM rental;
SELECT * FROM inventory;
	
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe. --> Park Citizen
SELECT fi.title, fi.description
FROM film AS fi
JOIN film_actor AS fia ON fi.film_id = fia.film_id
JOIN actor AS ac ON fia.actor_id = ac.actor_id
WHERE ac.first_name = 'Penelope' AND ac.last_name = 'Monroe'
AND fi.description LIKE '%Sumo Wrestler%'

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”. --> Cupboard Sinners
SELECT fi.title
FROM film AS  fi
JOIN film_category AS fic ON fi.film_id = fic.film_id
JOIN category AS ca ON fic.category_id = ca.category_id
WHERE fi.length < 60
AND fi.rating = 'R'
AND ca.name = 'Documentary';

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005. --> Sugar Wonk
SELECT fi.title
FROM FILM as fi
JOIN inventory AS inv ON fi.film_id = inv.film_id
JOIN rental AS re ON inv.inventory_id = re.inventory_id
JOIN customer AS cu ON re.customer_id = cu.customer_id
WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
AND fi.rental_rate > 4
AND re.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace. --> Stone Fire
SELECT fi.title, fi.description, fi.replacement_cost
FROM FILM AS fi
JOIN inventory AS inv ON fi.film_id = inv.film_id
JOIN rental AS re ON inv.inventory_id = re.inventory_id
JOIN customer AS cu ON re.customer_id = cu.customer_id
WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
AND fi.description LIKE '%Boat%'
GROUP BY 1, 2, 3
ORDER BY fi.replacement_cost DESC
LIMIT 1;

