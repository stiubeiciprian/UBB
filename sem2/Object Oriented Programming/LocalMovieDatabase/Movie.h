#pragma once
#include <string>

class Movie
{
private:

	// Fields of Movie
	std::string title;
	std::string genre;
	int year;
	int likes;
	std::string trailer;

public:

	// Default constructor for Movie
	Movie();

	// Constructor for Movie with parameters
	Movie(const std::string title, const std::string genre, const int year, const int likes, const std::string trailer);

	// Getters
	std::string getTitle() const;
	std::string getGenre() const;
	int getYear() const;
	int getLikes() const;
	std::string getTrailer() const;

	// Setters
	void setTitle(std::string newTitle);
	void setGenre(std::string newGenre);
	void setYear(int newYear);
	void setLikes(int newLikes);
	void setTrailer(std::string newTrailer);

	// Assignment operator
	Movie& operator=(const Movie& movie);

	// Play video at url
	void play();
};

//  Overload of operator ==
bool operator==(const Movie movie, const Movie other);

std::ostream & operator<<(std::ostream & os, const Movie & m);
std::istream & operator>>(std::istream & is, Movie & m);