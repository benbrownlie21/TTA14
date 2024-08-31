SELECT * FROM movies.movie LIMIT 10;

SELECT * FROM movies.genre LIMIT 10;

SELECT * FROM movies.movie_genres LIMIT 10;

SELECT * FROM movies.production_company LIMIT 10;

SELECT * FROM movies.movie_company LIMIT 10;

SELECT * FROM movies.movie_cast LIMIT 10;

SELECT * FROM movies.person LIMIT 10;

SELECT * FROM movies.movie_crew LIMIT 10;

--Task 1: Rank Actors by Their Appearance in Movies - Display the actor’s name and their rank
SELECT pe.person_name, mo.title,
       DENSE_RANK() OVER (PARTITION BY mo.movie_id ORDER BY mc.cast_order DESC) AS dense_rank
FROM movies.person as pe
JOIN movies.movie_cast AS mc ON pe.person_id = mc.person_id
JOIN movies.movie AS mo ON mc.movie_id = mo.movie_id

--Task 2: Identify the Top Director by Average Movie Rating - Display the director’s name and their average rating
WITH AVG_Movie_Rating AS (
    SELECT mc.person_id, pe.person_name, mc.job,
           RANK() OVER (PARTITION BY mo.vote_average ORDER BY mc.person_id DESC) AS average_rating
    FROM movies.movie_crew as mc
	JOIN movies.person AS pe ON mc.person_id = pe.person_id
	JOIN movies.movie AS mo ON mc.movie_id = mo.movie_id
)
SELECT * FROM AVG_Movie_RATING
WHERE job = 'Director';

--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor - Display the actor’s name and the cumulative revenue.
SELECT pe.person_name, mo.title,
       SUM(mo.revenue) OVER (PARTITION BY pe.person_id ORDER BY pe.person_name) AS cumulative_revenue
FROM movies.person AS pe
JOIN movies.movie_cast AS mc ON pe.person_id = mc.person_id
JOIN movies.movie AS mo ON mc.movie_id = mo.movie_id

--Task 4: Identify the Director Whose Movies Have the Highest Total Budget - Display the director’s name and the total budget
WITH highest_total_budget AS (
    SELECT mc.person_id, pe.person_name, mc.job,
           RANK() OVER (PARTITION BY mo.budget ORDER BY mc.person_id DESC) AS highest_budget
    FROM movies.movie_crew as mc
	JOIN movies.person AS pe ON mc.person_id = pe.person_id
	JOIN movies.movie AS mo ON mc.movie_id = mo.movie_id
)
SELECT * FROM highest_total_budget
WHERE job = 'Director'
ORDER BY highest_budget DESC;


SELECT * FROM movies.person LIMIT 10;

SELECT * FROM movies.movie_crew LIMIT 10;