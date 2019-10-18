#include "MultiMapIterator.h"
#include "MultiMapKeyIterator.h"
#include "MultiMap.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <assert.h>
#include <iostream>

void testKeyIterator() {
	MultiMap m;
	m.add(1, 100);
	m.add(2, 200);
	m.add(3, 300);
	m.add(1, 500);
	m.add(2, 600);
	m.add(4, 800);
	m.add(29, 600);
	m.add(41, 800);

	MultiMapKeyIterator im = m.keyIterator();
	assert(im.valid() == true);
	while (im.valid()) {
		std::cout << im.getCurrent() << "\n";
		im.next();
	}

	assert(im.valid() == false);
	im.first();
	assert(im.valid() == true);
}

int main() {

	testAll();
	testAllExtended();


	testKeyIterator();
	system("pause");
	
	return 0;
}