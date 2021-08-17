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

//����ʱ������
vector<int> twoSum_Jx002(vector<int>& numbers, int target)
{
    for (int i = 0; i < numbers.size() - 1; i++)
    {
        int temp = target - numbers[i];
        if (temp > numbers[numbers.size() - 1])
        {
            continue;
        }
        for (int j = 1; i + j < numbers.size(); j++)
        {
            if (numbers[i + j]==temp)
            {
                return { i + 1, i + j + 1 };
            }
            else if (numbers[i + j] > temp)
            {
                continue;
            }
        }
    }
    return { 0,0 };
}

//time:0 ms	//memory:9.4 MB	//rank:100%
vector<int> twoSum_Jx003(vector<int>& numbers, int target)
{
    int len = numbers.size();   //��ֹunsigned long
    for (int i = 0; i < len - 2; i++)
    {
        if (numbers[i] == numbers[i + 2])
        {
            //����Ψһ�ģ�
            while (numbers[i] == numbers[i + 1])
            {
                i++;
            }
            continue;
        }
        int temp = target - numbers[i];
        if (temp > numbers[len - 1])
        {
            continue;
        }
        for (int j = 1; i + j < len; j++)
        {
            if (numbers[i + j] == temp)
            {
                return { i + 1, i + j + 1 };
            }
            else if (numbers[i + j] > temp)
            {
                continue;
            }
        }
    }
    return { len - 1,len };
}

//��참�� ������
//˼·�޵�
vector<int> twoSum_Eg001(vector<int>& numbers, int target) 
{
    int n = numbers.size(); //��¼����
    int low = 0, high = n - 1, sum;
    while (low < high) {
        sum = numbers[high] + numbers[low];
        if (sum == target)
            return { low + 1,high + 1 };
        else if (sum < target)
            low++;
        else
            high--;
    }
    return { -1,-1 };
}