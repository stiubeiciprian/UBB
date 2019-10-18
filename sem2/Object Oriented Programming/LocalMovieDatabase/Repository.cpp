#include "Repository.h"



using namespace std;

// Default constructor for Repository
Repository::Repository(int capacity)
{
}

// Copy constructor for Repository
Repository::Repository(const Repository& v)
{	
	this->dvector = v.dvector;
}

// Initialize repo with existing vector
Repository::Repository(std::vector<Movie> v)
{
	this->dvector = v;
}

// Assignment operator for Repository
Repository& Repository::operator=(const Repository& v)
{
	if (this == &v)
		return *this;

	this->dvector = v.dvector;

	return *this;
}

/*
	Add an element to the Repository.
	Input: e - Movie
	Output: true, if the element was added
			false, if the element already exists
*/
bool Repository::add(const Movie& e)
{	
	auto it = std::find(this->dvector.begin(), this->dvector.end(), e);

	if (it != this->dvector.end())
		throw std::runtime_error("Element already exists in repository!\n");

	this->dvector.push_back(e);

	return true;
}


/*
	Remove an element from the Repository.
	Input: e - Movie
	Precond: e has the id of the element to be removed
	Output: true, if the element was removed
			false, if the element did not exist
*/
bool Repository::remove(const Movie e)
{
	auto it = std::find(this->dvector.begin(), this->dvector.end(), e);

	if (it != this->dvector.end()) {
		this->dvector.erase(it);
		return true;
	}
	
	throw std::runtime_error("Element was not found in repository!");
}

/*
	Update an element from the Repository.
	Input: e - Movie
	Precond: e has the id of the element to be updated
			 e contains the updated fields
	Output: true, if the element was updated
			false, if the element did not exist
*/
bool Repository::update(const Movie e)
{
	for(unsigned i=0; i<this->dvector.size(); i++)
		if (this->dvector[i] == e) {
			this->dvector[i] = e;
			return true;
		}

	throw std::runtime_error("Element was not found in repository!");
}

/*
	Search for an element in the Repository.
	Input: e - Movie
	Precond: e has the id of searched element
	Output: position of Movie, if the Movie was found in the Repository
			-1, otherwise
*/
int Repository::search(const Movie e)
{
	for (unsigned i = 0; i < this->dvector.size(); i++)
		if (this->dvector[i] == e)
			return i;

	return -1;
}

// Get size of the Repository
int Repository::getSize() const
{
	return this->dvector.size();
}


// Get element at given position
Movie Repository::getElem(int position) const {
	return this->dvector[position];
}



std::string Repository::getElemStr(int position) {
	std::string str = "";
	Movie e=this->dvector[position];
	str += "Title: " + e.getTitle() + "\tGenre: " + e.getGenre() + "\tYear: " + std::to_string(e.getYear()) + "\t Likes: " + std::to_string(e.getLikes()) + "\tURL: " + e.getTrailer();

	return str;
}

// Get all elements of the Repository represeted as string
std::string Repository::getAllString()
{
	std::string repoStr="";

	for (unsigned i = 0; i < this->dvector.size(); i++)
		repoStr += this->getElemStr(i) + "\n";

	return repoStr;
}

// Get all elements of the Repository
std::vector<Movie> Repository::getAll()
{
	std::vector<Movie> movies;

	movies = this->dvector;

	return movies;
}



Repository& operator+(Repository& repo, Movie elem) 
{
	repo.add(elem);
	return repo;
}

Repository& operator+(Movie elem, Repository& repo) 
{
	repo.add(elem);
	return repo;
}

