#include "../Jx_test.h"

//time:0 ms	//memory:8.9 MB	//rank:100%
void merge_Jx001(vector<int>& nums1, int m, vector<int>& nums2, int n)
{
	//���Ǳ�ǩ���ȥ������
	if (n==0)
	{
		return;
	}
	else if (m==0)
	{
		nums1 = nums2;
		return;
	}
	//�Ƚ�nums1�����ŵ�����ȥ
	for (int i = m-1; i >= 0; i--)
	{
		nums1[i + n] = nums1[i];
	}
	//Ȼ������
	int idx = 0;
	int idx1 = n;
	int idx2 = 0;
	while (idx < (m+n))
	{
		if (nums1[idx1]<nums2[idx2])
		{
			nums1[idx] = nums1[idx1];
			idx1++;
		}
		else
		{
			nums1[idx] = nums2[idx2];
			idx2++;
		}
		idx++;
		if (idx1 == m+n)
		{
			for (idx2; idx2 < n; idx2++)
			{
				nums1[idx] = nums2[idx2];
				idx++;
			}
		}
		else if (idx2 == n)
		{
			for (idx1; idx1 < m+n; idx1++)
			{
				nums1[idx] = nums1[idx1];
				idx++;
			}
		}
	}
	return;
}


//�൱����
//1.�������ȴӴ�С���Ͳ��ð�nums1Ųλ����
//2.whileѭ�����������
void merge_Eg001(vector<int>& nums1, int m, vector<int>& nums2, int n) {
	int n1 = m - 1;
	int n2 = n - 1;
	int length = m + n - 1;
	if (n == 0) return;
	while (n1 >= 0 && n2 >= 0) {
		if (nums1[n1] < nums2[n2]) {
			nums1[length--] = nums2[n2--];
		}
		else {
			nums1[length--] = nums1[n1--];
		}
	}
	while (n2 >= 0) {
		nums1[length--] = nums2[n2--];
	}
}
