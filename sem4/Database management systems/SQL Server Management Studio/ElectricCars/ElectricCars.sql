IF OBJECT_ID('CanBeCharged', 'U') IS NOT NULL
DROP TABLE CanBeCharged

IF OBJECT_ID('ChargingStation', 'U') IS NOT NULL
DROP TABLE ChargingStation

IF OBJECT_ID('Car', 'U') IS NOT NULL
	DROP TABLE Car


IF OBJECT_ID('Citizen', 'U') IS NOT NULL
	DROP TABLE Citizen

IF OBJECT_ID('City', 'U') IS NOT NULL
	DROP TABLE City



CREATE TABLE City (
	cityId INT PRIMARY KEY IDENTITY(1,1),
	[name] VARCHAR(255) NOT NULL,
	mayor VARCHAR(255)
)

CREATE TABLE Citizen (
	citizenId INT PRIMARY KEY IDENTITY(1,1),
	personalId INT UNIQUE NOT NULL,
	[name] VARCHAR(255) NOT NULL,
	age INT NOT NULL,
	cityId INT FOREIGN KEY REFERENCES City(cityId)
)

CREATE TABLE Car (
	carId INT PRIMARY KEY IDENTITY(1,1),
	currentFuelLevel INT NOT NULL,
	seatsNumber INT NOT NULL,
	citizenId INT FOREIGN KEY REFERENCES Citizen(citizenId) ON DELETE SET NULL
)

CREATE TABLE ChargingStation (
	stationId INT PRIMARY KEY IDENTITY(1,1),
	[location] VARCHAR(255) NOT NULL
)

CREATE TABLE CanBeCharged (
	carId INT FOREIGN KEY REFERENCES Car(carId),
	stationId INT FOREIGN KEY REFERENCES ChargingStation(stationId),
	PRIMARY KEY (carId, stationId)
)

GO

CREATE OR ALTER PROC deleteAllCitizens(@CityId INT)
AS
	IF @CityId IS NULL
	BEGIN
		RAISERROR('No city found with given ID.', 16, 1)
		RETURN -1
	END

	DELETE FROM Citizen WHERE cityId = @CityId
GO


INSERT City
VALUES ('Cluj Napoca', 'Boc'), ('Arad', 'Popescu'), ('Timisoara', 'Robu')

INSERT Citizen VALUES (1,'John Doe', 31, 1), (2,'Jane Doe', 23, 1), (3,'Winston Smith', 23, 1)
INSERT Citizen VALUES (4,'John Doe', 21, 2), (5,'Jane Doe', 23, 2), (6,'Winston Smith', 21, 2)
INSERT Citizen VALUES (7,'John Doe', 71, 3), (8,'Jane Doe', 53, 3), (9,'Winston Smith', 26, 3)

INSERT Car VALUES (50,4,1), (50,4,1), (50,4,2), (50,4,3), (50,4,4)
INSERT ChargingStation VALUES ('Str. X'),('Str. Y'),('Str. Z'),('Str. Y')
INSERT INTO CanBeCharged VALUES (1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,4),(3,2)

GO

GO

CREATE OR ALTER VIEW vCarsWithMostCompatibleStations
AS
	SELECT carId
	FROM Car c
	WHERE (SELECT COUNT(cbc.carId)
			FROM CanBeCharged cbc
			GROUP BY cbc.carId
			HAVING cbc.carId = c.carId) = (SELECT MAX(res.num) AS stationNum FROM (SELECT COUNT(*) AS num FROM CanBeCharged GROUP BY carId) res)
GO




CREATE OR ALTER FUNCTION ufListCities(@n INT)
RETURNS TABLE
RETURN
	SELECT c.[name]
	FROM City c
	WHERE c.cityId IN (
		SELECT ci.cityId
		FROM Citizen ci INNER JOIN Car cr ON ci.citizenId = cr.citizenId
		GROUP BY ci.citizenId, ci.cityId
		HAVING COUNT(*) >= @n
	)
GO

SELECT * FROM ufListCities(2)
