#include "../Jx_test.h"

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

//time:0 ms	//memory:10.3 MB	//rank:100%
ListNode* getKthFromEnd(ListNode* head, int k)
{
	ListNode* temp = head;
	for (int i = 0; i < k; i++)
	{
		temp = temp->next;
	}
	while (temp->next)
	{
		temp = temp->next;
		head = head->next;
	}
	return head->next;
}
