USE EmployeeManagementDatabase
GO
--Insert

CREATE OR ALTER PROCEDURE insertEmployees
@rowsNumber INT,
@position INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @position + @rowsNumber - 1

	SET IDENTITY_INSERT Employee ON

	WHILE @i >= @position
	BEGIN
		INSERT INTO Employee(employeeId, firstName, lastName, birthDate, CNP)
		VALUES (@i, 'Winston', 'Smith', '1984-03-03', '1840303040103')
		SET @i = @i - 1
	END

	SET IDENTITY_INSERT Employee OFF
END
GO

CREATE OR ALTER PROCEDURE insertSalaries
@rowsNumber INT,
@position INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @position + @rowsNumber - 1

	SET IDENTITY_INSERT Salary ON

	WHILE @i >= @position
	BEGIN
		INSERT INTO Salary(salaryId, employeeId, fromDate, toDate, value)
		VALUES (@i, 1, '2019-11-03', null, 1000)
		SET @i = @i - 1
	END

	SET IDENTITY_INSERT Salary OFF
END
GO

CREATE OR ALTER PROCEDURE insertEmployedAt
@rowsNumber INT,
@position INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @position + @rowsNumber - 1

	WHILE @i >= @position
	BEGIN
		INSERT INTO EmployedAt(employeeId, departmentId, fromDate)
		VALUES (@i, 1, '2019-11-03')
		SET @i = @i - 1
	END
END
GO

--Delete

CREATE OR ALTER PROCEDURE deleteEmployees
@rowsNumber INT,
@offset INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @offset

	WHILE @i < @rowsNumber + @offset
	BEGIN
		DELETE FROM Employee
		WHERE employeeId = @i
		SET @i = @i + 1
	END
END
GO


CREATE OR ALTER PROCEDURE deleteSalaries
@rowsNumber INT,
@offset INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @offset

	WHILE @i < @rowsNumber + @offset
 	BEGIN
		DELETE FROM Salary
		WHERE salaryId = @i
		SET @i = @i + 1
	END
END
GO


CREATE OR ALTER PROCEDURE deleteEmployedAt
@rowsNumber INT,
@offset INT
AS
BEGIN
	DECLARE @i INT
	SET @i = @offset

	WHILE @i < @rowsNumber + @offset
	BEGIN
		DELETE FROM EmployedAt
		WHERE employeeId = @i AND departmentId = 1 AND fromDate = '2019-11-03'
		SET @i = @i + 1
	END
END
GO

