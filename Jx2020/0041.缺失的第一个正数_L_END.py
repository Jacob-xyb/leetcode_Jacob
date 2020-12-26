"""题目描述"""
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''

"""示例"""
'''
输入: [1,2,0]
输出: 3

输入: [3,4,-1,1]
输出: 2
'''

"""解题思路"""
'''
v1.0:
- 不知为何反正dict速度就是很快很快，列表就是超时的
1. 首先遍历一下，舍去0项，不去也行，考虑到后面遍历，就减小了一下数据尺寸，但是每次都要判断一下也会延长时间，等会试试直接全部写成哈希表。
2. 如果都是负数的话就直接返回```1```
3. 如果有正数，那么从```1```开始寻找缺失的那个正数。
v1.1:
- 官方正解
- 理解的前提是输入的i 肯定在 [1,n+1]这个区间内，可以找规律得出。
- 在理解后，原地哈希即可。
'''


class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        posnums = {}
        for i in nums:
            if i > 0:
                posnums[i] = 1
        if posnums == {}:
            return 1
        res = 1
        while posnums:
            if res not in posnums:
                return res
            res += 1


class Solution_v1_1:
    def firstMissingPositive(self, nums: list) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

