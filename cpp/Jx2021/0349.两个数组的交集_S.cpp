#include "../Jx_test.h"


vector<int> intersection_Jx001(vector<int>& nums1, vector<int>& nums2)
{
	unordered_set<int> set_res;
	vector<int> res;
	set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(),
		inserter(res, res.begin()));
	//res.assign(set_res.begin(), set_res.end());
	return res;
}


vector<int> intersection_Jx002(vector<int>& nums1, vector<int>& nums2)
{
	unordered_set<int> set_nums1(nums1.begin(),nums1.end());
	unordered_set<int> set_nums2(nums2.begin(), nums2.end());
	unordered_set<int> set_res;

	set_intersection(set_nums1.begin(), set_nums1.end(), set_nums2.begin(), set_nums2.end(),
		inserter(set_res, set_res.begin()));
	vector<int> res;
	res.assign(set_res.begin(), set_res.end());
	return res;
}