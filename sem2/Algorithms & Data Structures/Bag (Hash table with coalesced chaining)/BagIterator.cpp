#include "BagIterator.h"

int BagIterator::findNextOccupiedPosition(int startPosition)
{	//O(n)
	int i = startPosition;

	if (startPosition == c.sizeOfBag)
		return startPosition + 1;
	i++;
	while (i < c.size() && c.next[i] ==-2)
		i++;

	return i;
}

BagIterator::BagIterator(const Bag& c) : c{ c } {}


void BagIterator::first()
{	
	currentElement = findNextOccupiedPosition(0);
}

void BagIterator::next()
{
	if (valid() == false)
		throw std::exception();

	currentElement = findNextOccupiedPosition(currentElement);


}

bool BagIterator::valid() const
{
	//theta(1)
	if (c.sizeOfBag == 0)
		return false;

	return currentElement < c.size();
}

TElem BagIterator::getCurrent() const
{
	//theta(1)
	if (valid() == false)
		throw std::exception();

	return c.ht[currentElement];
}


BagIterator::~BagIterator()
{
}
