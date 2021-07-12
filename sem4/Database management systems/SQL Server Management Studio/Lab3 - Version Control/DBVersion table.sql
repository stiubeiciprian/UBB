USE EmployeeManagementDatabase

CREATE TABLE DatabaseVersion(
	versionId INT NOT NULL PRIMARY KEY,
	applyProcedure VARCHAR(50),
	revertProcedure VARCHAR(50),
	description VARCHAR(255),
)

CREATE TABLE CurrentVersion(
	currentVersion INT NOT NULL PRIMARY KEY,
)

INSERT INTO DatabaseVersion VALUES (1,'','','Base version.')
INSERT INTO DatabaseVersion VALUES (2,'AddColumn','RemoveColumn','Add Employee CNP column.')
INSERT INTO DatabaseVersion VALUES (3,'ModifyColumn','ModifyColumnRevert','Modify CNP column type from varchar(13) to char(13).')
INSERT INTO DatabaseVersion VALUES (4,'AddCandidateKey','RemoveCandidateKey','Add UNIQUE constraint on CNP column.')
INSERT INTO DatabaseVersion VALUES (5,'AddTable','RemoveTable','Create Client table.')
INSERT INTO DatabaseVersion VALUES (6,'AddPrimaryKey','RemovePrimaryKey','Add PRIMARY KEY for Client table.')
INSERT INTO DatabaseVersion VALUES (7,'AddForeignKey','RemoveForeignKey','Add FOREIGN KEY for Client table.')
INSERT INTO DatabaseVersion VALUES (8,'AddDefaultConstraint','RemoveDefaultConstraint','Add DEFAULT constraint for clientName.')

INSERT INTO CurrentVersion VALUES (1)

SELECT *FROM DatabaseVersion

SELECT * FROM CurrentVersion