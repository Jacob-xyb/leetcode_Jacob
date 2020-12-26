"""题目描述"""
'''
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
'''

"""示例"""
'''
输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

输入: [1,2,2,3,1,4,2]
输出: 6
'''

"""解题思路"""
'''
v1.0:
- 思路简单但是复杂度高，时间超时。
v1.1:
- 官方左右数组解答:https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode/

'''


class Solution:
    def findShortestSubArray(self, s: list) -> int:
        from collections import Counter
        numlist = dict(Counter(s))
        maxcot = max(numlist.values())
        i = 0
        j = maxcot
        while maxcot == max(dict(Counter(s[i+1:])).values()):
            i += 1
        while i+j <= len(s) or maxcot == max(dict(Counter(s[i:i+j+1])).values()):
            j += 1
        # print(j+1)
        return j+1

class Solution_v1_1(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans