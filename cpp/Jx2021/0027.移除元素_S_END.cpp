#include "../Jx_test.h"

/*����ֻ������һ���ռ䣬�����뵽����ռ�������¼��Ҫ����ĸ���
ͬʱҲ�ܷ��������ŵ�λ��
��ȡ��һ�����ͷ���0��λ
��ȡ�ڶ������ͷ���1��λ
�Դ�����...*/
//time:4 ms	//memory:8.6 MB
int removeElement_Jx001(vector<int>& nums, int val)
{
	int num = 0;
	for (int i = 0; i < nums.size(); i++)
	{
		if (nums[i] != val)
		{
			nums[num] = nums[i];
			num++;
		}
	}
	return num;
}

//��참����˼·Ҳ������
int removeElement_Eg001(vector<int>& nums, int val) 
{
    int size = nums.size();
    for (int i = 0; i < size; i++) {
        if (nums[i] == val) { // ������Ҫ�Ƴ���Ԫ�أ��ͽ����鼯����ǰ�ƶ�һλ
            for (int j = i + 1; j < size; j++) {
                nums[j - 1] = nums[j];
            }
            i--; // ��Ϊ�±�i�Ժ����ֵ����ǰ�ƶ���һλ������iҲ��ǰ�ƶ�һλ
            size--; // ��ʱ����Ĵ�С-1
        }
    }
    return size;
}