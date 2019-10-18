
#include "DynamicVector.h"

// Default constructor for DynamicVector
template<typename TElem>
DynamicVector<TElem>::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elems = new TElem[capacity];
}

// Copy constructor for DynamicVector
template<typename TElem>
DynamicVector<TElem>::DynamicVector(const DynamicVector<TElem>& v)
{
	this->size = v.size;
	this->capacity = v.capacity;

	this->elems = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

}

// Assignment operator for DynamicVector
template<typename TElem>
DynamicVector<TElem>& DynamicVector<TElem>::operator=(const DynamicVector<TElem>& v)
{
	if (this == &v)
		return *this;

	this->size = v.size;
	this->capacity = v.capacity;

	delete[] this->elems;

	this->elems = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

// Resize the DynamicVector
template<typename TElem>
void DynamicVector<TElem>::resize()
{
	this->capacity = this->capacity * 2;

	TElem *elementsToDelete = this->elems;

	this->elems = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = elementsToDelete[i];

	delete[] elementsToDelete;
}

// Add an element to the DynamicVector
template<typename TElem>
void DynamicVector<TElem>::add(const TElem& e)
{
	if (this->size == this->capacity)
		this->resize();

	this->elems[this->size++] = e;
}

// Remove an element from the DynamicVector
/*
	Remove an element from the DynamicVector.
	Input: e - TElem
	Precond: e has the id of the element to be removed
	Output: true, if the element was removed
			false, if the element did not exist
	Postcond: the first occurance of the element e is removed
*/
template<typename TElem>
bool DynamicVector<TElem>::remove(const TElem e)
{
	for (int i = 0; i < this->size; i++)
		if (this->elems[i] == e) 
		{
			for (int j = i; j < this->size - 1; j++)
				this->elems[j] = this->elems[j + 1];
			this->size--;
			return true;
		}

	return false;
}

// Update an element from the DynamicVector
/*
	Update an element from the DynamicVector.
	Input: e - TElem
	Precond: e has the id of the element to be updated
			 e contains the updated fields
	Output: true, if the element was updated
			false, if the element did not exist
	Postcond: the first occurance of the element e is updated
*/
template<typename TElem>
bool DynamicVector<TElem>::update(const TElem e)
{
	for (int i = 0; i < this->size; i++)
		if (this->elems[i] == e) {
			this->elems[i] = e;
			return true;
		}
	return false;
}

// Search for an element in the DynamicVector 
/*
	Search for an element in the DynamicVector.
	Input: e - TElem
	Precond: e has the id of searched element
	Output: position of TElem, if the TElem was found in the DynamicVector
			-1, otherwise
*/
template<typename TElem>
int DynamicVector<TElem>::search(const TElem e)
{	
	for (int i = 0; i < this->size; i++)
		if (this->elems[i] == e)
			return i;
	return -1;
}

// Get size of the DynamicVector
template<typename TElem>
int DynamicVector<TElem>::getSize() const
{
	return this->size;
}


// Destructor for DynamicVector
template<typename TElem>
DynamicVector<TElem>::~DynamicVector()
{
	delete[] this->elems;
}
