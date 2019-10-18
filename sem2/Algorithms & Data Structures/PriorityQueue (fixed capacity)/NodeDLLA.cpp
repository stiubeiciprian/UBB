#include "NodeDLLA.h"


NodeDLLA::NodeDLLA(Element e, int next, int prev) : data{ e }, next{ next }, prev{ prev } {};

NodeDLLA& NodeDLLA::operator=(const NodeDLLA& e) {
	if (this == &e)
		return *this;

	this->data = e.data;
	this->next = e.next;
	this->prev = e.prev;

	return *this;
}

