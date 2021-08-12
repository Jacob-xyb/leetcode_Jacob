#include "../Jx_test.h"

//error
vector<int> getRow_Jx001(int rowIndex)
{
	if (rowIndex == 0)
	{
		return { 1 };
	}
	vector<int> temp(rowIndex + 1, 1);
	for (int i = 1; i <= rowIndex; i++)
	{
		for (int j = 1; j < i; j++)
		{
			temp[j] += temp[j - 1];	//上一行已经被改变
		}
	}
	return temp;
}

//由于是当前值+前面一个值，那么反着来就可以了
//time:0 ms	//memory:6.1 MB	//rank:100%
vector<int> getRow_Jx002(int rowIndex)
{
	vector<int> temp(rowIndex + 1, 1);
	for (int i = 1; i <= rowIndex; i++)
	{
		for (int j = i-1; j > 0; j--)
		{
			temp[j] += temp[j - 1];	//上一行已经被改变
		}
	}
	return temp;
}