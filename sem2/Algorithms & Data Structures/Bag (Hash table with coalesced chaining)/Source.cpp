#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>
int main()
{
	
	testAll();
	std::cout << "Short tests passed\n";
	testAllExtended();
	
	std::cout << "Done";
	return 0;
}