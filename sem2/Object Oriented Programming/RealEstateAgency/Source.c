#include <stdio.h>
#include <crtdbg.h>
#include <stdlib.h>
#include "offer.h"
#include "repository.h"
#include "console.h"
#include "test.h"
#include <stdio.h>

int main() {
	
	testAll();

	UI* app = createUI();
	
	run(app);
	app = NULL;

	_CrtDumpMemoryLeaks();
	return 0;
}