#include "../Jx_test.h"

//想了很久：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
//	这就是不太可能，要么线性时间复杂度，要么不使用额外空间，同时实现我觉得很离谱
//	可能是我太菜的原因。
//time:448 ms	//memory:17.2 MB	//rank:6.42%
int singleNumber_Jx001(vector<int>& nums)
{
	//首先遍历一遍，判断需要的数是奇数还是偶数
	int arrSum = 0;
	vector<int> temp;
	for (int i = 0; i < nums.size(); i++)
	{
		arrSum += nums[i];
	}
	if (!arrSum % 2)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[i]%2)
			{
				arrSum -= nums[i];
			}
			else
			{
				if (!count(temp.begin(),temp.end(),nums[i]))
				{
					temp.push_back(nums[i]);
				}
				else
				{
					arrSum -= nums[i] * 2;
				}
			}
		}
	}
	else
	{
		for (int i = 0; i < nums.size(); i++)
		{
			if (!nums[i] % 2)
			{
				arrSum -= nums[i];
			}
			else
			{
				if (!count(temp.begin(), temp.end(), nums[i]))
				{
					temp.push_back(nums[i]);
				}
				else
				{
					arrSum -= nums[i] * 2;
				}
			}
		}
	}
	return arrSum;
}

//这次不判断奇偶性了
//time:576 ms	//memory:17 MB	//rank:6.42%
int singleNumber_Jx002(vector<int>& nums)
{
	int arrSum = 0;
	vector<int> temp;
	for (int i = 0; i < nums.size(); i++)
	{
		arrSum += nums[i];
	}

	for (int i = 0; i < nums.size(); i++)
	{
		if (!count(temp.begin(), temp.end(), nums[i]))
		{
			temp.push_back(nums[i]);
		}
		else
		{
			arrSum -= nums[i] * 2;
		}
	}
	return arrSum;
}

//完美解答 异或具有交换律
// a⊕b⊕a = b⊕a⊕a = b⊕(a⊕a) = b⊕0 = b。
int singleNumber_Eg001(vector<int>& nums) {
	int num = nums[0];
	for (int i = 1; i < nums.size(); i++) {
		num ^= nums[i];
	}
	return num;
}