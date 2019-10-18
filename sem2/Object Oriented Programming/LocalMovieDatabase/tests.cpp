#include "tests.h"
#include "Repository.h"
#include "DynamicVector.h"
#include "Controller.h"
#include "ComparatorDescendingByYear.h"
#include <assert.h>
#include <algorithm>


void testMovie() {

	std::string title1 = "The Iron Giant";
	std::string genre1 = "animation";
	int year1 = 1999;
	int likes1 = 999;
	std::string trailer1 = "https://www.youtube.com/watch?v=fq2FZdvQXXg";

	Movie m1 = Movie(title1, genre1, year1, likes1, trailer1);

	m1 = m1;
	

	// Test getters
	assert(m1.getTitle() == title1);
	assert(m1.getGenre() == genre1);
	assert(m1.getYear() == year1);
	assert(m1.getLikes() == likes1);
	assert(m1.getTrailer() == trailer1);
	
	// Test setters
	Movie m2;

	m2.setTitle(title1);
	m2.setGenre(genre1);
	m2.setYear(year1);
	m2.setLikes(likes1);
	m2.setTrailer(trailer1);

	assert(m2.getTitle() == title1);
	assert(m2.getGenre() == genre1);
	assert(m2.getYear() == year1);
	assert(m2.getLikes() == likes1);
	assert(m2.getTrailer() == trailer1);

	// Test == operator
	assert(m1 == m2);

	// Test play
	m2.play();
}

void testRepository() {
	Repository v = Repository(5);
	v = v;
	

	assert(v.getSize() == 0);
	
	std::string title[] = { "The Iron Giant", "Gravity", "The Shining", "Airplane!", "Hangover" };
	std::string genre[] = { "animation", "sci-fi", "horror", "comedy", "comedy"};
	int year[] = { 1999, 2013, 1980, 1980, 2014};
	int likes[] = { 999, 340, 100, 121, 893 };
	std::string trailer[] = { "<link>", "<link>", "<link>", "<link>", "<link>" };

	// Test add
	for (int i = 0; i < 5; i++)
	{
		v.add(Movie(title[i], genre[i], year[i], likes[i], trailer[i]));

		try {
			v.add(Movie(title[i], genre[i], year[i], likes[i], trailer[i]));
			assert(false);
		}
		catch (std::runtime_error&) {
			assert(true);
		};
	}

	
	assert(v.getSize() == 5);

	// Test remove

	v.remove(Movie(title[2], "", 0, 0, ""));
	assert(v.getSize() == 4);

	try {
		v.remove(Movie(title[2], "", 0, 0, ""));
		assert(false);
	}
	catch (std::runtime_error&){
		assert(true);
	}

	// Test search
	assert(v.search(Movie(title[0], "", 0, 0, "")) == 0);
	assert(v.search(Movie(title[1], "", 0, 0, "")) == 1);
	assert(v.search(Movie(title[2], "", 0, 0, "")) == -1);
	assert(v.search(Movie(title[3], "", 0, 0, "")) == 2);
	assert(v.search(Movie(title[4], "", 0, 0, "")) == 3);



	// Test update
	try {
		v.update(Movie(title[2], "updated", 1, 9, "updated"));
		assert(false);
	}
	catch (std::runtime_error&){
		assert(true);
	}

	v.update(Movie(title[1], "updated", 1, 9, "updated"));

	// Test getElem

	assert(v.getElem(2) == Movie(title[3], "", 0, 0, ""));

	// Test getAll

	// Test getElemStr

	// Test data init repo
	DynamicVector<Movie> da = DynamicVector<Movie>();
	Repository vcopy = Repository(v);

	// Test operator=
	vcopy = v;

}

void testDynamicVector() {
	DynamicVector<Movie> v = DynamicVector<Movie>(5);
	v = v;

	assert(v.getSize() == 0);

	std::string title[] = { "The Iron Giant", "Gravity", "The Shining", "Airplane!", "Hangover" };
	std::string genre[] = { "animation", "sci-fi", "horror", "comedy", "comedy" };
	int year[] = { 1999, 2013, 1980, 1980, 2014 };
	int likes[] = { 999, 340, 100, 121, 893 };
	std::string trailer[] = { "<link>", "<link>", "<link>", "<link>", "<link>" };

	// Test add
	for (int i = 0; i < 5; i++)
	{
		v.add(Movie(title[i], genre[i], year[i], likes[i], trailer[i]));
	}

	assert(v.getSize() == 5);

	// Test operator=
	DynamicVector<Movie> vcopy;
	vcopy = v;

	// Test remove

	assert(v.remove(Movie(title[2], "", 0, 0, "")) == true);
	assert(v.getSize() == 4);
	assert(v.remove(Movie(title[2], "", 0, 0, "")) == false);

	// Test search
	assert(v.search(Movie(title[0], "", 0, 0, "")) == 0);
	assert(v.search(Movie(title[1], "", 0, 0, "")) == 1);
	assert(v.search(Movie(title[2], "", 0, 0, "")) == -1);
	assert(v.search(Movie(title[3], "", 0, 0, "")) == 2);
	assert(v.search(Movie(title[4], "", 0, 0, "")) == 3);

	// Add duplicates
	v.add(Movie(title[4], "", 0, 0, ""));
	v.add(Movie(title[3], "", 0, 0, ""));
	v.add(Movie(title[0], "", 0, 0, ""));


	// Test update

	assert(v.update(Movie(title[2], "updated", 1, 9, "updated")) == false);
	assert(v.update(Movie(title[1], "updated", 1, 9, "updated")) == true);
}

void testController() {
	Repository repo = Repository();
	WatchlistCSV wl;
	Controller cont = Controller(repo,wl);

	// Test add

	cont.add("title1", "genre1", 2001, 101, "url1");
	cont.add("title2", "genre2", 2002, 102, "url2");

	try {
		cont.add("title1", "genre1", 2001, 101, "url1");
		assert(false);
	}
	catch (std::runtime_error&){
		assert(true);
	}


	try {
		cont.add("title2", "genre2", 2002, 102, "url2");
		assert(false);
	}
	catch (std::runtime_error&){
		assert(true);
	}

	assert(repo.getSize() == 2);

	// Test remove
	cont.remove("title2");
	try {
		cont.remove("title2");
		assert(false);
	}	
	catch (std::runtime_error&) {
		assert(true);
	}

	assert(repo.getSize() == 1);

	// Test update
		
		//genre
	cont.updateGenre("title1", "animation");
	try {
		cont.updateGenre("empty", "animation");
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}
	
		//year
	cont.updateYear("title1", 2019);
	try {
		cont.updateYear("empty", 2019);
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}
		//likes
	cont.updateLikes("title1", 1);
	try {
		cont.updateLikes("empty", 1);
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}
		//trailer
	cont.updateTrailer("title1", "trailer_url");
	try {
		cont.updateTrailer("empty", "trailer_url");
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}

	Movie m = repo.getElem(repo.search(Movie("title1", "", 0, 0, "")));
	assert(m.getGenre() == "animation");
	assert(m.getLikes() == 1);
	assert(m.getYear() == 2019);
	assert(m.getTrailer() == "trailer_url");

	// Test select movies
	Repository movies = cont.selectMovies("animation");
	assert(movies.getSize() == 1);
	movies = cont.selectMovies("");

	// Test incLikes

	cont.incLikes("title1");
	assert(repo.getElem(repo.search(Movie("title1", "", 0, 0, ""))).getLikes() == 2);


	// Test addToWatchlist
	cont.addToWatchlist(m);

	try {
		cont.addToWatchlist(m);
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}

	// Test removeFromWatchlist
	cont.removeFromWatchlist("title1");
	try {
		cont.removeFromWatchlist("empty");
		assert(false);
	}
	catch (std::runtime_error&) {
		assert(true);
	}
	

	// Test getWatchlist
	std::string watchlist = cont.getWatchlist();

	
	// Test getAll
	std::string allMovies = cont.getAllString();
}


void lab5_activity() {

	Repository repo = Repository();


	Movie movie1 = Movie("title1", "genre1", 2001, 101, "url1");
	Movie movie2 = Movie("title2", "genre2", 2002, 102, "url2");

	repo = repo + movie1;
	repo = movie2 + repo;

	//std::cout << repo.getAllString();

	assert(repo.getSize() == 2);
}





void testSort_lab8() {

	std::vector<Movie> movies, sorted_movies;
	ComparatorDescendingByYear compareByYear;

	for (unsigned i = 0; i < 10; i++)
	{
		movies.push_back(Movie("title", "genre", 2000 + i, 1, "url"));
		sorted_movies.push_back(Movie("title", "genre", 2010 - i - 1, 1, "url"));
	}

	Repository repo = Repository(movies);
	WatchlistCSV wl;
	Controller cont = Controller(repo, wl);
	
	auto v = cont.getAllVector();

	cont.sortVector(v, compareByYear);

	assert(movies == sorted_movies);

}


void testAll() {

	testMovie();
	testDynamicVector();
	//testRepository();
	testController();

	lab5_activity();
	testSort_lab8();
}