SELECT * FROM movies.movie LIMIT 10;

SELECT * FROM movies.genre LIMIT 10;

SELECT * FROM movies.movie_genres LIMIT 10;

SELECT * FROM movies.production_company LIMIT 10;

SELECT * FROM movies.movie_company LIMIT 10;

--Task 1: Rank Movies by Popularity within Each Genre
SELECT mo.movie_id, mo.title, ge.genre_name,
       RANK() OVER (PARTITION BY mo.movie_id ORDER BY ge.genre_name DESC) AS rank
FROM movies.movie AS mo
JOIN movies.movie_genres AS mg ON mo.movie_id = mg.movie_id
JOIN movies.genre AS ge ON mg.genre_id = ge.genre_id;

--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
SELECT mo.movie_id, mo.title, pc.company_name, mo.revenue,
       NTILE(4) OVER (PARTITION BY pc.company_id ORDER BY mo.revenue DESC) AS quartile
FROM movies.movie AS mo
JOIN movies.movie_company AS mc ON mo.movie_id = mc.movie_id
JOIN movies.production_company AS pc ON mc.company_id = pc.company_id

--Task 3: Calculate the Running Total of Movie Budgets for Each Genre
SELECT mo.movie_id, mo.title, ge.genre_name, mo.budget,
       SUM(mo.budget) OVER (ORDER BY mo.title ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS running_total_budget
FROM movies.movie AS mo
JOIN movies.movie_genres AS mg ON mo.movie_id = mg.movie_id
JOIN movies.genre AS ge ON mg.genre_id = ge.genre_id;

--Task 4: Identify the Most Recent Movie for Each Genre - Display the genre name, movie title, and release date
SELECT mo.title, ge.genre_name, mo.release_date,
       FIRST_VALUE(mo.release_date) OVER (PARTITION BY ge.genre_name ORDER BY mo.release_date DESC) AS most_recent_movie_in_genre
FROM movies.movie AS mo
JOIN movies.movie_genres AS mg ON mo.movie_id = mg.movie_id
JOIN movies.genre AS ge ON mg.genre_id = ge.genre_id;

