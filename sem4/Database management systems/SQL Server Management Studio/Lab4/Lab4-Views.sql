USE EmployeeManagementDatabase
GO

--- Views

CREATE OR ALTER VIEW viewEmployees
AS SELECT firstName, lastName, CNP
	FROM Employee
GO

CREATE OR ALTER VIEW viewTitleSalaries
AS SELECT t.titleName, s.[value]
	FROM Title t
	LEFT JOIN Salary s ON t.employeeId=s.employeeId
GO


CREATE OR ALTER VIEW viewTitlesAvgSalary
AS SELECT t.titleName, AVG(s.value) AS "Average Salary"
	FROM Title t 
	LEFT JOIN Salary s ON t.employeeId=s.employeeId
	GROUP BY t.titleName
GO