#include "BagIterator.h"

BagIterator::BagIterator(const Bag& b) : c(b) {
	// Theta(1)
	this->position = 0;
}

void BagIterator::first() {
	// Theta(1)
	this->position = 0;
}

void BagIterator::next() {
	// Theta(1)

	if (this->valid() == false)
		throw;

		if (this->currentCount == this->c.nrOccurrences(this->c.getElem(this->position)))
			this->position++, this->currentCount = 1;
		else this->currentCount++;

}

int BagIterator::getCurrent() const {
	// Theta(1)
	if (this->valid() == false)
		throw;
	return this->c.getElem(this->position);
}


bool BagIterator::valid() const {
	// Theta(1)
	if (this->position >= this->c.getLength())
		return false;
	return true;
}

