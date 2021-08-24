#include "../Jx_test.h"

//题目很简单，但是描述的很云里雾里，跳过
//time:32 ms	//memory:16.6 MB	//rank:36.55%
class NumArray {
public:
    vector<int> sums;

    NumArray(vector<int>& nums) {
        int n = nums.size();
        sums.resize(n + 1);
        for (int i = 0; i < n; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
    }

    int sumRange(int i, int j) {
        return sums[j + 1] - sums[i];
    }
};