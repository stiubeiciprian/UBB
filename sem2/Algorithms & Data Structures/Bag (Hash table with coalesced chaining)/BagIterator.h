#pragma once
#include "Bag.h"
class Bag;

class BagIterator {

private:

	

	const Bag& c;

	/* representation specific for the iterator*/

	int findNextOccupiedPosition(int startPosition);
	int currentElement = findNextOccupiedPosition(0);



public:

	BagIterator(const Bag& c);

	void first();

	void next();

	bool valid() const;

	TElem getCurrent() const;

	~BagIterator();

};