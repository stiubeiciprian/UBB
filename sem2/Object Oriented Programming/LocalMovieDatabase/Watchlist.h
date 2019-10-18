#pragma once
#include "Movie.h"
#include "Repository.h"

class Watchlist : public Repository
{
public:
	Watchlist();
	virtual void writeToFile()=0;
	virtual void openFile()=0;
	virtual ~Watchlist();
};

