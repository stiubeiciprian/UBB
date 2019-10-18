#pragma once
#include "Watchlist.h"

class WatchlistCSV : public Watchlist
{
public:
	WatchlistCSV();
	void writeToFile();
	void openFile();
	~WatchlistCSV();
};

