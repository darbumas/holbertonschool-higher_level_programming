-- lists all cities that can be found in db 'hbtn_0d_usa' from California
-- results are sorted in ascending order by cities.id
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California')
;
