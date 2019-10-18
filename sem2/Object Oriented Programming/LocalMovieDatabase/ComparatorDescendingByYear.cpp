#include "ComparatorDescendingByYear.h"

ComparatorDescendingByYear::ComparatorDescendingByYear(){}

bool ComparatorDescendingByYear::compare(Movie& m1, Movie& m2) const{
	if (m1.getYear() < m2.getYear())
		return true;
	return false;
}

ComparatorDescendingByYear::~ComparatorDescendingByYear(){}
