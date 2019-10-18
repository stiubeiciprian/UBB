#include "controller.h"
#include <stdlib.h>
#include <string.h>

Controller* createController() {
	/*
		Create controller.
	*/

	Controller* cont = (Controller*)malloc(sizeof(Controller));
	cont->repo = createRepository(50);

	return cont;
}

void destroyController(Controller* cont) {
	/*
		Destroy controller.
	*/

	if (cont == NULL)
		return;

	destroyRepository(cont->repo);
	free(cont);
}

int cont_add(char address[], char type[], int price, int surface, Controller* cont) {
	/*
		Add element to repository.
		Input:	address - address (string)
				type - type (string)
				price - price (int)
				surface - surface (int)
				cont - controller (pointer)
		Output:	 0 if add was successful
				-1 if element already exists
	*/
	
	Offer* new_offer = createOffer(type, address, surface, price);
	int status = repo_add(new_offer, cont->repo);

	return status;
}

int cont_remove(char address[], Controller* cont) {
	/*
		Remove element from repository.
		Input: address - address (string)
		Output:  0 if remove was successful
				-1 if element does not exist
	*/

	Offer* offerToRemove = createOffer("", address, 0, 0);

	int status = repo_remove(offerToRemove, cont->repo);

	destroyOffer(offerToRemove);
	offerToRemove = NULL;

	return status;
}

int cont_update_type(char address[], char type[], Controller* cont) {
	/*
		Update an element from the repository.
		Input:	address - address (string)
				type - type (string)
				cont - controller (pointer)
		Output:	 0 if update was successful
				-1 if element does not exist
	*/

	Offer* offerToUpdate = repo_getElem(address, cont->repo);
	setOfferType(type, offerToUpdate);

	int status = repo_update(offerToUpdate, cont->repo);

	destroyOffer(offerToUpdate);
	offerToUpdate = NULL;

	return status;
}

int cont_update_price(char address[], int price, Controller* cont) {
	/*
		Update an element from the repository.
		Input:	address - address (string)
				price - price (int)
				cont - controller (pointer)
		Output:	 0 if update was successful
				-1 if element does not exist
	*/

	Offer* offerToUpdate = repo_getElem(address, cont->repo);
	setOfferPrice(price, offerToUpdate);

	int status = repo_update(offerToUpdate, cont->repo);

	destroyOffer(offerToUpdate);
	offerToUpdate = NULL;

	return status;
}

int cont_update_surface(char address[], int surface, Controller* cont) {
	/*
		Update an element from the repository.
		Input:	address - address (string)
				surface - surface (int)
				cont - controller (pointer)
		Output:	 0 if update was successful
				-1 if element does not exist
	*/

	Offer* offerToUpdate = repo_getElem(address, cont->repo);
	setOfferSurface(surface, offerToUpdate);

	int status = repo_update(offerToUpdate, cont->repo);

	destroyOffer(offerToUpdate);
	offerToUpdate = NULL;

	return status;
}


void cont_init(Controller* cont) {

	char address[50];
	char type[50];
	int price;
	int surface;

	strcpy(address, "address1");
	strcpy(type, "apartment");
	price = 100;
	surface = 100;
	cont_add(address, type, price, surface, cont);

	
	strcpy(address, "address2");
	strcpy(type, "house");
	price = 206;
	surface = 102;
	cont_add(address, type, price, surface, cont);


	strcpy(address, "address3");
	strcpy(type, "house");
	price = 204;
	surface = 102;
	cont_add(address, type, price, surface, cont);


	strcpy(address, "address4");
	strcpy(type, "house");
	price = 205;
	surface = 103;
	cont_add(address, type, price, surface, cont);
	
	
	strcpy(address, "address5.1");
	strcpy(type, "house");
	price = 234;
	surface = 102;
	cont_add(address, type, price, surface, cont);

	
	strcpy(address, "address6.1");
	strcpy(type, "house");
	price = 613;
	surface = 102;
	cont_add(address, type, price, surface, cont);

	
	strcpy(address, "address7.1");
	strcpy(type, "house");
	price = 344;
	surface = 102;
	cont_add(address, type, price, surface, cont);


	strcpy(address, "address8");
	strcpy(type, "apartment");
	price = 560;
	surface = 102;
	cont_add(address, type, price, surface, cont);

	
	strcpy(address, "address9");
	strcpy(type, "house");
	price = 2000;
	surface = 122;
	cont_add(address, type, price, surface, cont);
	
	strcpy(address, "address10");
	strcpy(type, "house");
	price = 1000;
	surface = 212;
	cont_add(address, type, price, surface, cont);
	
}


Repository* cont_getAll(Controller* cont) {
	
	return repo_getAll(cont->repo);
}

void cont_sort(Repository* repo) {
	
	Offer* aux_offer;

	for(int i= 0; i < repo->length - 1; i++)
		for(int j= i + 1; j < repo->length; j++)
			if (getOfferPrice(repo->elems[i]) > getOfferPrice(repo->elems[j])) {
			
				aux_offer = repo->elems[i];
				repo->elems[i] = repo->elems[j];
				repo->elems[j] = aux_offer;
			}
}