#pragma once
#include "MultiMap.h"
#include <set>

class MultiMap;

class MultiMapKeyIterator {

	friend class MultiMap;

private:
	const MultiMap &c;
	node *current;
	std::set<TKey> iteratedKeys;

public:
	MultiMapKeyIterator(const MultiMap& c);
	void first();
	void next();
	bool valid() const;
	TKey getCurrent() const;
};


