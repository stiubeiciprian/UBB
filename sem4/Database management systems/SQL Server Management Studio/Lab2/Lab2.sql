
-- Statement that violate integrity constraints
INSERT INTO Employee (employeeId, firstName, lastName, birthDate) VALUES (1, 'John', 'Doe', '1999-01-01');

INSERT INTO Employee (firstName, lastName, birthDate) VALUES ('John', 'Doe', 'not-a-date');

-- Data Insertion for at least 4 tables

INSERT INTO Employee (firstName, lastName, birthDate) VALUES ('Winston', 'Smith', '1984-12-12'),('Jane', 'Doe', '1956-03-11');
INSERT INTO Salary (employeeId, [value], fromDate, toDate) VALUES (2, 5000, '2017-02-11', '2019-06-10'),(2, 7000, '2019-06-11', NULL),(6, 4500, '2018-02-11', '2019-06-10'),(4, 6700, '2019-09-11', NULL);
INSERT INTO MeetingRoom (roomName, seatsNumber) VALUES ('Water room', 35),('Fire room', 40),('Earth room', 40),('Air room',45),('Tornado room', 50),('Cube room', 65);
INSERT INTO BookMeetingRoom (employeeId,roomId,bookingDate) VALUES (1,1,'2019-11-04'), (2,3,'2019-11-04'), (10,2,'2019-11-04'), (11,6,'2019-12-04'),(2,3,'2019-12-04'),(2,5,'2019-11-05');


-- Data Update for at least 3 tables

UPDATE MeetingRoom SET seatsNumber = 42 WHERE seatsNumber = 40;
UPDATE BookMeetingRoom SET bookingDate = '2019-12-03' WHERE employeeId = 1 AND bookingDate like '2019-11-04';
UPDATE Employee SET lastName = 'Jennifer' WHERE firstName LIKE 'Jane';

-- Data Deletion for at least 2 tables

DELETE FROM BookMeetingRoom WHERE employeeId = 7;
DELETE FROM Employee WHERE firstName LIKE 'Sherlock' AND lastName LIKE 'Holmes';

--------------SELECT Queries

-- a. 2 queries with the union operation; use UNION [ALL] and OR;

SELECT employeeId, firstName, lastName
FROM Employee
WHERE lastName LIKE 'J%'
UNION
SELECT employeeId, firstName, lastName
FROM Employee 
WHERE lastName LIKE 'A%'


SELECT employeeId, firstName, lastName
FROM Employee 
WHERE lastName LIKE 'A%' OR lastName LIKE 'J%'


-- b. 2 queries with the intersection operation; use INTERSECT and IN;



SELECT roomName, seatsNumber
FROM MeetingRoom
WHERE seatsNumber IN (40,42,45)

SELECT roomName, seatsNumber
FROM MeetingRoom
WHERE seatsNumber = 40
INTERSECT
SELECT roomName, seatsNumber
FROM MeetingRoom
WHERE seatsNumber = 45

-- c. 2 queries with the difference operation; use EXCEPT and NOT IN;

SELECT *
FROM Salary
WHERE value NOT IN (4500, 5000)

SELECT *
FROM Salary
EXCEPT
SELECT *
FROM Salary
WHERE value <= 5000


-- d. 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN; one query will join at least 3 tables, while another one will join at least two many-to-many relationships;

SELECT e.firstName, e.lastName, s.[value]
FROM Employee e
INNER JOIN Salary s
ON e.employeeId = s.employeeId

SELECT m.roomName, b.bookingDate
FROM MeetingRoom m
FULL JOIN BookMeetingRoom b
ON m.roomId = b.roomId

SELECT e.firstName, e.lastName, s.[value], t.titleName
FROM Employee e
LEFT JOIN Title t
ON e.employeeId = t.employeeId
LEFT JOIN Salary s
ON s.employeeId = e.employeeId

SELECT e.firstName, e.lastName, w.fromDate, w.toDate, p.title
FROM Employee e
INNER JOIN WorksOn w
ON w.employeeId = e.employeeId
RIGHT JOIN Project p
ON p.projectId = w.projectId




-- e. 2 queries using the IN operator to introduce a subquery in the WHERE clause; in at least one query, the subquery should include a subquery in its own WHERE clause;

SELECT e.firstName, e.lastName, s.[value]
FROM Employee e, Salary s
WHERE e.employeeId = s.employeeId AND e.employeeId IN ( SELECT DISTINCT b.employeeId
														FROM BookMeetingRoom b
														)

SELECT e.firstName, e.lastName
FROM Employee e
WHERE e.employeeId IN ( SELECT DISTINCT w.employeeId
						FROM WorksOn w
						WHERE fromDate > GETDATE()
						)

-- f. 2 queries using the EXISTS operator to introduce a subquery in the WHERE clause;

SELECT e.firstName, e.lastName
FROM Employee e
WHERE EXISTS ( SELECT DISTINCT w.employeeId
						FROM WorksOn w
						)

SELECT s.value
FROM Salary s
WHERE EXISTS ( SELECT e.employeeId
			   FROM Employee e
			   WHERE e.birthDate > '1990-01-01'
			   )

-- g. 2 queries with a subquery in the FROM clause;                             

SELECT sq.employeeId, sq.firstName, sq.lastName, sq.title
FROM (SELECT e.employeeId, e.firstName, e.lastName, p.title, w.fromDate, w.toDate
	  FROM Employee e, WorksOn w, Project p
	  WHERE e.employeeId = w.employeeId AND p.projectId = w.projectId
	  ) sq
WHERE sq.fromDate > GETDATE()

SELECT sq.firstName,sq.lastName, sq.fromDate, sq.departmentName
FROM (SELECT e.firstName, e.lastName, ea.fromDate, d.departmentName
	  FROM Employee e, EmployedAt ea, Department d 
	  WHERE e.employeeId = ea.employeeId AND d.departmentId = ea.departmentId
	  ) sq
WHERE sq.fromDate > '2001-03-14'


-- h. 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;


SELECT d.departmentName, COUNT(*) AS 'No. of employees'
FROM EmployedAt e
FULL JOIN Department d
ON e.departmentId = d.departmentId
GROUP BY d.departmentName


SELECT address AS 'Address', COUNT(*) AS 'No. of departments'
FROM Location
GROUP BY address
HAVING MAX(departmentId) < 3


SELECT sq.titleName, AVG(sq.value) AS 'Average Salary'
FROM (	SELECT s.[value], t.titleName
		FROM Employee e
		INNER JOIN Title t
		ON e.employeeId = t.employeeId
		INNER JOIN Salary s
		ON s.employeeId = e.employeeId
	) sq
GROUP BY sq.titleName
HAVING sq.titleName NOT IN (SELECT t.titleName
							FROM Title t
							WHERE toDate IS NULL)


SELECT e.employeeId, COUNT(w.projectId) AS 'No. of projects'
FROM Employee e
LEFT JOIN WorksOn w
ON e.employeeId = w.employeeId
GROUP BY e.employeeId
HAVING MIN(w.projectId) > 1


-- i. 4 queries using ANY and ALL to introduce a subquery in the WHERE clause; 2 of them should be rewritten with aggregation operators, while the other 2 should also be expressed with [NOT] IN.

