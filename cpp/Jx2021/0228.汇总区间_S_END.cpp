#include "../Jx_test.h"


//time:0 ms	//memory:6.8 MB	//rank:100%
vector<string> summaryRanges_Jx001(vector<int>& nums)
{
	vector<string> res;
	int len = nums.size();
	if (len == 0) return res;
	if (len == 1)
	{
		res.push_back(to_string(nums[0]));
		return res;
	}
	long left = nums[0], right = nums[0];	//数字可能挺大的
	for (int i = 1; i < len; i++)
	{
		if (nums[i] - right != 1)
		{
			if (left == right)
			{
				res.push_back(to_string(right));
			}
			else
			{
				string temp;
				temp += to_string(left) + "->" + to_string(right);
				res.push_back(temp);
			}
			left = right = nums[i];
		}
		else
		{
			right++;
		}
	}
	if (left == right)
	{
		res.push_back(to_string(right));
	}
	else
	{
		string temp;
		temp += to_string(left) + "->" + to_string(right);
		res.push_back(temp);
	}
	return res;
}

//push_back(string)可以写在一起
//time:0 ms	//memory:6.8 MB	//rank:100%
vector<string> summaryRanges_Jx002(vector<int>& nums)
{
	vector<string> res;
	int len = nums.size();
	if (len == 0) return res;
	if (len == 1)
	{
		res.push_back(to_string(nums[0]));
		return res;
	}
	long left = nums[0], right = nums[0];	//数字可能挺大的
	for (int i = 1; i < len; i++)
	{
		if (nums[i] - right != 1)
		{
			if (left == right) res.push_back(to_string(right));
			else res.push_back(to_string(left) + "->" + to_string(right));
			left = right = nums[i];
		}
		else right++;
	}

	if (left == right) res.push_back(to_string(right));
	else res.push_back(to_string(left) + "->" + to_string(right));

	return res;
}