#include "../Jx_test.h"

//����ѭ�����Խ��99%�����⣬���ǻ᲻��̫����
//����ʱ������
bool containsDuplicate_Jx001(vector<int>& nums)
{
	for (int i = 0; i < nums.size()-1; i++)
	{
		for (int j = 1; i+j < nums.size(); j++)
		{
			if (nums[i] == nums[i + j]) return true;
		}
	}
	return false;
}

//����ʱ������
bool containsDuplicate_Jx002(vector<int>& nums)
{
	int len = nums.size();
	//find min
	for (int i = len - 1; i > 0; i--)
	{
		if (nums[i] < nums[i - 1])
		{
			int temp = nums[i];
			nums[i] = nums[i - 1];
			nums[i - 1] = temp;
		}
		else if (nums[i] == nums[i - 1]) return true;
	}
	//sort
	for (int i = 0; i < len - 2; i++)
	{
		for (int j = 1; j < len - 1 - i; j++)
		{
			if (nums[j] > nums[j + 1])
			{
				int temp = nums[j + 1];
				nums[j + 1] = nums[j];
				nums[j] = temp;
			}
			else if (nums[i] == nums[i + j]) return true;
		}
		//len-2>max-min-1
		if ((len - i) - 2 > nums[len - 1 - i] - nums[0] - 1) return true;
	}
	return false;
}

//����ʱ������
bool containsDuplicate_Jx003(vector<int>& nums)
{
	int len = nums.size();
	//sort
	for (int i = 0; i < len - 2; i++)
	{
		for (int j = 0; j < len - 1 - i; j++)
		{
			if (nums[j] > nums[j + 1])
			{
				int temp = nums[j + 1];
				nums[j + 1] = nums[j];
				nums[j] = temp;
			}
		}
		//len-2>max-min-1
		//if ((len - i) - 2 > nums[len - 1 - i] - nums[0] - 1) return true;
	}
	for (int i = 0; i < len-1; i++)
	{
		if (nums[i] == nums[i+1])
		{
			return true;
		}
	}
	return false;
}

//�ͺ����ף����ʵ�ֵģ�
//time:44 ms	//memory:22 MB	//rank:24.59%
bool containsDuplicate_Jx004(vector<int>& nums)
{
	set<int> s(nums.begin(), nums.end());
	return s.size() != nums.size();
}

//��������ף����ķ�����������
bool containsDuplicate_Eg001(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	int n = nums.size();
	for (int i = 0; i < n - 1; i++) {
		if (nums[i] == nums[i + 1]) {
			return true;
		}
	}
	return false;
}
