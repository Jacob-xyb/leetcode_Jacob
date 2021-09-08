#include "../Jx_test.h"

//-2147483412 此输入不通过
int reverse_Jx001(int x)
{
	int y = abs(x);
	string s = to_string(y);
	int n = s.size();
	int res = 0;
	if ( (y % 10) * pow(10,n-1) > pow(2, 31) - 1) { return 0; }
	for (int i = 0; i < n; i++)
	{
		res += (y / int(pow(10, i)) - (y / int(pow(10, i + 1)) * 10) ) * pow(10,n-i-1);
	}
	if (x < 0) return -res;
	return res;
}

void reverse_test()
{
	cout.precision(9);
	int res = reverse_Jx001(1534236469);
	cout << res << endl;
	cout << pow(2, 31) << endl;
}