#include "../Jx_test.h"

//set_intersection()���������ƱȽ϶�
//	���������������Ҫ������ģ������ǲ��ظ���
//	˵������Ϊset�������ģ��������򡢲��ظ�����������Ҳ�ǿ��Ե�
//	������Ҫô���ǽ�����Ҫô�ͻ����ظ���Ԫ��
vector<int> intersection_Jx001(vector<int>& nums1, vector<int>& nums2)
{
	vector<int> res;
	set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(),
		inserter(res, res.begin()));
	return res;
}

//time:8 ms	//memory:10.6 MB	//rank:55.47%
vector<int> intersection_Jx002(vector<int>& nums1, vector<int>& nums2)
{
	set<int> set_nums1(nums1.begin(), nums1.end());
	set<int> set_nums2(nums2.begin(), nums2.end());
	vector<int> res;

	set_intersection(set_nums1.begin(), set_nums1.end(), set_nums2.begin(), set_nums2.end(),
		inserter(res, res.begin()));
	return res;
}

//�ڴ����н���ע��
//time:4 ms	//memory:9.6 MB	//rank:91.45%
vector<int> intersection_Eg001(vector<int>& nums1, vector<int>& nums2) {
    //�Ƚ��������н�������
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int len1 = nums1.size(), len2 = nums2.size();
    int i = 0, j = 0;
    vector<int> ret;
    while (i < len1 && j < len2) {  //�˳�ѭ��������
        //�������������������������һ��������ѭ��
        //  ����Ԫ����ͬʱ
        if (nums1[i] == nums2[j]) {
            //����Ԫ����ͬʱ�����retΪ��ֱ��ѹ��
            //����Ԫ����ͬʱ��ret��Ϊ�գ�Ԫ�ز�����β��Ҳ����ѹ��
            if (!ret.size() || nums1[i] != ret.back()) {
                ret.emplace_back(nums1[i]);
            }
            //�󽻼������ i++;j++; ��������ƶ�
            i++; j++;
        }
        //  �ĸ�С���ĸ������ƣ�ȥѰ���Ƿ��н���
        else if (nums1[i] < nums2[j]) {
            i++;
        }
        else {
            j++;
        }
    }
    return ret;
}
