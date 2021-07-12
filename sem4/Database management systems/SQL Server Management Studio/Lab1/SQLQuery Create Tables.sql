
CREATE TABLE Employee (
	employeeId INT IDENTITY(1,1) PRIMARY KEY ,
	firstName VARCHAR(255) NOT NULL,
	lastName VARCHAR(255) NOT NULL,
	birthDate DATE NOT NULL
)

CREATE TABLE Salary (
	salaryId INT IDENTITY(1,1) PRIMARY KEY,
	employeeId INT FOREIGN KEY REFERENCES Employee(employeeId),
	[value] INT NOT NULL,
	fromDate DATE NOT NULL,
	toDate DATE
)

CREATE TABLE Department (
	departmentId INT IDENTITY(1,1) PRIMARY KEY,
	departmentName VARCHAR(255) NOT NULL,
)

CREATE TABLE EmployedAt (
	employeeId INT FOREIGN KEY REFERENCES Employee(employeeId),
	departmentId INT FOREIGN KEY REFERENCES Department(departmentId),
	fromDate DATE NOT NULL,
	toDate DATE,
	PRIMARY KEY (employeeId,departmentId,fromDate)
	
)

CREATE TABLE [Location](
	locationId INT IDENTITY(1,1) PRIMARY KEY,
	departmentId INT FOREIGN KEY REFERENCES Department(departmentId),
	address VARCHAR(255) NOT NULL
)

CREATE TABLE Title (
	titleId INT IDENTITY(1,1) PRIMARY KEY,
	employeeId INT FOREIGN KEY REFERENCES Employee(employeeId),
	titleName VARCHAR(255) NOT NULL,
	fromDate DATE NOT NULL, 
	toDate DATE
)

CREATE TABLE MeetingRoom (
	roomId INT IDENTITY(1,1) PRIMARY KEY,
    roomName VARCHAR(50) NOT NULL,
	seatsNumber INT NOT NULL
)

CREATE TABLE BookMeetingRoom (
	employeeId INT FOREIGN KEY REFERENCES Employee(employeeId),
	roomId INT FOREIGN KEY REFERENCES MeetingRoom(roomId),
	bookingDate DATE NOT NULL,
	PRIMARY KEY (employeeId,roomId,bookingDate)
)

CREATE TABLE Project (
	projectId INT IDENTITY(1,1) PRIMARY KEY,
	title VARCHAR(255),
)

CREATE TABLE WorksOn (
	employeeId INT FOREIGN KEY REFERENCES Employee(employeeId),
	projectId INT FOREIGN KEY REFERENCES Project(projectId),
	fromDate DATE NOT NULL,
	toDate DATE,
	PRIMARY KEY (employeeId,projectId)
)