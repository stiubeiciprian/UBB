#pragma once
#include "Repository.h"
#include "Comparator.h"
#include "ValidatorMovie.h"
#include "Watchlist.h"
#include "WatchlistCSV.h"
#include "WatchlistHTML.h"

class Controller
{
	Repository& repo;
	ValidatorMovie validatorMovie;
	Watchlist& watchlist;
	std::string wlType;

public:
	Controller(Repository& r, Watchlist& wl) : repo{ r }, watchlist { wl } {}

	// Administrator mode methods
	bool add(std::string title, std::string genre, int year, int likes, std::string trailer);
	bool remove(std::string title);
	bool updateGenre(std::string title, std::string new_genre);
	bool updateYear(std::string title, int new_year);
	bool updateLikes(std::string title, int new_likes);
	bool updateTrailer(std::string title, std::string new_trailer);

	// User mode methods
	Repository selectMovies(std::string genre);

	

	bool addToWatchlist(Movie m);
	bool removeFromWatchlist(std::string title);
	void displayWatchlist();
	std::string getWatchlist();
	void incLikes(std::string title);


	std::vector<Movie> getAllVector();
	std::string getAllString();

	

	void sortVector(std::vector<Movie> &v, Comparator<Movie> &c);
	

};

