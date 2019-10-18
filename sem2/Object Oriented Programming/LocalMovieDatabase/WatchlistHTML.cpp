#include "WatchlistHTML.h"
#include <fstream>
#include <sstream>
#include <Windows.h>

using namespace std;

WatchlistHTML::WatchlistHTML()
{
}

void WatchlistHTML::writeToFile()
{
	ofstream f("Watchlist.html", ios::in);
	if (!f.is_open())
		throw std::runtime_error("File cannot be oppened!\n");

	f << "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Playlist</title>\n\t</head>\n\t<body>\n\t\t<table border = \"1\">\n\t\t\t<tr><td>Movie</td><td>Genre</td><td>Year</td><td>Likes</td><td>Youtube link</td></tr>\n";

	vector<Movie> movies = this->getAll();

	for (Movie m : movies)
	{
		f << "\t\t\t<tr>"
			<< "<td>" << m.getTitle() << "</td>"
			<< "<td>" << m.getGenre() << "</td>"
			<< "<td>" << m.getYear() << "</td>"
			<< "<td>" << m.getLikes() << "</td>"
			<< "<td>" << m.getTrailer() << "</td>"
		<< "</tr>\n";
	}
	
	f << "\t\t</table>\n\t</body>\n</html>";

	f.close();
}

void WatchlistHTML::openFile() {
	ShellExecuteA(0, 0, "chrome.exe", "Watchlist.html", 0, SW_SHOWMAXIMIZED);
}

WatchlistHTML::~WatchlistHTML()
{
}
