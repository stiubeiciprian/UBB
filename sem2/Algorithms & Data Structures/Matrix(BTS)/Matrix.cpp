#include "Matrix.h"
#include "MatrixIterator.h"
#include <exception>
#include <iostream>

TreeNode * Matrix::initNode(int i, int j, TElem e)
{
	// theta(1)
	TreeNode* node = new TreeNode;

	node->data.line = i;
	node->data.column = j;
	node->data.value = e;

	node->right = nullptr;
	node->left = nullptr;

	return node;
}

TreeNode* Matrix::insertNode(TreeNode ** node, int i, int j, TElem e)
{
	// O(n)
	if ((*node) == nullptr)
		(*node) = initNode(i, j, e);
	else if ((*node)->data.line < i)
		(*node)->right = insertNode(&(*node)->right, i, j, e);
	else if ((*node)->data.line == i && (*node)->data.column < j)
		(*node)->right = insertNode(&(*node)->right, i, j, e);
	else
		(*node)->left = insertNode(&(*node)->left, i, j, e);

	return (*node);
}

/*
void Matrix::insertNode(int i, int j, TElem e)
{
	TreeNode* currentNode = root, *parent = root;

	if (root == nullptr)
	{
		root = initNode(i, j, e);
		return;
	}

	while (currentNode != nullptr)
	{
		parent = currentNode;

		if (currentNode->data.line < i)
			currentNode = currentNode->right;
		else if (currentNode->data.line == i && currentNode->data.column < j)
			currentNode = currentNode->right;
		else currentNode = currentNode->left;
	}

	currentNode = initNode(i, j, e);
	if (parent->data.line < i)
		parent->right = currentNode;
	else if (parent->data.line == i && currentNode->data.column < j)
		parent->right = currentNode;
	else 	parent->left = currentNode;


}
*/
TreeNode * Matrix::searchNode(TreeNode * node, int i, int j) const
{
	//O(n)

	if (node == nullptr)
		return nullptr;
	else
	if (node->data.line == i && node->data.column == j)
		return node;
	else
	if (node->data.line < i)
		return searchNode(node->right, i, j);
	else
	if (node->data.line == i && node->data.column < j)
		return searchNode(node->right, i, j);
	else
	return searchNode(node->left, i, j);
}

void Matrix::deleteNode(TreeNode * node)
{
	// O(n)
	if (node == nullptr)
		return;
	if (node->left == nullptr && node->right == nullptr) {
		delete node;
		return;
	}

	if (node->left != nullptr)
		deleteNode(node->left);
	if (node->right != nullptr)
		deleteNode(node->right);
	delete node;
}



Matrix::Matrix(int nrLines, int nrCols)
{
	//theta(1)
	this->lines = nrLines;
	this->cols = nrCols;

	root = nullptr;
}

int Matrix::nrLines() const
{
	//theta(1)
	return lines;
}

int Matrix::nrColumns() const
{
	//theta(1)
	return cols;
}

TElem Matrix::element(int i, int j) const
{
	//O(n) - search
	if (i < 0 || i >= lines || j < 0 || j >= cols)
		throw std::exception();

	TreeNode* node = searchNode(root, i, j);

	if (node == nullptr)
		return 0;

	return node->data.value;
}

TElem Matrix::modify(int i, int j, TElem e)
{
	//O(n) - search / insert
	if (i < 0 || i >= lines || j < 0 || j >= cols)
		throw std::exception();

	TreeNode* node = searchNode(root, i, j);

	if (node == nullptr)
	{
		insertNode(&root,i, j, e);
		return 0;
	}

	TElem old_value = node->data.value;
	node->data.value = e;
	return old_value;
}

MatrixIterator Matrix::iterator(int line) const
{
	return MatrixIterator(*this, line);
}

Matrix::~Matrix()
{
	deleteNode(root);
}
