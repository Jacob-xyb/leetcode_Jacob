#include "../Jx_test.h"

//����ʱ������
//ԭ���������У�����Ԫ�ؿ�����ͬ
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