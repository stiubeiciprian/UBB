#include "PriorityQueue.h"


//implicit constructor
PriorityQueue::PriorityQueue(Relation r) {
	// theta(1)

	this->priorityRelation = r;
	this->firstEmpty = 0;
	this->head = -1;
	this->tail = -1;

	this->size = 0;
	this->capacity = 150;
	
	this->elems = new NodeDLLA[this->capacity];
	

	for (int i = 0; i < this->capacity; i++) {
		this->elems[i].next = i + 1;
		this->elems[i].prev = i - 1;
	}

	this->elems[0].prev = -1;
	this->elems[this->capacity - 1].next = -1;
}

// resize arrays
void PriorityQueue::resize() {
	// theta(n)
	NodeDLLA* elemsToDelete;

	elemsToDelete = this->elems;

	this->capacity *= 2;

	// Alloc new array
	this->elems = new NodeDLLA[this->capacity];
	

	// Copy elements to new array
	for (int i = 0; i < this->size; i++)
	{
		this->elems[i] = elemsToDelete[i];
	}

	// Initialize empty positions links
	for (int i = this->size; i < this->capacity; i++)
	{
		this->elems[i].next = i + 1;
		this->elems[i].prev = i - 1;
	}

	this->firstEmpty = this->size;

	this->elems[this->size].prev = -1;
	this->elems[this->capacity - 1].next = -1;


}


//adds an element with priority to the queue
void PriorityQueue::push(TElem e, TPriority p) {
	//theta(1)

	if (this->size == this->capacity)
		this->resize();

	if (this->size == 0) {
		
		this->head = firstEmpty;
		this->tail = firstEmpty;

		// Add element on the first empty position
		this->elems[firstEmpty].data = std::make_pair(e, p);

		// Update firstEmpty
		this->firstEmpty = this->elems[this->firstEmpty].next;
		

		// Link nodes
		this->elems[this->firstEmpty].prev = -1;

		this->elems[this->head].next = -1;
		this->elems[this->head].prev = -1;

	}
	else {
		
		int prevTail = this->tail;

		// Add element on the first empty position
		this->elems[firstEmpty].data = std::make_pair(e, p);
		this->tail = this->firstEmpty;

		// Update firstEmpty
		this->firstEmpty = this->elems[this->firstEmpty].next;
		this->elems[this->firstEmpty].prev = -1;

		// Link nodes
		this->elems[this->tail].next = -1;
		this->elems[this->tail].prev = prevTail;
		this->elems[prevTail].next = this->tail;
		
	}

	this->size++;

}



//returns the element with the highest priority with respect to the order relation
//throws exception if the queue is empty
Element PriorityQueue::top()  const {
	// O(n)

	if (this->size == 0)
		throw std::exception();

	int current = this->head;
	int highest_priority = current;

	// Search for the highest priority element
	while (current != -1) {

		if (this->priorityRelation(this->elems[current].data.second, this->elems[highest_priority].data.second))
			highest_priority = current;

		current = this->elems[current].next;
	}

	return this->elems[highest_priority].data;
}



//removes and returns the element with the highest priority
//throws exception if the queue is empty
Element PriorityQueue::pop() {
	// theta(n)


	if (this->size == 0)
		throw std::exception();

	int current = this->head;
	int highest_priority = current;

	// Search for the highest priority element
	while (current != -1) {

		if (this->priorityRelation(this->elems[current].data.second, this->elems[highest_priority].data.second))
			highest_priority = current;

		current = this->elems[current].next;
	}


	// Remove highest priority element

	if (this->head == highest_priority)
		this->head = this->elems[highest_priority].next;

	if (this->tail == highest_priority)
		this->tail = this->elems[highest_priority].prev;

	this->elems[this->elems[highest_priority].prev].next = this->elems[highest_priority].next;
	this->elems[this->elems[highest_priority].next].prev = this->elems[highest_priority].prev;
	
	this->elems[highest_priority].prev = -1;
	this->elems[this->firstEmpty].prev = highest_priority;
	this->elems[highest_priority].next = this->firstEmpty;

	this->firstEmpty = highest_priority;
	this->size--;

	return this->elems[highest_priority].data;

}



//checks if the queue is empty

bool PriorityQueue::isEmpty() const {
	//theta(1)

	if (this->size == 0)
		return true;
	return false;
}


PriorityQueue::~PriorityQueue() {
	//delete[] this->elems;
}