#include "bag.h"


Bag::Bag()
{	
	// Theta(1)
	this->length = 0;
	this->capacity = 50;

	this->elems = new TElem[this->capacity];
	this->freq = new TElem[this->capacity];
}

void Bag::resize()
{	
	// O(n)

	TElem *elemsToDel = this->elems, *freqToDel = this->freq;

	this->elems = new TElem[2 * this->capacity];
	this->freq = new TElem[2 * this->capacity];

	for (int i = 0; i < this->length; i++) {
		this->elems[i] = elemsToDel[i];
		this->freq[i] = freqToDel[i];
	}

	this->capacity *= 2;

	delete[] elemsToDel;
	delete[] freqToDel;
}

void Bag::add(TElem e)
{	
	// O(n)

	if (this->length + 1 == this->capacity)
		resize();

	if (search(e) == true) {

		for (int i = 0; i < this->length; i++)
			if (this->elems[i] == e)
				this->freq[i]++;

	}
	else 
	{
		this->elems[this->length] = e;
		this->freq[this->length] = 1;
		this->length++;
	}
}

bool Bag::remove(TElem e)
{	
	// O(n)

	if (search(e) == false)
		return false;

	for (int i = 0; i < this->length; i++) 
	{
		if (this->elems[i] == e) {
			this->freq[i]--;

			if (this->freq[i] == 0)
			{
				this->length--;

				for (int j = i; j < this->length; j++)
				{
					this->elems[j] = this->elems[j + 1];
					this->freq[j] = this->freq[j + 1];
				}

			}

			return true;
		}
	}

	return true;
}

bool Bag::search(TElem e) const
{
	// O(n)
	for (int i = 0; i < this->length; i++)
		if (this->elems[i] == e)
			return true;
	return false;
}

int Bag::nrOccurrences(TElem e) const
{
	// O(n)
	if (search(e) == false)
		return 0;

	for (int i = 0; i < this->length; i++)
		if (this->elems[i] == e)
			return this->freq[i];

	return 0;
}

int Bag::size() const
{
	// O(n)
	if (isEmpty() == true)
		return 0;

	int total = 0;

	for (int i = 0; i < this->length; i++)
		total += this->freq[i];

	return total;

}

BagIterator Bag::iterator() const
{
	// Theta(1)
	return BagIterator(*this);
}

bool Bag::isEmpty() const
{	
	// Theta(1)
	if (this->length == 0)
		return true;
	return false;
}



TElem Bag::getElem(int position) const {
	// Theta(1)
	return this->elems[position];
}

int Bag::getLength() const {
	// Theta(1)
	return this->length;
}


/*
	leastFrequent():
		
		if container_length == 0 then:
			leastFrequent <- NULL_ELEM

		min_element_position <- 0

		for i<-0 to container_length:
			if frequency[i] < frequency[min_element_position] then:
				min_element_position <- i

		leastFrequent <- elements[min_element_position]
*/

//returns the TElem with the smallest frequency from the Bag
//if the Bag is empty, it returns NULL_TELEM
TElem Bag::leastFrequent() const {
	/*
	Best case: Theta(1)
	Worst case: Theta(n)
	Average case: O(n)
	*/
	if (this->length == 0)
		return NULL_TELEM;

	TElem minElemPosition = 0;

	for (int i = 0; i < this->length; i++) {
		if (this->freq[i] < this->freq[minElemPosition])
			minElemPosition = i;
	}

	return this->elems[minElemPosition];

}

Bag::~Bag()
{	// Theta(1)
	delete[] this->elems;
}
