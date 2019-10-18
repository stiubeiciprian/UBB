#pragma once
#include "repository.h"

typedef struct {
	Repository* repo;
}Controller;

Controller* createController();
void destroyController(Controller *cont);

int cont_add(char[], char[], int, int, Controller*);
int cont_remove(char[], Controller*);
int cont_update_type(char[], char[], Controller*);
int cont_update_price(char[], int, Controller*);
int cont_update_surface(char[], int, Controller*);
void cont_init(Controller*);
Repository* cont_getAll(Controller*);

void cont_sort(Repository*);