#pragma once

template<typename T>
class Comparator
{
public:
	Comparator(){}

	virtual bool compare(T& elem1, T& elem2) const = 0;

	~Comparator(){}
};




