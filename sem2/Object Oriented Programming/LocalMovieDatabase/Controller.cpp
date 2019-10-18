#include "Controller.h"
#include "Movie.h"
#include <Windows.h>
#include "WatchlistCSV.h"
#include "WatchlistHTML.h"
#include "FileRepository.h"


using namespace std;


bool Controller::add(std::string title, std::string genre, int year, int likes, std::string trailer)
{
	Movie m = Movie(title, genre, year, likes, trailer);

	this->validatorMovie.validate(m);

	return this->repo.add(m);
}

bool Controller::remove(std::string title)
{
	return this->repo.remove(Movie(title, "", 0, 0, ""));
}



bool Controller::updateGenre(std::string title, std::string new_genre)
{
	int position = this->repo.search(Movie(title, "", 0, 0, ""));

	if (position == -1)
		throw std::runtime_error("Cannot update inexisting element!\n");

	Movie e = this->repo.getElem(position);
	e.setGenre(new_genre);
	this->repo.update(e);

	return true;
}

bool Controller::updateYear(std::string title, int new_year)
{
	int position = this->repo.search(Movie(title, "", 0, 0, ""));

	if (position == -1)
		throw std::runtime_error("Cannot update inexisting element!\n");

	Movie e = this->repo.getElem(position);
	e.setYear(new_year);
	this->repo.update(e);

	return true;
}

bool Controller::updateLikes(std::string title, int new_likes)
{
	int position = this->repo.search(Movie(title, "", 0, 0, ""));

	if (position == -1)
		throw std::runtime_error("Cannot update inexisting element!\n");

	Movie e = this->repo.getElem(position);
	e.setLikes(new_likes);
	this->repo.update(e);

	return true;
}

bool Controller::updateTrailer(std::string title, std::string new_trailer)
{	
	int position = this->repo.search(Movie(title, "", 0, 0, ""));

	if (position == -1)
		throw std::runtime_error("Cannot update inexisting element!\n");

	Movie e = this->repo.getElem(position);
	e.setTrailer(new_trailer);
	this->repo.update(e);

	return true;
}


std::string Controller::getAllString() 
{
	return this->repo.getAllString();
}


Repository Controller::selectMovies(std::string genre) {
	Repository movies;

	if (genre == "") {
		movies = this->repo;
		return movies;
	}

	for (int i = 0; i < this->repo.getSize(); i++)
		if (this->repo.getElem(i).getGenre() == genre)
			movies.add(this->repo.getElem(i));

	return movies;
}


bool Controller::addToWatchlist(Movie m) {
	this->watchlist.add(m);
	this->watchlist.writeToFile();

	return true;
}

bool Controller::removeFromWatchlist(std::string title) {
	this->watchlist.remove(Movie(title, "", 0, 0, ""));
	this->watchlist.writeToFile();

	return true;
}

void Controller::displayWatchlist()
{
	this->watchlist.openFile();
}

std::string Controller::getWatchlist() {
	return this->watchlist.getAllString();
}


void Controller::incLikes(std::string title) {
	Movie elem = this->repo.getElem(this->repo.search(Movie(title, "", 0, 0, "")));
	elem.setLikes(elem.getLikes() + 1);
	this->repo.update(elem);
}

std::vector<Movie> Controller::getAllVector() {
	return this->repo.getAll();
}

void Controller::sortVector(std::vector<Movie> &v, Comparator<Movie> &c) {
	Movie aux;

	for (unsigned i = 0; i < v.size() - 1; i++)
		for (unsigned j = i + 1; j < v.size(); j++)
			if (c.compare(v[i], v[j]))
			{
				aux = v[i];
				v[i] = v[j];
				v[j] = aux;
			}

}