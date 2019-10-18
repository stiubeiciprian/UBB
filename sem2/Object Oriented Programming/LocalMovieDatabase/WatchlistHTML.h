#pragma once
#include "Watchlist.h"

class WatchlistHTML : public Watchlist
{
public:
	WatchlistHTML();
	void writeToFile();
	void openFile();
	~WatchlistHTML();
};

