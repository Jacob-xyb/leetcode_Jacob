#include "../Jx_test.h"

//time:0 ms	//memory:6.4 MB	//rank:100%
vector<vector<int>> generate_Jx001(int numRows)
{
	if (numRows == 1) return { {1} };

	vector<vector<int>> res{ {1} };
	for (int i = 1; i < numRows; i++)
	{
		vector<int> temp(i+1,1);
		for (int j = 1; j < i; j++)
		{
			temp[j] = res[i - 1][j - 1] + res[i - 1][j];
		}
		res.push_back(temp);
	}
	return res;
}