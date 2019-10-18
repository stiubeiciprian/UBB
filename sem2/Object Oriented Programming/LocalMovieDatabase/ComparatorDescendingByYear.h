#pragma once
#include "Comparator.h"
#include "Movie.h"

class ComparatorDescendingByYear : public Comparator<Movie>
{
public:
	ComparatorDescendingByYear();
	bool compare(Movie& m1, Movie& m2) const override;
	~ComparatorDescendingByYear();
};

