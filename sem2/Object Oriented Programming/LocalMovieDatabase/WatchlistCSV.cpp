#include "WatchlistCSV.h"
#include <fstream>
#include <sstream>
#include <Windows.h>
#include <iostream>

using namespace std;

WatchlistCSV::WatchlistCSV()
{
}

void WatchlistCSV::writeToFile()
{
	ofstream f("Watchlist.csv", ios::in);
	if (!f.is_open())
		throw std::runtime_error("File cannot be oppened!\n");

	vector<Movie> movies = this->getAll();

	for (Movie m : movies)
	{
		f << m;
	}

	f.close();
}

void WatchlistCSV::openFile() {
	ShellExecuteA(0, 0, "notepad.exe", "Watchlist.csv", 0, SW_SHOWMAXIMIZED);
}

WatchlistCSV::~WatchlistCSV()
{
}
