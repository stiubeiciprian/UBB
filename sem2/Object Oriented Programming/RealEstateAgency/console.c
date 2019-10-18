#include "console.h"
#include "controller.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

UI* createUI() {

	UI* ui = (UI*)malloc(sizeof(UI));

	ui->cont = createController();

	return ui;
}

void destroyUI(UI* ui) {

	if (ui == NULL)
		return;

	destroyController(ui->cont);
	free(ui);
}

void printMenu() {
	printf("Menu:\n");
	printf("add <type> <address> <surface> <price> - add offer\n");
	printf("update type/surface/price <address> - update the type/surface/price of an offer\n");
	printf("remove <address> - remove offer\n");
	printf("sort price <string> - sort all offers containing string in their address by price\n");
	printf("surface <int> - sort all offers with a given surface by price\n");
	printf("larger <int> - show all offers with surface larger than int\n");
	printf("exit - quit program\n");
}

void run(UI* app) {

	char inputText[500];
	char params[10][50];
	int wordCount = 0;
	char *p;

	cont_init(app->cont);

	while (1) {


		printf(">>");
		fgets(inputText, 500, stdin);

		wordCount = 0;
		p = strtok(inputText, " \n");
		while (p != NULL)
		{
			strcpy(params[wordCount], p);
			wordCount++;
			p = strtok(NULL, " \n");
		}


		// add <type> <address> <surface> <price>
		if (wordCount == 5 && strcmp(params[0], "add") == 0) {
	
			if (cont_add(params[2], params[1], atoi(params[4]), atoi(params[3]), app->cont) == -1)
				printf("Element already exists!\n");

		} else

		// remove <address>
		if (wordCount == 2 && strcmp(params[0], "remove") == 0) {
			
			if (cont_remove(params[1], app->cont) == -1)
				printf("Element does not exist!\n");

		} else
		
		// update type/surface/price <address>
		if (wordCount == 4 && strcmp(params[0], "update") == 0) {
			
			// update type <address> <new_type>
			if (strcmp(params[1], "type") == 0) {
				if (cont_update_type(params[2], params[3], app->cont) == -1)
					printf("Element does not exist!\n");

			} else

			// update surface <address> <new_surface>
			if (strcmp(params[1], "surface") == 0) {
				if (cont_update_surface(params[2], atoi(params[3]), app->cont) == -1)
					printf("Element does not exist!\n");

			} else

			// update price <address> <new_price>
			if (strcmp(params[1], "price") == 0) {
				if (cont_update_price(params[2], atoi(params[3]), app->cont) == -1)
					printf("Element does not exist!\n");

			}

		} else

		// sort price <string>
		if (wordCount == 3 && strcmp(params[0], "sort") == 0 && strcmp(params[1], "price") == 0) {
			

			Repository *repo = cont_getAll(app->cont);

			cont_sort(repo);
			
			printf("Elements sorted by price:\n");
			for (int i = 0; i < repo->length; i++)
				if (strstr(getOfferAddress(repo->elems[i]), params[2]) != NULL) {
					char *str = offerToString(repo->elems[i]);
					printf("%s", str);
					free(str);
					str = NULL;
				}
			free(repo->elems);
			free(repo);

		} else
		
		// sort price 
		if (wordCount == 2 && strcmp(params[0], "sort") == 0 && strcmp(params[1], "price") == 0) {


			Repository *repo = cont_getAll(app->cont);

			cont_sort(repo);

			printf("Elements sorted by price:\n");
			for (int i = 0; i < repo->length; i++) {
				char *str = offerToString(repo->elems[i]);
				printf("%s", str);
				free(str);
				str = NULL;
			}
			free(repo->elems);
			free(repo);

		}
		else

		// surface <int>
		if (wordCount == 2 && strcmp(params[0], "surface") == 0) {

			int surface = atoi(params[1]);

			Repository *repo = cont_getAll(app->cont);

			cont_sort(repo);

			printf("Elements sorted by price:\n");
			for (int i = 0; i < repo->length; i++)
				if (getOfferSurface(repo->elems[i]) == surface) {
					char* str = offerToString(repo->elems[i]);
					printf("%s", str);
					free(str);
					str = NULL;
				}
			
			free(repo->elems);
			free(repo);

		} else

		// larger <int>
		if (wordCount == 2 && strcmp(params[0], "larger") == 0) {
			
			int num = atoi(params[1]);

			Repository *repo = cont_getAll(app->cont);

			printf("Elements:\n");
			for (int i = 0; i < repo->length; i++)
				if(getOfferSurface(repo->elems[i]) >= num){
					char* str = offerToString(repo->elems[i]);
					printf("%s", str);
					free(str);
					str = NULL;
				}
			free(repo->elems);
			free(repo);

		} else

		// print
		if (wordCount == 1 && strcmp(params[0], "print") == 0) {

			Repository *repo = cont_getAll(app->cont);

			printf("Elements:\n");
			for (int i = 0; i < repo->length; i++){
				char* str = offerToString(repo->elems[i]);
				printf("%s", str);
				free(str);
				str = NULL;
			}

			free(repo->elems);
			free(repo);

		}
			else
		
		// help
		if (wordCount == 1 && strcmp(params[0], "help") == 0) {
			printMenu();
		} else

		// exit
		if (wordCount == 1 && strcmp(params[0], "exit") == 0) {
			destroyUI(app);
			return;
		}
		else {
			printf("%s", params[0]);
			printf("Invalid command!\n");
		}
	}
}