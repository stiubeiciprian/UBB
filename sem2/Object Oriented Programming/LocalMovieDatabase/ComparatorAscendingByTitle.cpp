#include "ComparatorAscendingByTitle.h"



ComparatorAscendingByTitle::ComparatorAscendingByTitle()
{
}

bool ComparatorAscendingByTitle::compare(Movie& m1, Movie& m2) const {
	if (m1.getTitle() < m2.getTitle())
		return true;
	return false;
}

ComparatorAscendingByTitle::~ComparatorAscendingByTitle()
{
}
