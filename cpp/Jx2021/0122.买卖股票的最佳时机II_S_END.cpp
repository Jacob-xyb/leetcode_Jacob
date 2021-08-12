#include "../Jx_test.h"

//初次尝试想的就是在股票跌之前卖出去
//time:0 ms	//memory:12.7 MB	//rank:100%
int maxProfit_Jx001(vector<int>& prices)
{
	if (prices.size() == 1) return 0;
	int buy = prices[0];
	int sell = prices[1];
	int profit = 0;
	for (int i = 1; i < prices.size()-1; i++)
	{
		if (prices[i] > sell)
		{
			sell = prices[i];
			continue;
		}
		if (prices[i] < prices[i - 1])
		{
			profit += max(0, sell - buy);
			buy = prices[i];
			sell = prices[i + 1];
		}
	}
	//最后一天肯定不能买了
	if (prices[prices.size() - 1] > sell)
	{
		sell = prices[prices.size() - 1];
	}
	profit += max(0, sell - buy);
	return profit;
}

//最快案例，赚差价的思想	//太妙了
int maxProfit_Eg001(vector<int>& prices) {
	int n = prices.size(), sum = 0;
	for (int i = 0; i < n - 1; i++)
	{
		if (prices[i] < prices[i + 1])
		{
			sum += prices[i + 1] - prices[i];
		}
	}
	return sum;
}