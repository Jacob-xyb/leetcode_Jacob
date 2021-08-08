#include "../Jx_test.h"

//time:300 ms	//memory:12.8 MB	//rank:6.66%
int maxSubArray_Jx001(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//��ֹ����{...,����,max,����...}�����
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


//����������
//time:548 ms	//memory:12.8 MB	//rank:5.45%
int maxSubArray_Jx002(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//��ֹ����{...,����,max,����...}�����
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


//����һ��continue������΢�ӿ��ٶ�
//time:284 ms	//memory:12.8 MB	//rank:6.88%
int maxSubArray_Jx003(vector<int>& nums)
{
	int max = nums[0];
	int temp;
	for (int i = 0; i < nums.size(); i++)
	{
		max = (nums[i] > max ? nums[i] : max);	//��ֹ����{...,����,max,����...}�����
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


//��참��
//��ǰ�����ѯ
//����ۼ�<0������ʼ�����ӵ�ǰ��ʼ���¼����ۻ�
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