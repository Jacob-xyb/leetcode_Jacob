"""题目描述"""
'''
给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。
我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
'''

"""示例"""
'''
输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
'''

"""解题思路"""
'''
v1.0:
- TODO：加速刷题中。
v1.1:
- 最效率范例
- 思路与v1.0相同。 
'''


class Solution:
    def pivotIndex(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return -1
        elif n == 1:
            return 0
        sumL = 0
        sumR = sum(nums[1:])
        if sumR == 0:
            return 0
        else:
            for i in range(1,n):
                sumL += nums[i-1]
                sumR -= nums[i]
                if sumL == sumR:
                    return i
        return -1

class Solution_v1_1:
    def pivotIndex(self, nums: list) -> int:
        _sum = sum(nums)
        _left_sum = 0
        to_return = -1
        for i in range(len(nums)):
            if _sum - nums[i] == 2 * _left_sum:
                to_return = i
                break
            _left_sum += nums[i]
        return to_return
