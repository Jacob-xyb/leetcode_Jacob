#include "../Jx_test.h"

//time:0 ms	//memory:9.4 MB	//rank:100%
int searchInsert_Jx001(vector<int>& nums, int target)
{
	int left = 0;
	//int right = nums.size() - 1;	//还有可能在最后一个数后面插入，因此不能size()-1
	int right = nums.size();
	while (left!=right)
	{
		if (nums[(right+left)/2] < target)
		{
			left = (right + left) / 2 + 1;
		}
		else
		{
			right = (right + left) / 2;
		}
	}
	return left;
}