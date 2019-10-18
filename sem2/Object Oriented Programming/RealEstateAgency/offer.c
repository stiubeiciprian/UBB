#include "offer.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

Offer* createOffer(char* type, char* address, int surface, int price) {
	/*
		Create offer with given type, address, surface and price.
		Input:	type - string
				address - string
				surface - int
				price -int
		Output: Offer
	*/

	Offer *pOffer = (Offer*)malloc(sizeof(Offer));

	pOffer->type = (char*)malloc(sizeof(char*) * (strlen(type) + 1));
	strcpy(pOffer->type, type);

	pOffer->address = (char*)malloc(sizeof(char*) * (strlen(address) + 1));
	strcpy(pOffer->address, address);

	pOffer->surface = surface;
	pOffer->price = price;

	return pOffer;
}

void destroyOffer(Offer* pOffer) {
	/*
		Destroy an offer.
		Input: pOffer - pointer to the offer to be destroyed
		Output: -
		Postcond: After destroyOffer is called pOffer must be set to NULL (to avoid dangling pointers).
	*/

	if (pOffer == NULL)
		return;

	free(pOffer->address);
	pOffer->address = NULL;

	free(pOffer->type);
	pOffer->type = NULL;

	free(pOffer);
	pOffer = NULL;
}

/* Getters */

char* getOfferAddress(Offer* pOffer) {
	return pOffer->address;
}

char* getOfferType(Offer* pOffer) {

	return pOffer->type;

}

int getOfferSurface(Offer* pOffer) {
	return pOffer->surface;
}

int getOfferPrice(Offer* pOffer) {
	return pOffer->price;
}


/* Setters */

void setOfferAddress(char* address, Offer* pOffer) {
	strcpy(pOffer->address, address);
}

void setOfferType(char* type, Offer* pOffer) {
	strcpy(pOffer->type, type);
}
void setOfferSurface(int surface, Offer* pOffer) {
	pOffer->surface = surface;
}

void setOfferPrice(int price, Offer* pOffer) {
	pOffer->price = price;
}


char* offerToString(Offer* pOffer) {

	char* str =(char*)malloc(sizeof(char) * 100);

	sprintf(str, "Address: %s; Type: %s; Surface: %d; Price: %d\n", getOfferAddress(pOffer), getOfferType(pOffer), getOfferSurface(pOffer), getOfferPrice(pOffer));

	return str;
}