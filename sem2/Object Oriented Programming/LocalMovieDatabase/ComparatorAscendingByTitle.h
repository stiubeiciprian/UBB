#pragma once
#include "Comparator.h"
#include "Movie.h"

class ComparatorAscendingByTitle : public Comparator<Movie>
{
public:
	ComparatorAscendingByTitle();
	bool compare(Movie& m1, Movie& m2) const override;
	~ComparatorAscendingByTitle();
};

