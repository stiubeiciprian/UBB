#include "Movie.h"
#include <Windows.h>
#include <shellapi.h>
#include <vector>
#include <fstream>
#include <sstream>


using namespace std;

// Default constructor for movie
Movie::Movie(): title(""), genre(""), year(0), likes(0), trailer("") {}

// Constructor for Movie with parameters
Movie::Movie(const std::string title, const std::string genre, const int year, const int likes, const std::string trailer)
{
	this->title = title;
	this->genre = genre;
	this->year = year;
	this->likes = likes;
	this->trailer = trailer;
}

// Assignment operator =
Movie& Movie::operator=(const Movie& movie)
{
	if (this == &movie)
		return *this;

	this->title = movie.getTitle();
	this->genre = movie.getGenre();
	this->year = movie.getYear();
	this->likes = movie.getLikes();
	this->trailer = movie.getTrailer();

	return *this;
}

void Movie::play()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
}

// Getters
std::string Movie::getTitle() const { return this->title; }
std::string Movie::getGenre() const { return this->genre; }
int Movie::getYear() const { return this->year; }
int Movie::getLikes() const { return this->likes; }
std::string Movie::getTrailer() const { return this->trailer; }

// Setters
void Movie::setTitle(std::string newTitle) { this->title = newTitle; }
void Movie::setGenre(std::string newGenre) { this->genre = newGenre; }
void Movie::setYear(int newYear) { this->year = newYear; }
void Movie::setLikes(int newLikes) { this->likes = newLikes; }
void Movie::setTrailer(std::string newTrailer) { this->trailer = newTrailer; }

//  Overload of operator ==
bool operator==(const Movie movie,const Movie other) 
{
	if (movie.getTitle() == other.getTitle())
		return true;
	return false;
}



/*
	Tokenizes a string.
	Input:	str - the string to be tokenized.
			delimiter - char - the delimiter used for tokenization
	Output: a vector of strings, containing the tokens
*/
vector<string> tokenize(string str, char delimiter)
{
	vector <string> result;
	stringstream ss(str);
	string token;
	while (getline(ss, token, delimiter))
		result.push_back(token);

	return result;
}

std::istream & operator>>(std::istream & is, Movie & m)
{
	string line;
	getline(is, line);

	vector<string> tokens = tokenize(line, ',');
	if (tokens.size() != 5)
		return is;

	m.setTitle(tokens[0]);
	m.setGenre(tokens[1]);
	m.setYear(std::stoi(tokens[2]));
	m.setLikes(std::stoi(tokens[3]));
	m.setTrailer(tokens[4]);

	return is;
}

std::ostream & operator<<(std::ostream & os, const Movie & m)
{
	os << m.getTitle() << ","
		<< m.getGenre() << ","
		<< m.getYear() << ","
		<< m.getLikes() << ","
		<< m.getTrailer() << "\n";
	return os;
}