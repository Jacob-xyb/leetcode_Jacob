#include "../Jx_test.h"

//time:108 ms	//memory:91.2 MB	//rank:81.16%
int maxProfit_Jx001(vector<int>& prices)
{
    if (prices.size() == 1) return 0;
    int buy = prices[0];
    int sell = prices[1];
    int profit = sell - buy;
    for (int i = 1; i < prices.size() - 1; i++)
    {
        if (prices[i] < buy)
        {
            buy = prices[i];
            sell = prices[i + 1];
            profit = (sell - buy) > profit ? (sell - buy) : profit;
        }
        if (prices[i] > sell)
        {
            sell = prices[i];
            profit = (sell - buy) > profit ? (sell - buy) : profit;
        }
    }
    //��ʣ���һ��
    if (prices[prices.size() - 1] > sell)
    {
        sell = prices[prices.size() - 1];
        profit = (sell - buy) > profit ? (sell - buy) : profit;
    }
    profit = profit >= 0 ? profit : 0;
    return profit;
}


//��ʵֻҪÿ�λ�buy��ʱ���ж�һ��profit����
//time:104 ms	//memory:91.2 MB	//rank:86.61%
int maxProfit_Jx002(vector<int>& prices)
{
    if (prices.size() == 1) return 0;
    int buy = prices[0];
    int sell = prices[1];
    int profit = sell - buy;
    for (int i = 1; i < prices.size() - 1; i++)
    {
        if (prices[i] < buy)
        {
            profit = (sell - buy) > profit ? (sell - buy) : profit;
            buy = prices[i];
            sell = prices[i + 1];

        }
        if (prices[i] > sell)
        {
            sell = prices[i];
        }
    }
    //��ʣ���һ��
    if (prices[prices.size() - 1] > sell)
    {
        sell = prices[prices.size() - 1];
    }
    profit = (sell - buy) > profit ? (sell - buy) : profit;
    return profit >= 0 ? profit : 0;
}


//���������ˣ����䲻�����
//time:120 ms	//memory:91.2 MB	//rank:66.80%
int maxProfit_Jx003(vector<int>& prices)
{
    if (prices.size() == 1) return 0;
    int buy = prices[0];
    int sell = prices[1];
    int profit = sell - buy;
    for (int i = 1; i < prices.size() - 1; i++)
    {
        if (prices[i] > sell)
        {
            sell = prices[i];
            continue;
        }
        if (prices[i] < buy)
        {
            profit = (sell - buy) > profit ? (sell - buy) : profit;
            buy = prices[i];
            sell = prices[i + 1];
        }
    }
    //��ʣ���һ��
    if (prices[prices.size() - 1] > sell)
    {
        sell = prices[prices.size() - 1];
    }
    profit = (sell - buy) > profit ? (sell - buy) : profit;
    return profit >= 0 ? profit : 0;
}

//�����һ����참����˼�룬����򵥷�������
//time:100 ms	//memory:91.1 MB	//rank:91.09%
int maxProfit_Jx004(vector<int>& prices)
{
    if (prices.size() == 1) return 0;
    int buy = prices[0];
    int profit = 0;
    for (int i = 1; i < prices.size(); i++)
    {
        buy = prices[i] < buy ? prices[i] : buy;
        profit = prices[i] - buy > profit ? prices[i] - buy : profit;
    }
    return profit;
}

//�ٶȲ����ȶ�..96~132 ms
int maxProfit_Eg001(vector<int>& prices) {
    int n = prices.size();
    if (n < 2) {
        return 0;
    };
    int max_profit = 0;
    int min_price = prices[0];
    for (int i = 1; i < n; i++) {
        min_price = min(min_price, prices[i]);
        max_profit = max(max_profit, prices[i] - min_price);
    };
    return max_profit;
};