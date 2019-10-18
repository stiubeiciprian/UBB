#include "Matrix.h"
#include "MatrixIterator.h"
#include <assert.h>
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>

void testIterator()
{
	Matrix m{ 10,10 };

	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
			m.modify(i, j, j);

	for (int i = 0; i < 10; i++)
	{
		MatrixIterator it = m.iterator(i);

		assert(it.valid() == true);

		for (int next = 0; next < 9; next++)
		{
			assert(it.valid() == true);
			assert(it.getCurrent() == next);
			it.next();
		}
		assert(it.getCurrent() == 9);

		for (int prev = 0; prev < 9; prev++)
		{
			assert(it.valid() == true);
			assert(it.getCurrent() == 9-prev);
			it.previous();
		}
		assert(it.getCurrent() == 0);
	}	
	

	Matrix m2{ 2,2 };

	try {
		MatrixIterator it2 = m2.iterator(6);
		assert(false);
	}
	catch(std::exception&)
	{
		assert(true);
	}
	
}


int main()
{
	testAll();
	testAllExtended();
	testIterator();

	return 0;
}