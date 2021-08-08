#include "../Jx_test.h"

//time:0 ms	//memory:18 MB	//rank:100%
int removeDuplicates_Jx001(vector<int>& nums)
{
	if (nums.size()==0)
	{
		return 0;
	}

	int num = 1;
	for (int i = 1; i < nums.size(); i++)
	{
		if (nums[i] != nums[num-1])
		{
			nums[num++] = nums[i];
		}
	}
	return num;
}

