#pragma once
#include <utility>

typedef int TElem;

typedef int TPriority;

typedef std::pair<TElem, TPriority> Element;

class NodeDLLA
{
	friend class PriorityQueue;

private:
	Element data;
	int next, prev;

public:
	NodeDLLA() {};
	NodeDLLA(Element e, int next, int prev);

	NodeDLLA& operator=(const NodeDLLA& e);

	~NodeDLLA() {};
};

