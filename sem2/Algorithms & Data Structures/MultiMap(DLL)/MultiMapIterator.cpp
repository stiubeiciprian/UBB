#include "MultiMapIterator.h"

MultiMapIterator::MultiMapIterator(const MultiMap &c) : c(c) {
	// Theta(1)
	this->current = this->c.getFirst();
}

void MultiMapIterator::first() {
	// Theta(1)
	this->current = this->c.getFirst();
}

void MultiMapIterator::next() {
	// Theta(1)
	this->current = this->current->next;
}

bool MultiMapIterator::valid() const {
	// Theta(1)
	if (this->current == NULL)
		return false;
	return true;
}

TElem MultiMapIterator::getCurrent() const {
	// Theta(1)
	return this->current->data;
}