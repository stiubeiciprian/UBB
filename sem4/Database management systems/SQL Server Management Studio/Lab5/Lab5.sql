USE Lab5

CREATE TABLE Ta(
	aid INT PRIMARY KEY,
	a2 INT UNIQUE,
	a3 INT
)

CREATE TABLE Tb (
	bid INT PRIMARY KEY,
	b2 INT
)

CREATE TABLE Tc (
	cid INT PRIMARY KEY,
	aid INT REFERENCES Ta(aid),
	bid INT REFERENCES Tb(bid)
)

INSERT INTO Tc(cid, aid, bid)
VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6)

SELECT bid, b2
FROM Tb
WHERE b2 = 2

EXEC sp_helpindex Ta
EXEC sp_helpindex Tb
EXEC sp_helpindex Tc

-- a)
SELECT aid FROM Ta WHERE a3 = 1 --clustered index scan
SELECT aid FROM Ta WHERE aid > 2 --clustered index seek
SELECT a2 FROM Ta -- nonclustered index scan
SELECT aid FROM Ta WHERE a2 > 1 -- nonclustered index seek
SELECT a3 FROM Ta WHERE a2 = 3 -- nonclustered index seek (for a2) + key lookup (for a3)


-- b)
SELECT b2 FROM Tb WHERE b2 = 1 
--BEFORE: clustered index scan Tb.PK - 0.0032886
CREATE NONCLUSTERED index index_nc_b2 on Tb(b2)
--AFTER: nonclustered index seek Tb.index.nc_b2 - 0.0032831
DROP INDEX index_nc_b2 ON Tb


GO
-- c)
CREATE OR ALTER VIEW viewJoin2Tables
AS
	SELECT tc.cid, tc.aid
	FROM Tc INNER JOIN Ta ON Tc.aid = Ta.aid
	WHERE Tc.aid > 1
GO

SELECT * FROM viewJoin2Tables 
--BEFORE:
--clustered index scan Tc.PK - 0.0032886
--clustered index seek Ta.PK - 0.0039155
CREATE NONCLUSTERED INDEX index_nc_aid ON Tc(aid)
--AFTER:
--nonclustered index seek Tc.index_nc_aid - 0.0032875
--clustered index seek Ta.PK - 0.0039155
DROP INDEX index_nc_aid ON Tc
