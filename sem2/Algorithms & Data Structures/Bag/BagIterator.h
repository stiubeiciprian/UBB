#pragma once
#include "bag.h"

class Bag;

class BagIterator {
	friend class Bag;
private:

	int currentCount = 1;
	int position = 0;

	//contains a reference of the container it iterates over
	const Bag&  c;

public:

	//Constructor receives a reference of the container.
	//after creation the iterator will refer to the first element of the container, or it will be invalid if the container is empty
	BagIterator(const Bag& c);

	//sets the iterator to the first element of the container
	void first();

	//moves the iterator to the next element
	//throws exception if the iterator is not valid
	void next();

	//returns the value of the current element from the iterator
	// throws exception if the iterator is not valid
	//TElem getCurrent() const;
	int getCurrent() const;

	//checks if the iterator is valid
	bool valid() const;

};


