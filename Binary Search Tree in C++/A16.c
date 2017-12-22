// Binary Search Tree

#include<iostream>
using namespace std;

class BstNode
{
public:
	int data;
	BstNode* left;
	BstNode* right;
};

BstNode* GetNewNode(int data)
{
	BstNode* newNode = new BstNode();
	newNode->data = data;
	newNode->left = newNode->right = NULL;
	return newNode;
}

BstNode* insert(BstNode* head, int data)
{
	if(head == NULL)
	{
	    head = GetNewNode(data);
	}
	else if(data <= head->data)
    {
		head->left = insert(head->left, data);
    }

	else
    {
		head->right = insert(head->right, data);
	}
	return head;
}

void preorder(BstNode * head)
{
    if (head == NULL) return;

    cout<< head->data;
         preorder(head-> left);
         preorder(head-> right);
}

void inorder( BstNode* head)
{
    if (head == NULL) return;

    inorder(head->left);
    cout <<head-> data;
    inorder(head-> right);

}
void postorder(BstNode* head)
{
    if (head == NULL) return;

    postorder(head->left);
    postorder(head-> right);
    cout <<head-> data;
}

int main() {
	BstNode* head = NULL;
	head = insert(head, 6);
	head = insert(head, 4);
	head = insert(head, 7);
	head = insert(head, 10);

	cout<<"Preorder:"<<endl;
	preorder(head);
	cout<<"\n"<<endl;

	cout<<"inorder:"<<endl;
	inorder(head);
	cout<<"\n"<<endl;

	cout<<"post_order:" << endl;
	postorder(head);
	cout<<"\n"<<endl;
    return 0;
}
