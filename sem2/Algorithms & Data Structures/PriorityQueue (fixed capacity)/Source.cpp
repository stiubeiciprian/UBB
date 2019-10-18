#include "PriorityQueue.h"
#include <assert.h>
#include <exception>
#include <iostream>

bool rel(TPriority p1, TPriority p2) {
	if (p1 <= p2) {
		return true;
	}
	else {
		return false;
	}
}

int main() {


	PriorityQueue pq{rel,2};
	//pq = PriorityQueue(rel, 2);
	



	// pq is not full
	assert(pq.isFull() == false);



	pq.push(10, 10);
	pq.push(20, 20);



	// pq is full
	assert(pq.isFull() == true);




	// cannot add another element to a full queue
	try {
		pq.push(30, 30);
		assert(false);
	}
	catch (std::exception&) {
		assert(true);
	}
	



	return 0;
}