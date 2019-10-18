#pragma once
#include "Movie.h"
#include <vector>

class Repository
{
	//friend class DynamicVector<Movie>;

private:

	// Fields of Repository
	std::vector<Movie> dvector;

public:
	// Default constructor for Repository
	Repository(int capacity = 25);
	
	// Constructor with given vector 
	Repository(std::vector<Movie> v);

	// Copy constructor for Repository
	Repository(const Repository& v);

	// Assignment operator for Repository
	Repository& operator=(const Repository& v);



	// Add an element to the Repository
	bool add(const Movie& e);

	// Remove an element from the Repository
	bool remove(const Movie e);



	// Update an element from the Repository
	bool update(const Movie e);



	// Search for an element in the Repository
	int search(const Movie e);



	// Get a copy of an element at given position
	Movie getElem(int position) const;

	std::string getElemStr(int position);

	// Get size of the Repository
	int getSize() const;

	// Get all elements of the Repository
	std::string getAllString();

	// Get all elements
	std::vector<Movie> getAll();

};

Repository& operator+(Repository& repo, Movie elem);

Repository& operator+(Movie elem, Repository& repo);
