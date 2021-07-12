
/*
 * create a stored procedure that inserts data in tables that are in a m:n relationship; 
 * if one insert fails, all the operations performed by the procedure must be rolled back (grade 3);
 */

CREATE OR ALTER PROC assignProject(@projectName VARCHAR(255), @CNP CHAR(13))
AS
	BEGIN TRY
		BEGIN TRAN

		INSERT INTO Project(title) VALUES(@projectName);
		DECLARE @employeeId INT = (SELECT employeeId FROM Employee WHERE CNP = @CNP)
		INSERT INTO WorksOn(projectId, employeeId, fromDate) VALUES(@@IDENTITY , @employeeId, CURRENT_TIMESTAMP);

		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RAISERROR('Assign project transaction failed.', 16, 1)
	END CATCH
GO

SELECT * FROM Project;
SELECT * FROM Employee;
SELECT * FROM WorksOn;


EXEC assignProject "DBMS Project fail", "1234567890123"
EXEC assignProject "DBMS New Project", "1990319020105"
GO




/*
 * create a stored procedure that inserts data in tables that are in a m:n relationship; 
 * if an insert fails, try to recover as much as possible from the entire operation: 
 * for example, if the user wants to add a book and its authors, succeeds creating the authors, but fails with the book, the authors should remain in the database (grade 5);
 */

CREATE OR ALTER PROC addEmployeeAndProject(@projectName VARCHAR(255), @firstName VARCHAR(255), @lastName VARCHAR(255), @birthDate DATE,  @CNP CHAR(13))
AS
	BEGIN TRY
		BEGIN TRAN
		INSERT INTO Employee(firstName, lastName, birthDate, CNP) VALUES(@firstName, @lastName, @birthDate, @CNP);
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RAISERROR('Failed to add employee.', 16, 1)
	END CATCH

		BEGIN TRY
		BEGIN TRAN
		INSERT INTO Project(title) VALUES(@projectName);
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RAISERROR('Failed to add project.', 16, 1)
	END CATCH

	BEGIN TRY
		BEGIN TRAN
		DECLARE @employeeId INT = (SELECT employeeId FROM Employee WHERE CNP = @CNP)
		DECLARE @projectId INT = (SELECT projectId FROM Project WHERE title = @projectName)
		INSERT INTO WorksOn(projectId, employeeId, fromDate) VALUES(@projectId, @employeeId, CURRENT_TIMESTAMP);
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RAISERROR('Failed to assign project to employee.', 16, 1)
	END CATCH
GO

SELECT * FROM Project;
SELECT * FROM Employee;

EXEC addEmployeeAndProject "Project Success 2", "Alexander", "Johnson", "1999-03-19", "190319030118"
EXEC addEmployeeAndProject "Project New", "Jane", "Doe", NULL, "180349030106"
GO


/*
 * create 4 scenarios that reproduce the following concurrency issues under pessimistic isolation levels:
 *
 * dirty reads, 
 * non-repeatable reads, 
 * phantom reads,
 * and a deadlock; 
 *
 * you can use stored procedures and / or stand-alone queries;
 * find solutions to solve / workaround the concurrency issues (grade 9);
 */

  SELECT * FROM Employee

-- Dirty read: occurs when one transaction reads data that is being modified by another transaction which is running concurrently but which has not yet committed itself. 


SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	UPDATE Employee
	SET firstName = 'Dillan'
	WHERE employeeId = 1
	WAITFOR DELAY '00:00:10'
ROLLBACK TRAN

-- run in different session 
-- solution 
--SET TRANSACTION ISOLATION LEVEL READ COMMITTED
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRAN
	SELECT * FROM Employee
COMMIT TRAN
 
-- Non-repeatable reads: an existing row changes during the transaction, therefore different reads of the row will return different values

-- solution 
--SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	SELECT * FROM Employee
	WAITFOR DELAY '00:00:10'
	SELECT * FROM Employee
 COMMIT TRAN

-- run in separate session
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	UPDATE Employee
	SET firstName = 'Will'
	WHERE employeeId = 264
COMMIT TRAN



-- Phantom reads: rows have been inserted after a read operation and become visible in a follow-up read operation within the same transaction.
--solution 
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
--SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	SELECT * FROM Employee
	WAITFOR DELAY '00:00:10'
	SELECT * FROM Employee
COMMIT TRAN

-- run in a different session
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	INSERT INTO Employee(firstName, lastName, birthDate, CNP)
	VALUES ('Phantom', 'Phantom', 1000-10-10, 1001010020105)
COMMIT TRAN

SELECT * FROM WorksOn

DELETE FROM Employee WHERE employeeId = 267




SELECT * FROM WorksOn
SELECT * FROM Employee
-- Deadlock: concurrency problem i which 2 transactions block each other
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
--SET DEADLOCK_PRIORITY LOW
BEGIN TRAN
	UPDATE Employee
	SET lastName = 'Waterson'
	WHERE employeeId = 1

	WAITFOR DELAY '00:00:10'

	UPDATE WorksOn
	SET toDate = '2019-05-21'
	WHERE employeeId = 1
COMMIT TRAN

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRAN
	UPDATE WorksOn
	SET toDate = '2020-05-21'
	WHERE employeeId = 1

	WAITFOR DELAY '00:00:10'

	UPDATE Employee
	SET lastName = 'Johnson'
	WHERE employeeId = 1
COMMIT TRAN


