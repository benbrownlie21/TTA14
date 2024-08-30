SELECT * FROM olympics.person LIMIT 10;

SELECT * FROM olympics.person_region LIMIT 10;

SELECT * FROM olympics.competitor_event ORDER BY competitor_id DESC LIMIT 10;

SELECT competitor_id, count(distinct event_id) FROM olympics.competitor_event GROUP BY 1 HAVING count(distinct event_id) > 1 ORDER BY 2 DESC LIMIT 10;

SELECT * FROM olympics.games_competitor LIMIT 10;

SELECT * FROM olympics.medal LIMIT 10;

SELECT * FROM olympics.noc_region LIMIT 10;

SELECT * FROM olympics.games ORDER BY games_year DESC LIMIT 10;

SELECT * FROM olympics.games_competitor LIMIT 10;

--Task 1
UPDATE olympics.person
SET height = (SELECT AVG(height) FROM olympics.person);

--Task 2
CREATE TEMPORARY TABLE Num_events AS
SELECT competitor_id, count(distinct event_id) 
FROM olympics.competitor_event 
GROUP BY 1 
HAVING count(distinct event_id) > 1 
ORDER BY 2 DESC;

INSERT INTO Num_events
VALUES 
	(34459032, 84),
	(34459033, 22),
	(34459034, 16),
	(34459035, 32);
	
SELECT * FROM Num_events ORDER BY 2 DESC LIMIT 10;

--Task 3
SELECT pr.region_id, nr.region_name, 
       ROUND(AVG(medals_per_competitor), 2) AS avg_medals_per_competitor
FROM (
    SELECT ce.competitor_id, 
           COUNT(ce.medal_id) AS medals_per_competitor
    FROM olympics.competitor_event AS ce
    GROUP BY ce.competitor_id
) AS competitor_medals
JOIN olympics.person_region AS pr ON competitor_medals.competitor_id = pr.person_id
JOIN olympics.noc_region AS nr ON pr.region_id = nr.id
GROUP BY pr.region_id, nr.region_name
HAVING AVG(medals_per_competitor) > (
    SELECT AVG(medals_per_competitor)
    FROM (
        SELECT ce.competitor_id, 
               COUNT(ce.medal_id) AS medals_per_competitor
        FROM olympics.competitor_event AS ce
        GROUP BY ce.competitor_id
    ) AS overall_medals
)
ORDER BY avg_medals_per_competitor DESC;

--Task 4
CREATE TEMPORARY TABLE participant_over_seasons AS
SELECT gc.person_id, gc.games_id, ga.season, ga.games_name
FROM olympics.games_competitor AS gc
JOIN olympics.games AS ga ON gc.games_id = ga.id
GROUP BY 1, 2, 3, 4;

SELECT 
	person_id
FROM participant_over_seasons 
WHERE season IN ('Summer', 'Winter')
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2
ORDER BY person_id;

