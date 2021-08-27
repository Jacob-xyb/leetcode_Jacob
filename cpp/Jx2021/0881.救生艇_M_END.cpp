#include "../Jx_test.h"

//�������
//����참��˼·��ȫһ��
//time:60 ms	//memory:41 MB	//rank:97.81%
int numRescueBoats_Jx001(vector<int>& people, int limit)
{
	int n = people.size();
	sort(people.begin(), people.end());
	int res = 0;
	int l = 0, r = n - 1;
	while (l <= r)
	{	
		if (people[l] + people[r] <= limit) l++;
		res++;
		r--;
	}
	return res;
}
