#include "../Jx_test.h"

//time:4 ms	//memory:8.6 MB	//rank:50.61%
vector<int> plusOne_Jx001(vector<int>& digits)
{
	if (digits == vector<int>(digits.size(),9))
	{
		vector<int> res(digits.size() + 1, 0);
		res[0] = 1;
		return res;
	}
	else
	{
		int bit = digits.size()-1;
		while (digits[bit]==9)
		{
			digits[bit] = 0;
			bit--;
		}
		digits[bit]++;
		return digits;
	}
}


//time:0 ms	//memory:8.4 MB	//rank:100%
vector<int> plusOne_Jx002(vector<int>& digits)
{
	int bit = digits.size() - 1;
	while (bit >= 0 && digits[bit] == 9)
	{	
		digits[bit] = 0;
		bit--;
	}
	if (bit==-1)
	{
		vector<int> res(digits.size() + 1);
		res[0] = 1;
		return res;
	}
	digits[bit]++;
	return digits;
}


//��Ѱ����������Ҿ��ò����Ǻܺã����Ƕ��ж���һ��
//��ʵ��֤���������ø����ʱ�� 
vector<int> plusOne_Eg001(vector<int>& digits) {
	int n = digits.size();
	bool flag = false;
	// �����һλ��һ
	digits[n - 1]++;

	for (int i = n - 1; i >= 0; i--)
	{
		if (flag)
			digits[i] += 1;
		if (digits[i] == 10)
		{
			flag = true;
			digits[i] = 0;
			if (i == 0)
			{
				digits.insert(digits.begin(), 1);
				return digits;
			}
		}
		else {
			flag = false;
		}
	}
	return digits;
}


//"������"��Ȼ������
//�������ø����ʱ��
//time:4 ms	//memory:8.4 MB	//rank:50.61%
vector<int> plusOne_Jx003(vector<int>& digits)
{
	int bit = digits.size() - 1;
	while (bit >= 0 && digits[bit] == 9)
	{
		digits[bit] = 0;
		bit--;
	}
	if (bit == -1)
	{
		digits.insert(digits.begin(), 1);
		return digits;
	}
	digits[bit]++;
	return digits;
}
