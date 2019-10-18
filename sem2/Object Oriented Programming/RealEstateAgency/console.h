#pragma once
#include "controller.h"

typedef struct {
	Controller* cont;
}UI;

UI* createUI();

void destroyUI(UI*);

void printMenu();

void run(UI*);