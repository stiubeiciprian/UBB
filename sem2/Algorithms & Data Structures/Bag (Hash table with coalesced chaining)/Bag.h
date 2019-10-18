#pragma once
#include <iostream>

class BagIterator;

typedef int TElem;

class Bag {
	friend class BagIterator;
private:

	/*representation of Bag*/
	TElem *ht;
	int *next;
	int m, sizeOfBag, firstFree;


	int hash(TElem e) const;

	void findNextFreePosition();

	void resize();


public:
	void print()
	{
		std::cout << "\nIndexes\n";
		for (int i = 0; i < m; i++)
			std::cout << i <<" ";
		std::cout << "\n\nContents\n";
		for (int i = 0; i < m; i++)
			if (this->next[i] == -2)
				std::cout << "/ ";
			else 
				std::cout << this->ht[i] << " ";
		std::cout << "\n\nNext\n";
		for (int i = 0; i < m; i++)
			std::cout << this->next[i] << " ";
	}
	//constructor
	Bag();

	//adds an element to the bag
	void add(TElem e);

	//removes one occurrence of an element from a bag
	//returns true if an element was removed, false otherwise (if e was not part of the bag)
	bool remove(TElem e);


	//checks if an element appearch is the bag
	bool search(TElem e) const;

	//returns the number of occurrences for an element in the bag
	int nrOccurrences(TElem e) const;

	//returns the number of elements from the bag
	int size() const;

	//returns an iterator for this bag
	BagIterator iterator() const;

	//checks if the bag is empty
	bool isEmpty() const;

	
	//destructor
	~Bag();

};