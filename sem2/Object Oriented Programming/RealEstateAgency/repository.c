#include "repository.h"
#include <stdlib.h>
#include <string.h>

Repository* createRepository(int capacity) {
	/*
		Create repository.
	*/
	
	Repository* repo = (Repository*)malloc(sizeof(Repository));

	repo->length = 0;
	repo->capacity = capacity;

	repo->elems = (TElem*)malloc(sizeof(TElem) * capacity);

	return repo;
}

void destroyRepository(Repository* pRepo) {
	/*
		Destroy repository.
	*/

	if (pRepo == NULL)
		return;
	
	for (int i = 0; i < pRepo->length; i++)
		destroyOffer(pRepo->elems[i]);
	
	free(pRepo->elems);
	pRepo->elems = NULL;

	free(pRepo);
	pRepo = NULL;
}

void resizeRepository(Repository* pRepo) {
	/*
		Resize repository.
	*/

	pRepo->capacity *= 2;

	TElem* aux = (TElem*)realloc(pRepo->elems, pRepo->capacity * sizeof(TElem));

	pRepo->elems = aux;
}

int repo_add(TElem elem, Repository* pRepo) {
	/*
		Add an element to the repository.
		Input:	elem - element to be added (TElem)
				pRepo - repository (pointer)
		Output: 0 if element was added
				-1 if element already exists
	*/

	if (repo_search(elem, pRepo) != -1)
		return -1;

	if (pRepo->length == pRepo->capacity)
		resizeRepository(pRepo);

	pRepo->elems[pRepo->length] = elem;
	pRepo->length++;

	return 0;
}

int repo_remove(TElem elem, Repository* pRepo) {
	/*
		Remove an element from the repository.
		Input:	elem - element to be removed (TElem)
				pRepo - repository (pointer)
		Output: 0 if element was removed
				-1 if element does not exist
	*/

	if (repo_search(elem, pRepo) == -1)
		return -1;
	
	for (int i = 0; i < pRepo->length; i++) {
		if (strcmp(elem->address, getOfferAddress(pRepo->elems[i])) == 0) {

			pRepo->length--;
			
			for (int j = pRepo->length-1; j >= i; j--) {
				pRepo->elems[j] = pRepo->elems[j + 1];
			}

			return 0;
		}
	}
	
	return -1;
}

int repo_update(TElem elem, Repository* pRepo) {
	/*
		Update an element from the repository.
		Input:	elem - element to be removed (TElem)
				pRepo - repository (pointer)
		Output: 0 if element was updated
				-1 if element did not exist
	*/

	int position = repo_search(elem, pRepo);

	if (position == -1)
		return -1;
	
	setOfferType(getOfferType(elem), pRepo->elems[position]);
	setOfferSurface(getOfferSurface(elem), pRepo->elems[position]);
	setOfferPrice(getOfferPrice(elem), pRepo->elems[position]);

	return 0;


}

int repo_search(TElem elem, Repository* pRepo) {
	/*
		Search an element in the repository.
		Input:	elem - element to be searched for
				pRepo - repository
		Output:	position of elem in repo, if found
				-1 if elem does not exist in repo
	*/

	for (int i = 0; i < pRepo->length; i++) {

		if (strcmp(elem->address, getOfferAddress(pRepo->elems[i])) == 0) {
			return i;
		}
	}

	return -1;
}

TElem* repo_getElem(char address[], Repository* pRepo) {
	/*
	Return deep copy of offer with given adderss.
	Input:	address - offer address (string)
			pRepo - repository (pointer)
	Output: offer with empty address - if element was not found
			deep copy of offer - otherwise
	*/
	TElem* offer = createOffer("none", address, 0, 0);

	int index = repo_search(offer, pRepo);

	if (index == -1)
		return offer;

	setOfferType(getOfferType(pRepo->elems[index]), offer);
	setOfferPrice(getOfferPrice(pRepo->elems[index]), offer);
	setOfferSurface(getOfferSurface(pRepo->elems[index]), offer);

	return offer;
}

Repository* repo_getAll(Repository* pRepo) {
	
	Repository* new_repo = createRepository(pRepo->length + 1);

	for (int i = 0; i < pRepo->length; i++) {
		repo_add(pRepo->elems[i], new_repo);
	}

	return new_repo;
}