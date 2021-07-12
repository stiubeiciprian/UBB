--a. Modify column type procedure

CREATE OR ALTER PROCEDURE ModifyColumn
AS
	ALTER TABLE Employee
	ALTER COLUMN CNP char(13)
GO

CREATE OR ALTER PROCEDURE ModifyColumnRevert
AS
	ALTER TABLE Employee
	ALTER COLUMN CNP varchar(13)
GO



--b. Add / Remove column procedures

CREATE OR ALTER PROCEDURE AddColumn
AS
	BEGIN
		ALTER TABLE Employee ADD CNP VARCHAR(13);
	END
GO

CREATE OR ALTER PROCEDURE RemoveColumn
AS
	BEGIN
		ALTER TABLE Employee 
		DROP COLUMN CNP
	END
GO




--c. Add / Remove default constraint procedures

CREATE OR ALTER PROCEDURE AddDefaultConstraint
AS
	ALTER TABLE Client 
	ADD CONSTRAINT DC_Client DEFAULT 'Anonymous' FOR clientName
GO

CREATE OR ALTER PROCEDURE RemoveDefaultConstraint
AS
	ALTER TABLE Client
	DROP CONSTRAINT DC_Client
GO




--d. Add / Remove primary key procedures

CREATE OR ALTER PROCEDURE AddPrimaryKey
AS
	ALTER TABLE Client
	ADD CONSTRAINT PK_clientId PRIMARY KEY (clientId)
GO

CREATE OR ALTER PROCEDURE RemovePrimaryKey
AS
	ALTER TABLE Client
	DROP CONSTRAINT PK_clientId
GO




--e. Add / Remove candidate key procedures

CREATE OR ALTER PROCEDURE AddCandidateKey
AS
	ALTER TABLE Employee
	ADD CONSTRAINT UC_Employee UNIQUE (lastName,firstName)
GO

CREATE OR ALTER PROCEDURE RemoveCandidateKey
AS
	ALTER TABLE Employee
	DROP CONSTRAINT UC_Employee
GO




--f. Add / Remove foreign key procedures

CREATE OR ALTER PROCEDURE AddForeignKey
AS
	ALTER TABLE Client
	ADD CONSTRAINT FK_projectId FOREIGN KEY (projectId) REFERENCES Project(projectId)
GO

CREATE OR ALTER PROCEDURE RemoveForeignKey
AS
	ALTER TABLE Client
	DROP CONSTRAINT FK_projectId
GO




--g. Create / Remove table procedures

CREATE OR ALTER PROCEDURE AddTable
AS
	BEGIN
		CREATE TABLE Client (
			clientId INT IDENTITY(1,1),
			clientName VARCHAR(50),
			projectId INT
			)
	END
GO

CREATE OR ALTER PROCEDURE RemoveTable
AS
	BEGIN
		DROP TABLE Client
	END
GO


EXEC RemoveColumn
GO

EXEC ModifyColumn
GO

EXEC RemoveCandidateKey
GO


EXEC RemoveTable
GO

EXEC RemovePrimaryKey
GO

EXEC RemoveForeignKey
GO

EXEC RemoveDefaultConstraint
GO

EXEC AddDefaultConstraint
GO

SELECT * FROM Client