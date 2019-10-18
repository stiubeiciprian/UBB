#include "MultiMap.h"
#include "MultiMapIterator.h"
#include "MultiMapKeyIterator.h"
#include <vector>
#include<utility>

MultiMap::MultiMap() {
	// Theta(1)
	this->length = 0;
}


void MultiMap::add(TKey c, TValue v) {
	// Theta(1)

	if (length == 0) {
		this->first = new node;
		this->first->data = std::make_pair(c, v);

		this->first->next = nullptr;
		this->first->prev = nullptr;

		this->last = this->first;

		this->length++;
	}
	else {

		node* new_node = new node;
		
		// Fill data
		new_node->data = std::make_pair(c, v);

		// Link elems
		this->last->next = new_node;
		new_node->prev = this->last;
		new_node->next = nullptr;

		// Update last elem
		this->last = new_node;

		this->length++;
	}
}



//removes a key value pair from the multimap

//returns true if the pair was removed (if it was in the multimap) and false otherwise

bool MultiMap::remove(TKey c, TValue v) {
	// O(n)
	node* current = this->first;
	

	if (current == nullptr)
		return false;

	if (get<0>(current->data) == c && get<1>(current->data) == v) {
		this->first = current->next;
		delete current;
		this->length--;

		return true;
	}

	node* prev = nullptr;

	while (current != nullptr && !(get<0>(current->data) == c && get<1>(current->data) == v)) {
		prev = current;
		current = current->next;
	}
	
	if (current == nullptr)
		return false;

	prev->next = current->next;
	delete current;
	this->length--;

	return true;
}



//returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty

vector<TValue> MultiMap::search(TKey c) const {
	// O(n)

	std::vector<TValue> v;

	node* current = this->first;

	while (current != nullptr ) {
		if (get<0>(current->data) == c) {
			v.push_back(get<1>(current->data));
		}
		current = current->next;
	}

	return v;
}



//returns the number of pairs from the multimap

int MultiMap::size() const {
	// Theta(1)
	return this->length;
}



//checks whether the multimap is empty

bool MultiMap::isEmpty() const {
	// Theta(1)
	if (this->length == 0)
		return true;
	return false;
}


MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

MultiMapKeyIterator MultiMap::keyIterator() const {
	return MultiMapKeyIterator(*this);
}

node* MultiMap::getFirst()  const {
	// Theta(1)
	return this->first;
}

node* MultiMap::getLast() const {
	// Theta(1)
	return this->last;
}

MultiMap::~MultiMap() {
	// O(n)
	node* current = this->first;

	while (current != nullptr) {
		node* c_next = current->next;
		delete current;
		current = c_next;
	}
}
