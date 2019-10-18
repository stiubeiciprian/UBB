#pragma once
#include "Repository.h"
#include "Movie.h"
#include <fstream>
#include <sstream>
#include <vector>


class FileRepository : public Repository
{
public:
	FileRepository();

	void readObjects();
	void writeObjects();

	~FileRepository();
};

