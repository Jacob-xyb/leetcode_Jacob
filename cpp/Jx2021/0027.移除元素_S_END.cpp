#include "../Jx_test.h"

/*由于只允许用一个空间，于是想到这个空间用来记录需要输出的个数
同时也很符合数组存放的位置
获取第一个数就放在0号位
获取第二个数就放在1号位
以此类推...*/
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

//最快案例，思路也很清晰
int removeElement_Eg001(vector<int>& nums, int val) 
{
    int size = nums.size();
    for (int i = 0; i < size; i++) {
        if (nums[i] == val) { // 发现需要移除的元素，就将数组集体向前移动一位
            for (int j = i + 1; j < size; j++) {
                nums[j - 1] = nums[j];
            }
            i--; // 因为下表i以后的数值都向前移动了一位，所以i也向前移动一位
            size--; // 此时数组的大小-1
        }
    }
    return size;
}