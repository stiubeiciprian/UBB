USE EmployeeManagementDatabase
GO

-- Add views to Views table
CREATE OR ALTER PROCEDURE addView(@viewName varchar(50))
AS
	INSERT INTO Views VALUES (@viewName)
GO

-- Add tables to Tables table
CREATE OR ALTER PROCEDURE addTable(@tableName varchar(50))
AS
	INSERT INTO Tables VALUES (@tableName)
GO

-- Add tests to Tests table

CREATE OR ALTER PROCEDURE addTest(@testName varchar(50), @viewName varchar(50), @tableName varchar(50), @rowsNumber int, @position int)
AS
	IF OBJECT_ID(@testName, 'P') IS NULL BEGIN
		RAISERROR('Test does not exist!', 16, 1)
		RETURN -1
	END

	-- Add view
	DECLARE @viewId varchar(50) = (SELECT ViewID FROM Views WHERE Name = @viewName)

	IF @viewId IS NULL BEGIN
		IF OBJECT_ID(@viewName, 'V') IS NOT NULL BEGIN
			EXEC addView @viewName
			SET @viewId = (SELECT ViewID FROM Views WHERE Name = @viewName)
		END
		ELSE BEGIN
			RAISERROR('View does not exist!', 16, 1)
			RETURN -1
		END
	END

	--Add table
	DECLARE @tableId varchar(50) = (SELECT TableID FROM Tables WHERE Name = @tableName)

	IF @tableId IS NULL BEGIN
		IF OBJECT_ID(@tableName, 'U') IS NOT NULL BEGIN
			EXEC addTable @tableName
			SET @tableId = (SELECT TableID FROM Tables WHERE Name = @tableName)
		END
		ELSE BEGIN
			RAISERROR('Table does not exist!', 16, 1)
			RETURN -1
		END
	END
	
	INSERT INTO Tests(Name) VALUES (@testName)
	DECLARE @testId int = @@IDENTITY
	INSERT INTO TestViews(TestID, ViewID) VALUES(@testId, @viewId)
	INSERT INTO TestTables(TestID, TableID, NoOfRows, Position) VALUES(@testId, @tableId, @rowsNumber, @position)
GO

-- RUN TEST PROCEDURE

CREATE OR ALTER PROCEDURE executeTest
@testId varchar(50)
AS
	DECLARE @testName varchar(50) = (SELECT Name FROM Tests WHERE TestID = @testId)
	DECLARE @position int = (SELECT Position FROM TestTables WHERE TestID = @testId)
	DECLARE @rowsNumber int = (SELECT NoOfRows FROM TestTables WHERE TestID = @testId)
	DECLARE @tableId int = (SELECT tb.TableID FROM TestTables tb LEFT JOIN Tables t ON tb.TableID = t.TableID WHERE tb.TestID = @testId)
	DECLARE @viewId int = (SELECT tv.ViewID FROM TestViews tv LEFT JOIN Views v ON tv.ViewID = v.ViewID WHERE tv.TestID = @testId)
	DECLARE @viewName varchar(50) = (SELECT v.Name FROM Views v WHERE v.ViewID = @viewId)

	INSERT INTO TestRuns(Description, StartAt)
	VALUES (@testName, SYSDATETIME())

	DECLARE @testRunId int = @@IDENTITY

	EXEC @testName @testId, @testRunId, @rowsNumber, @position, @viewName, @viewId, @tableId

	UPDATE TestRuns
	SET EndAt = SYSDATETIME()
	WHERE TestRunID = @testRunId
GO

--------------------------------------------------------

SELECT * FROM Tests
SELECT * FROM Views
SELECT * FROM Tables
SELECT * FROM TestViews
SELECT * FROM TestTables

SELECT * FROM TestRunTables
SELECT * FROM TestRunViews
SELECT * FROM TestRuns

SELECT * FROM Employee ORDER BY employeeId



EXEC addTest 'employeeTest', 'viewEmployees', 'Employee', 10, 50
EXEC addTest 'salariesTest', 'viewTitleSalaries', 'Salary', 20, 100
EXEC addTest 'employedAtTest', 'viewTitlesAvgSalary', 'Salary', 20, 1

EXEC executeTest 7


DELETE FROM TestRunTables
DELETE FROM TestRunViews
DELETE FROM TestRuns
DELETE FROM Tests
DELETE FROM TestViews
DELETE FROM TestTables
DELETE FROM Views
DELETE FROM Tables
