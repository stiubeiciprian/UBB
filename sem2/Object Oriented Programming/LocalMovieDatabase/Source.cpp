#include<iostream>
#include "UserInterface.h"
#include "FileRepository.h"
#include <crtdbg.h>



int main() {
	
	{

		Watchlist * w = new WatchlistCSV;
		Repository r = Repository();

			
		std::string type;
		std::cout << "Select watchlist type:\n \t-csv\n \t-html\n";
		std::getline(std::cin, type);


		if (type == "csv")
		{
			delete w;
			w = new WatchlistCSV;
		}
		else if (type == "html")
		{
			delete w;
			w = new WatchlistHTML;
		}
		else std::cout << "Invalid file type for watchlist!\n";

		if (w == nullptr)
			return 1;

		Controller cont = Controller(r, *w);
		UserInterface ui = UserInterface(cont);

		ui.UI_init();
		ui.runApp();
		
		delete w;
	}

	

	_CrtDumpMemoryLeaks();

	return 0;
}