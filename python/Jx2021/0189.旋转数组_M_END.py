"""题目描述"""
'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''

"""示例"""
'''
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
'''

"""解题思路"""
'''
v1.0:
- 比较简单，但是效率不高。
v1.1:
- 最快范例。
'''


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k != 0:
            nums[:] = (nums[-k:]+nums[0:-k])

class Solution_v1_1:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]