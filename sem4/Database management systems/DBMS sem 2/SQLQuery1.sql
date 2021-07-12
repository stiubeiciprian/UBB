/*

Create a database for a film festival ticketing system. The entities of interest to the problem domain are: Movies, Producers, Movie Categories, and Cinemas
Your system must track ticket sales for different movies, which run in different cinemas, at different times.
Each movie has a title, a producer and a movie category. Such a category has a name (e.g., romance, thriller, comedy) and a description. 
A producer has a first name, last name, nationality, number of awards, and can be associated with several movies. 
Each cinema has a name, location and number of seats. 

There is also a schedule for each movie, with the corresponding cinema, the time the movie starts at and the number of sold tickets 
(e.g., <movie m1, cinema c1, 10:00 AM, 100 tickets>, <movie m1, cinema c1, 12:00 PM, 70 tickets>, <movie m1, cinema c2, 12:00 PM, 80 tickets>, <movie m2, cinema c1, 7:00 PM, 100 tickets>, etc).



a. Write an SQL script that creates the corresponding relational data model in 3NF.
 
b. Create a Master/Detail Form that allows one to display the movies for a given producer, to carry out <insert, update, delete> operations on the movies of a given producer. 
	
The form should have a DataGridView named dgvProducers to display the producers, a DataGridView named dgvMovies to display all the movies of the selected producer, 

and a button for saving added / deleted / modified movies. You must use the following classes: DataSet, SqlDataAdapter, BindingSource. 

* Tip – when deleting movies: test the application with movies that are not referenced from other tables; or use ON DELETE CASCADE.

c. Create a scenario that reproduces the dirty read phenomenon on this database. Explain why the 
dirty read occurs, and describe a solution to prevent this concurrency problem. Don’t use stored procedures.		

*/

CREATE TABLE Producers (
	producerId INT PRIMARY KEY IDENTITY(1,1),
	firstName VARCHAR(50),
	lastName VARCHAR(50),
	nationality VARCHAR(50),
	numberOfAwards SMALLINT
)

CREATE TABLE Categories (
	categoryId INT PRIMARY KEY IDENTITY(1,1),
	[name] VARCHAR(50),
	[description] VARCHAR(255)
)

CREATE TABLE Movies (
	movieId INT PRIMARY KEY IDENTITY(1,1),
	title VARCHAR(50),
	producerId INT REFERENCES Producers(producerId), --A producer can be associated with multiple movies
	categoryId INT REFERENCES Categories(categoryId), --A movie has a single main category instead of multiple ones. But one category can belong to multiple movies.
)

CREATE TABLE Cinemas (
	cinemaId INT PRIMARY KEY IDENTITY(1,1),
	[name] VARCHAR(50),
	[location] VARCHAR(255),
	numberOfSeats INT
)

CREATE TABLE Schedule (
	cinemaId INT REFERENCES Cinemas(cinemaId), 
	movieId INT REFERENCES Movies(movieId) ON DELETE CASCADE,
	numberOfSoldTickets INT,
	movieStartTime DATETIME,
	PRIMARY KEY(cinemaId, movieId, movieStartTime) --One movie can be seen at multiple cinemas or at the same cinema at different times
	)

INSERT INTO Producers(firstName, lastName, nationality, numberOfAwards) VALUES ('John', 'Doe', 'British', 4), ('Marry', 'Doe', 'British', 6),('Will', 'Lee', 'British', 10);
INSERT INTO Categories([name], [description]) VALUES ('Indie', 'Description'), ('Generic', 'Description 2');
INSERT INTO Movies(title, producerId, categoryId) VALUES ('Shark Attack 3', 1, 1), ('Shark Attack 2', 1, 1), ('Umbrella Academy', 2, 2), ('Bruce Lee', 3, 2);

SELECT * FROM Movies;
SELECT * FROM Categories;
SELECT * FROM Producers;