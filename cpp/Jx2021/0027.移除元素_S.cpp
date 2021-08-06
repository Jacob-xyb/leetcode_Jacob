#include "../Jx_test.h"

void deleteElement(vector<int>& nums, int idx)
{
	for (int i = idx; i < nums.size()-1; i++)
	{
		nums[i] = nums[i + 1];
		if (i==(nums.size()-2))
		{
			nums[i + 1] = -1;
		}
		else if (nums[i] == -1)
		{
			return;
		}
	}
}

int removeElement(vector<int>& nums, int val)
{

}