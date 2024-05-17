SELECT * FROM actors;

SELECT COUNT(*) FROM actors;

INSERT INTO actors(first_name, last_name)
VALUES ('Robert', 'Hill');

-- result: ERROR:  null value in column "age" of relation "actors" violates not-null constraint
-- 		   DETAIL:  Failing row contains (7, Robert, Hill, null, null).