SELECT * FROM olympics.person LIMIT 10;

SELECT * FROM olympics.person_region LIMIT 10;

SELECT * FROM olympics.competitor_event ORDER BY competitor_id DESC LIMIT 10;

SELECT * FROM olympics.games_competitor LIMIT 10;

SELECT * FROM olympics.medal LIMIT 10;

SELECT * FROM olympics.noc_region LIMIT 10;

--Task 1
SELECT pe.id, pe.full_name, ce.medal_id
FROM olympics.person AS pe
JOIN olympics.games_competitor AS gc ON pe.id = gc.person_id
JOIN olympics.competitor_event AS ce ON gc.person_id = ce.competitor_id
WHERE gc.age > (SELECT ROUND(AVG(age),0)
                FROM olympics.games_competitor
                WHERE person_id = pe.id)
AND ce.medal_id <> 4
GROUP BY 1, 3
ORDER BY 2 ASC;

--Task 2
SELECT region_id, COUNT(*) FROM olympics.person_region GROUP BY 1 ORDER BY 2 DESC LIMIT 5;

SELECT competitor_id, COUNT(*) AS EVENT_COUNT FROM olympics.competitor_event WHERE medal_id <> 4 GROUP BY 1 ORDER BY 2 DESC;

SELECT region_name, region_id, COUNT(DISTINCT competitor_id) AS unique_competitors
FROM (
    SELECT nr.region_name, re.region_id, ce.competitor_id, COUNT(DISTINCT ce.event_id) AS event_count
    FROM olympics.person_region AS re
	JOIN olympics.competitor_event AS ce ON re.person_id = ce.competitor_id
	JOIN olympics.noc_region AS nr ON re.region_id = nr.id
    GROUP BY re.region_id, ce.competitor_id, nr.region_name
    HAVING COUNT(DISTINCT ce.event_id) >= 3
) AS filtered_competitors
GROUP BY region_id, region_name
ORDER BY unique_competitors DESC
LIMIT 5;

--Task 3
CREATE TEMPORARY TABLE Medal_Count_2 AS
SELECT 
	competitor_id,
	COUNT(event_id) AS total_medals
FROM olympics.competitor_event
WHERE medal_id <> 4
GROUP BY competitor_id
HAVING COUNT(event_id) >= 2;

SELECT *
FROM Medal_Count_2
ORDER BY total_medals DESC;

--Task 4
CREATE TEMPORARY TABLE No_Medals AS
SELECT 
	competitor_id,
	medal_id
FROM olympics.competitor_event
GROUP BY 1, 2

SELECT *
FROM No_Medals
ORDER BY medal_id DESC;

DELETE FROM No_Medals WHERE medal_id = 4;