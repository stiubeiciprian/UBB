#include <assert.h>
#include <string.h>
#include "controller.h"
#include "repository.h"
#include "offer.h"
#include "test.h"

void testCont() {

	Controller* cont = createController();

	// Test add
	assert(cont_add("address1", "type1", 100, 100, cont) == 0);
	assert(cont_add("address2", "type2", 200, 200, cont) == 0);
	assert(cont_add("address3", "type2", 2020, 2020, cont) == 0);
	assert(cont_add("address2", "type2", 312, 123, cont) == -1);

	// Test remove
	assert(cont_remove("address2", cont) == 0);
	assert(cont_remove("address101", cont) == -1);

	// Test update

		// type
		assert(cont_update_type("address1", "new_type", cont) == 0);
		assert(cont_update_type("address123", "new_type", cont) == -1);
		// surface
		assert(cont_update_surface("address1", 101, cont) == 0);
		assert(cont_update_surface("address123", 101, cont) == -1);
		// price
		assert(cont_update_price("address1", 101, cont) == 0);
		assert(cont_update_price("address123", 101, cont) == -1);

	destroyController(cont);
	cont = NULL;
}

void testRepo() {
	Repository* repo = createRepository(1);

	Offer* offer = createOffer("apartment", "eroilor", 100, 400);
	Offer* offer2 = createOffer("apartment2", "revolutiei", 102, 234);
	//char* offerStr = offerToString(offer);


	// Test add
	assert(repo_add(offer, repo) == 0);	
	assert(repo_add(offer, repo) == -1);	// offer was already added to repo

	assert(repo_add(offer2, repo) == 0);
	assert(repo_add(offer2, repo) == -1);	// offer2 was already added to repo
	
	//Test remove
	assert(repo_remove(offer, repo) == 0);	
	assert(repo_remove(offer, repo) == -1);	//offer was removed from repo

	// Test search
	assert(repo_search(offer2, repo) != -1); // offer2 exists in repo
	assert(repo_search(offer, repo) == -1);	// offer was removed from repo

	// Test update
	assert(repo_update(offer, repo) == -1);
	setOfferAddress(getOfferAddress(offer2), offer);
	assert(repo_update(offer, repo) == 0);
	
	destroyRepository(repo);
}

void testOffer() {

	char type[] = "apartment";
	char address[] = "eroilor";
	int surface = 100;
	int price = 400;

	Offer* offer = createOffer(type, address, surface, price);

	assert(strcmp(type, getOfferType(offer)) == 0);
	assert(strcmp(address, getOfferAddress(offer)) == 0);
	assert(surface == getOfferSurface(offer));
	assert(price == getOfferPrice(offer));

	destroyOffer(offer);

}



void testAll() {

	testOffer();
	testRepo();
	testCont();
}

