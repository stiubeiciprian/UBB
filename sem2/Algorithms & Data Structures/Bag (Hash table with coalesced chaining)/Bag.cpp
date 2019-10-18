#include "Bag.h"
#include "BagIterator.h"

Bag::Bag()
{
	this->m = 30;
	this->sizeOfBag = 0;
	this->ht = new TElem[this->m];
	this->next = new int[this->m];
	
	for (int i = 0; i < this->m; i++) {
		this->next[i] = -2;
	}
	this->firstFree = 0;

}

void Bag::findNextFreePosition() {
	while (firstFree < m && next[firstFree] != -2)
		firstFree++;
}

void Bag::resize() {
		TElem* htToDelete = this->ht;
		int* nextToDelete = this->next;
		this->firstFree = 0;
		this->sizeOfBag = 0;
	
		this->ht = new TElem[this->m*2];
		this->next = new int[this->m*2];

		// Empty all positions
		for (int i = 0; i < this->m*2; i++) {
			this->next[i] = -2;
		}
		
		// Add elements
		for (int i = 0; i < this->m; i++)
			if (nextToDelete[i] != -2)
				add(htToDelete[i]);

		delete[] htToDelete;
		delete[] nextToDelete;
	
		this->m *= 2;
}	

//adds an element to the bag
void Bag::add(TElem e) {
	// O(m)

	int pos = hash(e);


	// If container is full resize and rehash
	if (this->sizeOfBag == this->m)
		resize();


	this->sizeOfBag++;

	// If the position is empty add element
	if (next[pos] == -2)
	{
		ht[pos] = e;
		next[pos] = -1;

		if (pos == firstFree)
			findNextFreePosition();
	}
	// Find the end of the chain and add element
	else {

		while (next[pos] != -1)
			pos = next[pos];

		next[pos] = firstFree;
		ht[firstFree] = e;
		next[firstFree] = -1;
		findNextFreePosition();
	}
	
	
}

//removes one occurrence of an element from a bag
//returns true if an element was removed, false otherwise (if e was not part of the bag)
bool Bag::remove(TElem e) {
	// O(m)

	int prev = -1;
	int elemToDeletePos = -1;
	int pos = this->hash(e);

	// Element is not in container
	if (this->next[pos] == -2)
		return false;

	// Find first occurence of element
	while (pos != -1 && this->ht[pos] != e) {
		prev = pos;
		pos = this->next[pos];
	}
	elemToDeletePos = pos;

	// Element not in container
	if (elemToDeletePos == -1)
		return false;
	
	if (this->next[elemToDeletePos] == -1)
	{
		this->next[prev] = -1;
		this->next[elemToDeletePos] =-2;
		this->sizeOfBag--;
		return true;
	}
	while (this->next[elemToDeletePos] != -1) {
		this->ht[elemToDeletePos] = this->ht[this->next[elemToDeletePos]];
		prev = elemToDeletePos;
		elemToDeletePos = this->next[elemToDeletePos];
	}


	if (prev != -1)
		this->next[prev] = -1;

	this->next[elemToDeletePos] = -2;

	this->sizeOfBag--;
	return true;

}


//checks if an element appearch is the bag
bool Bag::search(TElem e) const {
	//O(m)
	int pos = this->hash(e);

	while (pos >= 0) {
		if (this->ht[pos] == e)
			return true;
		pos = this->next[pos];
	}

	return false;
}

//returns the number of occurrences for an element in the bag
int Bag::nrOccurrences(TElem e) const {
	// O(m)
	int count = 0;
	int pos = this->hash(e);

	while (pos >= 0) {
		if (this->ht[pos] == e)
			count++;
		pos = this->next[pos];
	}

	return count;
}

//returns the number of elements from the bag
int Bag::size() const {
	//theta(1)
	return this->sizeOfBag;
}

//returns an iterator for this bag
BagIterator Bag::iterator() const {
	return BagIterator(*this);
}

//checks if the bag is empty
bool Bag::isEmpty() const {
	//theta(1)
	return this->sizeOfBag == 0;
}

//returns hash of element
int Bag::hash(TElem e) const{
	//theta(1)
	if (e < 0)
		return -e % this->m;
	else
		return e % this->m;
}

Bag::~Bag()
{
	delete[] this->ht;
	delete[] this->next;
}
