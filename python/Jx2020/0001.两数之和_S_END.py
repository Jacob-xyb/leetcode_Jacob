"""题目描述"""
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''

"""示例"""
'''
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

"""解题思路"""
'''
v1.0:
- 比较简单
v1.1:
- 官方遍历，内存小一点
v1.2:
- 哈希表
'''


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)-1):
            y = target - nums[i]
            if y in nums[i+1:]:
                return [i, (nums[i+1:].index(y))+i+1]


class Solution_v1_1:
    def twoSum(self, nums: list, target: int) -> list:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class Solution_v1_2:
    def twoSum(self, nums: list, target: int) -> list:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
