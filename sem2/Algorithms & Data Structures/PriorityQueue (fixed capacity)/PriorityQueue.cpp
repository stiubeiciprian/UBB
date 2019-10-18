#include "PriorityQueue.h"


PriorityQueue::PriorityQueue(Relation r, int cap) {
	// theta(capacity)

	if (cap <= 0)
		throw std::exception();

	this->priorityRelation = r;
	this->firstEmpty = 0;
	this->head = -1;
	this->tail = -1;

	this->size = 0;
	this->capacity = cap;
	
	this->elems = new NodeDLLA[this->capacity];
	

	for (int i = 0; i < this->capacity; i++) {
		this->elems[i].next = i + 1;
		this->elems[i].prev = i - 1;
	}

	this->elems[0].prev = -1;
	this->elems[this->capacity - 1].next = -1;
}


/*	Complexity: theta(1)

	method push(element, priority)
		
		if priorityQueue.size = priorityQueue.capacity
			throw exception
		end-if

		if priorityQueue.size = 0
			
				priorityQueue.head <- firstEmpty
				priorityQueue.tail <- firstEmpty

				priorityQueue.elems[firstEmpty].data <- pair(element, priority)

				priorityQueue.firstEmpty <- priorityQueue.elems[firstEmpty].next

				priorityQueue[firstEmpty].prev <- -1

				priorityQueue.elems[head].next <- -1
				priorityQueue.elems[head].prev <- -1
		
		else
			
				previousTail <- priorityQueue.tail

				priorityQueue.elems[firstEmpty].data <- pair(element, priority)

				priorityQueue.tail <- firstEmpty;
		
				priorityQueue.firstEmpty <- priorityQueue.elems[firstEmpty].next
				priorityQueue.elems[firstEmpty].prev <- -1

				priorityQueue.elems[tail].next <- -1
				priorityQueue.elems[tail].prev <- prevTail
				priorityQueue.elems[prevTail].next <- priorityQueue.tail
	
		end-if

		
		priorityQueue.size = priorityQueue.size + 1 


	end-method


*/

//adds an element with priority to the queue
void PriorityQueue::push(TElem e, TPriority p) {
	// theta(1)

	if (this->size == this->capacity)
		throw std::exception();

	if (this->size == 0) {
		
		this->head = firstEmpty;
		this->tail = firstEmpty;

		// Add element on the first empty position
		this->elems[firstEmpty].data = std::make_pair(e, p);

		this->elems[0];
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





/*
	Complexity: theta(1)

	method isFull()

		if priorityQueue.size = priorityQueue.capaciy
			isFull <- true
		end-if

		isFull <- false

	end-method
*/

//checks if the queue is full
bool PriorityQueue::isFull() const {
	if (this->size == this->capacity)
		return true;
	return false;
}



//checks if the queue is empty

bool PriorityQueue::isEmpty() const {
	if (this->size == 0)
		return true;
	return false;
}


PriorityQueue& PriorityQueue::operator=(PriorityQueue& pq)
{
	if (this == &pq)
		return *this;

	this->capacity = pq.capacity;
	this->size = pq.size;
	this->firstEmpty = pq.firstEmpty;
	this->head = pq.head;
	this->tail = pq.tail;
	this->elems = pq.elems;
	this->priorityRelation = pq.priorityRelation;

	return *this;
}






//destructor

PriorityQueue::~PriorityQueue() {
	delete[] this->elems;	
}