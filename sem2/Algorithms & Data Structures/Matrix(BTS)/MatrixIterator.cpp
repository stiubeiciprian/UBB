#include "MatrixIterator.h"
#include <exception>



MatrixIterator::MatrixIterator(const Matrix & c, int line) : c{ c }, line{ line } 
{
	if (line < 0 || line >= c.nrLines() || col < 0 || col >= c.nrColumns())
		throw std::exception("Invalid iterator.");
}

void MatrixIterator::first()
{
	// theta(1)
	col = 0;
}

void MatrixIterator::next()
{
	// theta(1)
	col++;

	if (valid() == false)
		throw std::exception("Invalid iterator.");
}

void MatrixIterator::previous()
{
	// theta(1)
	col--;

	if (valid() == false)
		throw std::exception("Invalid iterator.");
}

/*

	function valid(iterator):
	
		if iterator.line < 0 or iterator.line >= nrLines(iterator.matrix) or iterator.column < 0 or iterator.column >= nrColumns(iterator.matrix) then
			valid <- false
		else
			valid <-true
		end-if

	end-function

*/
bool MatrixIterator::valid() const
{
	// theta(1)
	if (line < 0 || line >= c.nrLines() || col < 0 || col >= c.nrColumns())
		return false;
	return true;
}

TElem MatrixIterator::getCurrent() const
{
	// O(n) - element
	if (valid() == false)
		throw std::exception("Invalid iterator.");
	return c.element(line, col);
}
