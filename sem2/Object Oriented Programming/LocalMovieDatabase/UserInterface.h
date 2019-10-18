#pragma once
#include "Controller.h"
#include <iostream>



class UserInterface
{
	Controller &cont;

public:
	UserInterface(Controller &c) : cont{ c } {}

	void printMainMenu();
	void printUpdateMenu();
	void printAdminMenu();
	void printUserMenu();
	void printWatchlistMenu();
	void UI_init();
	void runAdmin();
	void runApp();
	void runUser();

	bool selectMovies();
	bool deleteMovie();
};

