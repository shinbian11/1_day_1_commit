#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode
{
	int data;
	struct TreeNode* left;
	struct TreeNode* right;

}TreeNode;

TreeNode* root = NULL;

TreeNode* Insert(TreeNode* root, int data)
{
	if (root == NULL)
	{
		TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
		node->data = data;
		node->left = NULL;
		node->right = NULL;
		return node;
	}
	else
	{
		if (root->data > data)
			root->left = Insert(root->left, data);
		else
			root->right = Insert(root->right, data);
	}
	return root;
}

void PrintAll(TreeNode* root)
{
	if (root == NULL)
		return;

	//중위 순위(left->root->right)
	PrintAll(root->left);
	printf("%d ", root->data);
	PrintAll(root->right);
}

TreeNode* findMinNode(TreeNode* root)
{
	TreeNode* tmp = root;
	while (tmp->left != NULL)
		tmp = tmp->left;
	return tmp;
}

TreeNode* Delete(TreeNode* root, int data)
{
	TreeNode* tNode = NULL;
	if (root == NULL)
		return NULL;

	if (root->data > data)
		root->left = Delete(root->left, data);
	else if (root->data < data)
		root->right = Delete(root->right, data);
	else
	{
		if (root->right != NULL && root->left != NULL)
		{
			tNode = findMinNode(root->right);
			root->data = tNode->data;
			root->right = Delete(root->right, tNode->data);
		}
		else
		{
			tNode = (root->left == NULL) ? root->right : root->left;
			free(root);
			return tNode;
		}
	}

	return root;
}

TreeNode* Search(TreeNode* root, int data)
{
	if (root == NULL)
		return NULL;

	if (root->data == data)
		return root;
	else if (root->data > data)
		return Search(root->left, data);
	else
		return Search(root->right, data);
}

int main()
{
	root = Insert(root, 7);
	root = Insert(root, 1);
	root = Insert(root, 2);
	root = Insert(root, 6);
	root = Insert(root, 3);
	root = Insert(root, 8);
	root = Delete(root, 2);
	PrintAll(root);
}