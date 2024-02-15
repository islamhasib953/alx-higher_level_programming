-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT c.id id, c.name name, s.name name
FROM cities c
JOIN states s
ON c.state_id=s.id
ORDER BY c.id;
