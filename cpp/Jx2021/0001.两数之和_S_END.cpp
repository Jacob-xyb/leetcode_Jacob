#include "../Jx_test.h"
//#include <unordered_map>

//这样写的效率好像很低
//time:728 ms	//memory:9.8 MB
vector<int> twoSum_Jx001(vector<int>& nums, int target)
{
	//两次for循环遍历得出结果
	vector<int> res{ 0,0 };
	for (res[0]; res[0] < nums.size() - 1; res[0]++)
	{
		res[1] = res[0] + 1;
		while (res[1] < nums.size())
		{
			if (nums[res[0]] + nums[res[1]] == target)
			{
				return res;
			}
			res[1]++;
		}
	}
	return res;
}

//不算加法
//time:588 ms	//memory:9.8M
vector<int> twoSum_Jx002(vector<int>& nums, int target)
{
	//两次for循环遍历得出结果
	vector<int> res{ 0,0 };
	int temp;
	for (res[0]; res[0] < nums.size() - 1; res[0]++)
	{
		temp = target - nums[res[0]];
		res[1] = res[0] + 1;
		while (res[1] < nums.size())
		{
			if (nums[res[1]] == temp)
			{
				return res;
			}
			res[1]++;
		}
	}
	return res;
}


//只算一次size()
//time:564 ms	//memory:9.8M
vector<int> twoSum_Jx003(vector<int>& nums, int target)
{
	//两次for循环遍历得出结果
	vector<int> res{ 0,0 };
	int temp;
	int n = nums.size();
	for (res[0]; res[0] < n - 1; res[0]++)
	{
		temp = target - nums[res[0]];
		res[1] = res[0] + 1;
		while (res[1] < n)
		{
			if (nums[res[1]] == temp)
			{	
				return res;
			}
			res[1]++;
		}
	}
	return res;
}

//最快答案，但是看不懂	//TODO
// time:12 ms	//memory:10.5 MB
vector<int> twoSum_Ans001(vector<int>& nums, int target) {
	unordered_map<int, int> hashtable;
	for (int i = 0; i < nums.size(); ++i) {
		auto it = hashtable.find(target - nums[i]);
		if (it != hashtable.end()) {
			return { it->second, i };
		}
		hashtable[nums[i]] = i;
	}
	return {};
}