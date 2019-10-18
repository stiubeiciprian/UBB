#pragma once
#include "Movie.h"

typedef Movie TElem;

class DynamicVector;

class Repository
{
	friend class DynamicVector;

private:

	// Fields of Repository
	DynamicVector dvector;

	// Resize the Repository
	void resize();

public:
	// Default constructor for Repository
	Repository(int capacity = 25);

	// Copy constructor for Repository
	Repository(const Repository& v);

	// Assignment operator for Repository
	Repository& operator=(const Repository& v);

	// Add an element to the Repository
	bool add(const TElem& e);

	// Remove an element from the Repository
	bool remove(const TElem e);

	// Update an element from the Repository
	bool update(const TElem e);

	// Search for an element in the Repository
	int search(const TElem e);

	// Get a copy of an element at given position
	TElem getElem(int position) const;

	std::string getElemStr(int position);

	// Get size of the Repository
	int getSize() const;

	// Get all elements of the Repository
	std::string getAll();

};

Repository& operator+(Repository& repo, TElem elem);

Repository& operator+(TElem elem, Repository& repo);
