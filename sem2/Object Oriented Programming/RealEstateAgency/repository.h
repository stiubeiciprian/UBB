#pragma once
#include "offer.h"

typedef Offer* TElem;

typedef struct {
	TElem *elems;
	int length;
	int capacity;
}Repository;

Repository* createRepository(int);
void destroyRepository(Repository*);
void resizeRepository(Repository*);

int repo_add(TElem, Repository*);
int repo_remove(TElem, Repository*);
int repo_update(TElem, Repository*);
int repo_search(TElem, Repository*);
TElem* repo_getElem(char[], Repository*);

Repository* repo_getAll(Repository* pRepo);