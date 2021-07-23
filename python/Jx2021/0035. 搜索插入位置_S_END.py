from typing import *
"""题目描述"""
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
'''

"""示例"""
'''
输入: [1,3,5,6], 5
输出: 2
输入: [1,3,5,6], 2
输出: 1
输入: [1,3,5,6], 7
输出: 4
'''

"""解题思路"""
'''
v1.0:
- 既然已知是排序序列，用二分法即可
v1.1:
- 最快范例,不太好理解结束条件。
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target > nums[-1]:
            return n
        elif target < nums[0]:
            return 0

        idxL, idxR = 0, n-1
        while 1:
            idx = (idxR+idxL)//2
            if nums[idx] == target:
                return idx
            elif idx == idxL:
                return idx+1
            else:
                if nums[idx] > target:
                    idxR = idx
                elif nums[idx] < target:
                    idxL = idx

class Solution_V1_1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return left
