#include "FileRepository.h"


using namespace std;

FileRepository::FileRepository()
{
	this->readObjects();
}


void FileRepository::readObjects()
{
	ifstream f("Movies.csv");
	if (!f.is_open())
		throw std::runtime_error("Elements cannot be loaded. File is open.\n");

	Movie m{};
	while (f >> m) {
		this->add(m);
	}

	f.close();
}

void FileRepository::writeObjects()
{
	ofstream f("Movies.csv", ios::in);
	if (!f.is_open())
		throw std::runtime_error("File cannot be oppened!\n");

	vector<Movie> movies = this->getAll();

	for (Movie m : movies)
	{
		f << m;
	}

	f.close();
}


FileRepository::~FileRepository()
{
	this->writeObjects();
}
