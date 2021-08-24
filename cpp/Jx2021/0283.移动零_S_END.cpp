#include "../Jx_test.h"

//time:0 ms	//memory:8.8 MB	//rank:100%
void moveZeroes_Jx001(vector<int>& nums)
{
	int len = nums.size();
	int zeroNum = 0;
	for (int i = 0; i < len; i++)
	{
		if (nums[i] == 0)
		{
			zeroNum++;
			continue;
		}
		nums[i - zeroNum] = nums[i];
	}
	for (int j = len-zeroNum; j < len; j++) nums[j] = 0;
}

//×î¼Ñ°¸Àý£¬Ð´µÄÃî
void moveZeroes_Eg001(vector<int>& nums) {
	int index = 0;
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] != 0) {
			nums[index++] = nums[i];
		}
	}
	for (int i = index; i < nums.size(); i++) {
		nums[i] = 0;
	}
}