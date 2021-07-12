IF OBJECT_ID('RouteStation', 'U') IS NOT NULL
	DROP TABLE RouteStation

IF OBJECT_ID('Station', 'U') IS NOT NULL
	DROP TABLE Station

IF OBJECT_ID('Route', 'U') IS NOT NULL
	DROP TABLE Route

IF OBJECT_ID('Train', 'U') IS NOT NULL
DROP TABLE Train

IF OBJECT_ID('TrainType', 'U') IS NOT NULL
	DROP TABLE TrainType
GO


CREATE TABLE TrainType (
	ttid TINYINT PRIMARY KEY IDENTITY(1,1),
	description VARCHAR(255)
)

CREATE TABLE Train (
	tid SMALLINT PRIMARY KEY IDENTITY(1,1),
	[name] VARCHAR(255) UNIQUE,
	ttid TINYINT FOREIGN KEY REFERENCES TrainType(ttid)
)

CREATE TABLE [Route] (
	rid SMALLINT PRIMARY KEY IDENTITY(1,1),
	tid SMALLINT REFERENCES Train(tid),
	[name] VARCHAR(255) UNIQUE
)

CREATE TABLE Station (
	[sid] SMALLINT PRIMARY KEY IDENTITY(1,1),
	[name] VARCHAR(255) UNIQUE
)

CREATE TABLE RouteStation (
	rid SMALLINT REFERENCES Route(rid),
	[sid] SMALLINT REFERENCES Station([sid]),
	arrivalTime TIME,
	departureTime TIME,
	PRIMARY KEY (rid, [sid])
)
GO


CREATE OR ALTER PROC uspStationOnRoute(@Route VARCHAR(255), @Station VARCHAR(100), @Arrival TIME, @Departure TIME)
AS
	DECLARE @rid INT = (SELECT rid FROM Route WHERE [name] = @Route)
	DECLARE @sid INT = (SELECT [sid] FROM Station WHERE [name] = @Station)

	IF @rid IS NULL OR @sid IS NULL
	BEGIN
		RAISERROR('No such station / route', 16, 1)
		RETURN -1
	END

	IF EXISTS ( SELECT *
				FROM RouteStation
				WHERE rid = @rid AND [sid] = @sid)
			UPDATE RouteStation
			SET arrivalTime = @Arrival,
				departureTime = @Departure
			WHERE rid = @rid AND [sid] = @sid
	ELSE 
		INSERT RouteStation (rid,[sid],arrivalTime, departureTime)
		VALUES (@rid, @sid, @Arrival, @Departure)
GO

INSERT TrainType
VALUES ('regio'), ('interregio')

INSERT Train
VALUES ('t1',1), ('t2',2),('t3',2)

INSERT Station
VALUES ('s1'), ('s2'),('s3')

INSERT [Route]
VALUES (1,'r1'), (2,'r2'),(3,'r3')

SELECT * FROM TrainType
SELECT * FROM Train
SELECT * FROM Station
SELECT * FROM [Route]
SELECT * FROM RouteStation

EXEC uspStationOnRoute 'r1', 's1', '6:10', '6:20'
EXEC uspStationOnRoute 'r1', 's2', '6:30', '6:40'
EXEC uspStationOnRoute 'r1', 's3', '6:45', '6:50'
EXEC uspStationOnRoute 'r2', 's3', '6:55', '7:10'

GO

CREATE OR ALTER VIEW vRoutesWithAllStations
AS
	SELECT r.name
	FROM [Route] r
	WHERE NOT EXISTS
		(SELECT s.[sid]
		 FROM Station s
		 EXCEPT
		 SELECT rs.[sid]
		 FROM RouteStation rs
		 WHERE rs.rid =r.rid
		)
GO

SELECT * FROM vRoutesWithAllStations

GO

CREATE OR ALTER FUNCTION ufFilterStationsByNumRoutes(@R INT)
RETURNS TABLE
RETURN SELECT s.[name]
FROM Station s
WHERE s.sid IN (
	SELECT rs.[sid]
	FROM RouteStation rs
	GROUP BY rs.[sid]
	HAVING COUNT(*) >= @R)

GO
SELECT * FROM ufFilterStationsByNumRoutes(3)
