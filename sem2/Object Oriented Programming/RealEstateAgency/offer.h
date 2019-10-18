#pragma once

typedef struct {
	char *type;
	char *address;
	int surface;
	int price;
}Offer;


Offer* createOffer(char* type, char* address, int surface, int price);
void destroyOffer(Offer*);

char* getOfferAddress(Offer*);
char* getOfferType(Offer*);
int getOfferSurface(Offer*);
int getOfferPrice(Offer*);

void setOfferAddress(char*, Offer*);
void setOfferType(char*, Offer*);
void setOfferSurface(int, Offer*);
void setOfferPrice(int, Offer*);

char* offerToString(Offer*);