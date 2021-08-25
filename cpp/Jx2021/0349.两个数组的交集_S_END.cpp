#include "../Jx_test.h"

//set_intersection()函数的限制比较多
//	输入的两个序列需要是升序的，并且是不重复的
//	说白了是为set量身定做的，但是升序、不重复的其他序列也是可以的
//	否则结果要么不是交集，要么就会有重复的元素
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

//在代码中进行注释
//time:4 ms	//memory:9.6 MB	//rank:91.45%
vector<int> intersection_Eg001(vector<int>& nums1, vector<int>& nums2) {
    //先将两个序列进行排序
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int len1 = nums1.size(), len2 = nums2.size();
    int i = 0, j = 0;
    vector<int> ret;
    while (i < len1 && j < len2) {  //退出循环的条件
        //三个条件包含所有情况，满足一个就跳入循环
        //  两个元素相同时
        if (nums1[i] == nums2[j]) {
            //两个元素相同时，如果ret为空直接压入
            //两个元素相同时，ret不为空，元素不等于尾数也立即压入
            if (!ret.size() || nums1[i] != ret.back()) {
                ret.emplace_back(nums1[i]);
            }
            //求交集，因此 i++;j++; 均可向后移动
            i++; j++;
        }
        //  哪个小，哪个往后移，去寻找是否有交集
        else if (nums1[i] < nums2[j]) {
            i++;
        }
        else {
            j++;
        }
    }
    return ret;
}
