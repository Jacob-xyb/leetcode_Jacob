#include "../Jx_test.h"

//time:300 ms	//memory:12.8 MB	//rank:6.66%
int maxSubArray_Jx001(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//防止出现{...,负数,max,负数...}的情况
		if (nums[i]<=0)
		{
			continue;
		}
		temp = nums[i];
		for (int j = i+1; j < nums.size(); j++)
		{
			temp += nums[j];
			max = (temp > max ? temp : max);
		}
	}
	return max;
}


//反而变慢了
//time:548 ms	//memory:12.8 MB	//rank:5.45%
int maxSubArray_Jx002(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//防止出现{...,负数,max,负数...}的情况
		if (nums[i] > 0)
		{
			temp = nums[i];
			for (int j = i + 1; j < nums.size(); j++)
			{
				temp += nums[j];
				if (nums[j]>0)
				{
					max = (temp > max ? temp : max);
				}
			}
		}
	}
	return max;
}


//少用一次continue可以稍微加快速度
//time:284 ms	//memory:12.8 MB	//rank:6.88%
int maxSubArray_Jx003(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//防止出现{...,负数,max,负数...}的情况
		if (nums[i] > 0)
		{
			temp = nums[i];
			for (int j = i + 1; j < nums.size(); j++)
			{
				temp += nums[j];
				max = (temp > max ? temp : max);
			}
		}
	}
	return max;
}


//最快案例
//往前分组查询
//如果累加<0，则起始索引从当前开始重新计算累积
int maxSubArray_Eg001(vector<int>& nums) 
{
	if (nums.size() == 1)
		return nums[0];
	int max = nums[0];
	int mid = nums[0];
	for (int i = 1; i < nums.size(); i++) {
		int a = mid > 0 ? mid : 0;
		mid = a + nums[i];
		max = mid > max ? mid : max;
	}
	return max;
}