#include "ValidatorMovie.h"



ValidatorMovie::ValidatorMovie()
{
}


void ValidatorMovie::validate(Movie m) {

	if (m.getTitle() == "")
		this->err += "\tTitle cannot be empty!\n";
	
	if(m.getGenre() == "")
		this->err += "\tGenre cannot be empty!\n";

	if (m.getTrailer() == "")
		this->err += "\tTrailer cannot be empty!\n";


	if (this->err != "")
		throw std::runtime_error("Error:\n" + this->err);
}


ValidatorMovie::~ValidatorMovie()
{
}
