#include "../Jx_test.h"

//time:16 ms	//memory:19.1 MB	//rank:82.69%
int majorityElement_Jx001(vector<int>& nums)
{
	sort(nums.begin(), nums.end());
	int t = 1;
	for (int i = 0; i < nums.size()-1; i++)
	{
		if (nums[i] == nums[i+1]) 
		{
			t++;
		}
		else
		{
			t = 1;
		}
		if (t > nums.size() / 2)
		{
			return nums[i];
		}
	}
	return nums[0];
}

//最佳案例，深刻理解了排序后数组的属性
int majorityElement_Eg001(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	return nums[nums.size() / 2];
}