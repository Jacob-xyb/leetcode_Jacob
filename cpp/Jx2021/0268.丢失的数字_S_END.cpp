#include "../Jx_test.h"

//time:12 ms	//memory:17.4 MB	//rank:96.57%
int missingNumber_Jx001(vector<int>& nums)
{
	int n = nums.size();
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += nums[i];
	}
	return n * (n+1) / 2 - sum;
}

//提供了另一种思路，用异或的方式来找出缺失的那个数
//time:16 ms	//memory:17.6 MB	//rank:85.37%
int missingNumber_Eg001(vector<int>& nums) {
    int ans = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        ans ^= nums[i];
    }
    for (int i = 0; i <= nums.size(); i++) {
        ans ^= i;
    }
    return ans;
}
