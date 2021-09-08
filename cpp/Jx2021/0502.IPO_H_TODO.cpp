#include "../Jx_test.h"

//超时
int findMaximizedCapital_Jx001(int k, int w, vector<int>& profits, vector<int>& capital)
{
	int* p =  &capital[0];
	int n = capital.size();
	int capMax = *max_element(p, p + n);
	//同时排序
	for (int i = profits.size(); i >0; i--)
	{
		int times = 0;
		for (int j = 1; j < i; j++)
		{
			if ( profits[j-1] < profits[j] )
			{
				int temp1 = profits[j - 1];
				profits[j - 1] = profits[j];
				profits[j] = temp1;
				int temp2 = capital[j - 1];
				capital[j - 1] = capital[j];
				capital[j] = temp2;
				times++;
			}
		}
		if (!times) { break; }
	}
	while (k > 0)
	{
		if ( w > capMax)
		{
			for (int i = 0; i < capital.size(); i++)
			{
				if (capital[i] <= w && capital[i] >= 0)
				{
					w += profits[i];	//赚取利润
					capital[i] = -1;	//结束交易
					k--;
				}
				if (k == 0)
				{
					return w;
				}
			}
		}
		else
		{
			for (int i = 0; i < capital.size(); i++)
			{
				if (capital[i] <= w && capital[i] >= 0)
				{
					w += profits[i];	//赚取利润
					capital[i] = -1;	//结束交易
					break;
				}
			}
		}
		k--;
	}
	return w;
}

int findMaximizedCapital_Jx002(int k, int w, vector<int>& profits, vector<int>& capital)
{
	return 0;
}

void findMaximizedCapital_test()
{
	int k = 2;
	int w = 0;
	vector<int> p{ 3,3,3 };
	vector<int> c{ 0,1,1 };
	int r = findMaximizedCapital_Jx001(k, w, p, c);
	cout << r << endl;
}
