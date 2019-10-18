#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator {

	friend class MultiMap;

private:
	const MultiMap &c;
	node *current;

public:
	MultiMapIterator(const MultiMap& c);
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;
};

