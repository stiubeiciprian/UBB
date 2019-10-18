#include "MultiMapKeyIterator.h"

MultiMapKeyIterator::MultiMapKeyIterator(const MultiMap &c) : c(c) {
	// Theta(1)
	this->current = this->c.getFirst();

}

void MultiMapKeyIterator::first() {
	// Theta(1)
	this->current = this->c.getFirst();
}


void MultiMapKeyIterator::next() {
	// O(n)

	if (this->current == NULL)
		return;

	this->iteratedKeys.insert(std::get<0>(this->current->data));

	while (this->current !=NULL && find(this->iteratedKeys.begin(), this->iteratedKeys.end(), std::get<0>(this->current->data)) != this->iteratedKeys.end())
		this->current = this->current->next;
}

bool MultiMapKeyIterator::valid() const {
	// Theta(1)
	if (this->current == NULL)
		return false;
	return true;
}

TKey MultiMapKeyIterator::getCurrent() const {
	// Theta(1)

	return std::get<0>(this->current->data);
}