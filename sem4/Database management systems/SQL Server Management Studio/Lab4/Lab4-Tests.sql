USE EmployeeManagementDatabase
GO

CREATE OR ALTER PROCEDURE employeeTest
@testId int,
@testRunId int,
@rowsNumber int,
@position int,
@viewName varchar(50),
@viewId int,
@tableId int
AS
	--Delete test
	EXEC deleteEmployees @rowsNumber, @position

	--Insert test
	DECLARE @startTime DATETIME = SYSDATETIME()

	EXEC insertEmployees @rowsNumber, @position

	INSERT INTO TestRunTables(TestRunID, TableID, StartAt, EndAt)
	VALUES (@testRunId, @tableId, @startTime, SYSDATETIME())

	--View test
	SET @startTime = SYSDATETIME()

	DECLARE @query nvarchar(50) = N'SELECT * FROM ' + @viewName
	EXEC sp_executesql @query
	
	INSERT INTO TestRunViews(TestRunID, ViewID, StartAt, EndAt)
	VALUES (@testRunId, @viewId, @startTime, SYSDATETIME())
	
GO

CREATE OR ALTER PROCEDURE salariesTest
@testId int,
@testRunId int,
@rowsNumber int,
@position int,
@viewName varchar(50),
@viewId int,
@tableId int
AS
	--Delete test
	EXEC deleteSalaries @rowsNumber, @position
	
	--Insert test
	DECLARE @startTime DATETIME = SYSDATETIME()

	EXEC insertSalaries @rowsNumber, @position

	INSERT INTO TestRunTables(TestRunID, TableID, StartAt, EndAt)
	VALUES (@testRunId, @tableId, @startTime, SYSDATETIME())
	
	--View test
	SET @startTime = SYSDATETIME()

	DECLARE @query nvarchar(50) = N'SELECT * FROM ' + @viewName
	EXEC sp_executesql @query
	
	INSERT INTO TestRunViews(TestRunID, ViewID, StartAt, EndAt)
	VALUES (@testRunId, @viewId, @startTime, SYSDATETIME())
	
GO

CREATE OR ALTER PROCEDURE employedAtTest
@testId int,
@testRunId int,
@rowsNumber int,
@position int,
@viewName varchar(50),
@viewId int,
@tableId int
AS
	-- Delete test
	EXEC deleteEmployedAt @rowsNumber, @position

	-- Insert Test
	DECLARE @startTime DATETIME = SYSDATETIME()

	EXEC insertEmployedAt @rowsNumber, @position

	INSERT INTO TestRunTables(TestRunID, TableID, StartAt, EndAt)
	VALUES (@testRunId, @tableId, @startTime, SYSDATETIME())

	--View test
	SET @startTime = SYSDATETIME()

	DECLARE @query nvarchar(50) = N'SELECT * FROM ' + @viewName
	EXEC sp_executesql @query
	
	INSERT INTO TestRunViews(TestRunID, ViewID, StartAt, EndAt)
	VALUES (@testRunId, @viewId, @startTime, SYSDATETIME())
GO