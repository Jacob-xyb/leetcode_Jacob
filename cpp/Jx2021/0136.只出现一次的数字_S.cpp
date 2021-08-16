#include "../Jx_test.h"

//���˺ܾã�����㷨Ӧ�þ�������ʱ�临�Ӷȡ� ����Բ�ʹ�ö���ռ���ʵ����
//	����ǲ�̫���ܣ�Ҫô����ʱ�临�Ӷȣ�Ҫô��ʹ�ö���ռ䣬ͬʱʵ���Ҿ��ú�����
//	��������̫�˵�ԭ��
//time:448 ms	//memory:17.2 MB	//rank:6.42%
int singleNumber_Jx001(vector<int>& nums)
{
	//���ȱ���һ�飬�ж���Ҫ��������������ż��
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

//��β��ж���ż����
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

//������� �����н�����
// a��b��a = b��a��a = b��(a��a) = b��0 = b��
int singleNumber_Eg001(vector<int>& nums) {
	int num = nums[0];
	for (int i = 1; i < nums.size(); i++) {
		num ^= nums[i];
	}
	return num;
}