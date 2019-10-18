#include "UserInterface.h"


void UserInterface::printMainMenu() {

	std::string str = "\n";

	str += "Menu\n";
	str += "1. Administrator mode\n";
	str += "2. User mode \n";
	str += "0. Exit\n";

	std::cout << str;
}

void UserInterface::printUpdateMenu() {

	std::string str = "\n";

	str += "1. Update genre\n";
	str += "2. Update year \n";
	str += "3. Update likes\n";
	str += "4. Update trailer url\n";
	str += "0. Cancel\n";

	std::cout << str;
}

void UserInterface::printAdminMenu() {

	std::string str = "\n";

	str += "Menu\n";
	str += "1. Add movie\n";
	str += "2. Update movie genre/year/likes/trailer \n";
	str += "3. Remove movie <title>\n";
	str += "4. Print all movies\n";
	str += "0. Exit\n";

	std::cout << str;
}

void UserInterface::printUserMenu() {

	std::string str = "\n";

	str += "Menu\n";
	str += "1. Search movie by genre\n";
	str += "2. Delete movie from watchlist \n";
	str += "3. See watchlist\n";
	str += "4. Display watchlist\n";
	str += "0. Exit\n";

	std::cout << str;
}

void UserInterface::printWatchlistMenu() {

	std::string str = "\n";

	str += "Menu\n";
	str += "1. Add movie to watchlist\n";
	str += "2. Next movie \n";
	str += "0. Exit\n";

	std::cout << str;
}

void UserInterface::UI_init() {
	
	std::string title = "title";
	std::string genre = "genre";
	std::string url = "url";

	for (int i = 0; i <= 9; i++)
		this->cont.add(title + std::to_string(i), genre + std::to_string(i), 2000 + i, 100 + i, url + std::to_string(i));

}


bool UserInterface::selectMovies() {
	

	std::string genre;

	std::cout << "Genre: ";
	std::getline(std::cin, genre);

	Repository movies = this->cont.selectMovies(genre);

	if (movies.getSize() == 0)
		return false;

	std::string command="";
	int i = 0;
	while(command != "add"){
		
		if (i == movies.getSize())
			i = 0;

		std::cout << movies.getElemStr(i) + "\n";
		movies.getElem(i).play();

		std::cout << "( add / next )>>";
		std::getline(std::cin, command);
		
		if (command == "add") {
			this->cont.addToWatchlist(movies.getElem(i));
			return true;
		}

		else if (command == "next") {
			i++;
		}
		else std::cout << "Invalid command!\n";

	}


	return true;
}

bool UserInterface::deleteMovie() {
	
	std::string title;

	std::cout << "Enter title: ";
	std::getline(std::cin, title);

	bool status = this->cont.removeFromWatchlist(title);

	if (status) {
		std::string response;
		std::cout << "Did you like the movie?\nPress y if yes or any other key if you did not.\n";
		std::cout << ">> ";
		std::getline(std::cin, response);

		if (response == "y")
			this->cont.incLikes(title);
	}
	
	return status;
}

void UserInterface::runApp() {

	std::string commandTxt;
	int command = 0;

	while (true) {
		this->printMainMenu();

		std::cout << ">>";
		std::getline(std::cin, commandTxt);
		command = std::stoi(commandTxt);

		if (command == 1)
			runAdmin();
		else if (command == 2)
			runUser();
		else if (command == 0)
			return;

		else std::cout << "Invalid command!\n";
	}
}

void UserInterface::runUser() {

	

	while (true) {

		this->printUserMenu();

		std::string commandTxt;
		int command = 0;

		std::cout << ">>";
		std::getline(std::cin, commandTxt);
		command = std::stoi(commandTxt);

		// Search by genre
		if (command == 1) {

			if (this->selectMovies() == false)
				std::cout << "No movies found. Try another genre.\n";
		}
		// Delete movie from watchlist
		else if (command == 2)
		{
			if (this->deleteMovie() == false)
				std::cout << "Movie was not found in the watchlist.\n";
		}
		// See watchlist
		else if (command == 3)
			std::cout << this->cont.getWatchlist();

		// Display watchlist
		else if (command == 4)
			this->cont.displayWatchlist();
		// Exit
		else if (command == 0)
			return;
		else std::cout << "Invalid command!\n";

	}
}

void UserInterface::runAdmin() {

	

	while (true) {

		try
		{
			this->printAdminMenu();

			std::string commandTxt;
			int command = 0;

			std::cout << ">>";
			std::getline(std::cin, commandTxt);
			command = std::stoi(commandTxt);

			// Add
			if (command == 1)
			{
				std::string title, genre, trailer;
				std::string year, likes;

				std::cout << "Enter title: ";
				std::getline(std::cin, title);

				std::cout << "Genre: ";
				std::getline(std::cin, genre);

				std::cout << "Year: ";
				std::getline(std::cin, year);


				std::cout << "Likes: ";
				std::getline(std::cin, likes);


				std::cout << "Trailer url: ";
				std::getline(std::cin, trailer);

				this->cont.add(title, genre, std::stoi(year), std::stoi(likes), trailer);
			}

			// Update
			else if (command == 2)
			{
				this->printUpdateMenu();
				int update_command = 0;
				std::string update_commandTxt;

				std::cout << ">>";

				std::getline(std::cin, update_commandTxt);
				command = std::stoi(update_commandTxt);

				if (update_command == 1)
				{
					std::string title, genre;

					std::cout << "Enter title: ";
					std::getline(std::cin, title);

					std::cout << "New genre: ";
					std::getline(std::cin, genre);


					this->cont.updateGenre(title, genre);
				}

				else if (update_command == 2)
				{
					std::string title;
					std::string year;

					std::cout << "Enter title: ";
					std::getline(std::cin, title);

					std::cout << "New year: ";
					std::getline(std::cin, year);

					this->cont.updateYear(title, std::stoi(year));
				}

				else if (update_command == 3)
				{
					std::string title, likes;

					std::cout << "Enter title: ";
					std::getline(std::cin, title);

					std::cout << "New likes number: ";
					std::getline(std::cin, likes);


					this->cont.updateLikes(title, std::stoi(likes));
				}

				else if (update_command == 4)
				{
					std::string title, trailer;

					std::cout << "Enter title: ";
					std::getline(std::cin, title);

					std::cout << "New trailer url: ";
					std::getline(std::cin, trailer);

					this->cont.updateTrailer(title, trailer);

				}

				else if (update_command == 0)
				{
					std::cout << "Update canceled.\n";
				}

				else std::cout << "Invalid input!\n";

			}

			// Remove
			else if (command == 3)
			{
				std::string title;

				std::cout << "Enter title: ";
				std::getline(std::cin, title);

				this->cont.remove(title);
			}

			// Print all
			else if (command == 4)
			{
				std::cout << this->cont.getAllString();
			}

			


			// Exit
			else if (command == 0) {
				return;
			}

			else std::cout << "Invalid command!\n";
		}


		catch (std::runtime_error& e) {
			std::cout << e.what();
		}

		catch (std::exception&) {
			std::cout << "Invalid input!\n";
		}
	}
}