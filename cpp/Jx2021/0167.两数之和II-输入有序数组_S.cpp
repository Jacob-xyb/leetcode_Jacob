#include "../Jx_test.h"

//超过时间限制
//原因，升序排列，但是元素可能相同
vector<int> twoSum_Jx001(vector<int>& numbers, int target)
{
    for (int i = 0; i < numbers.size() - 1; i++)
    {
        for (int j = 1; i + j < numbers.size(); j++)
        {
            int temp = numbers[i] + numbers[i + j];
            if (temp == target)
            {
                return { i + 1, i + j + 1 };
            }
            else if (temp > target)
            {
                continue;
            }
        }
    }
    return { 0,0 };
}