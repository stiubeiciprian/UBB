#pragma once
#include "Movie.h"

class ValidatorMovie
{
	std::string err = "";

public:
	ValidatorMovie();

	void validate(Movie);

	~ValidatorMovie();
};

