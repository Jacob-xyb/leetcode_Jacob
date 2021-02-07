from typing import *
"""题目描述"""
'''
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
'''

"""示例"""
'''
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
'''

"""解题思路"""
'''
v1.0:
- 我真的觉得这个简单题不是很简单。
- 如果一次遍历的话就需要分四种情况讨论，我做的有点崩溃了就用了四次遍历
- 首先一锅端，如果不能一锅端就找出需要修改的元素，重点来了，这个元素应该如何修改：
__分四种情况，判别要修改的元素处加黑（idx的位置自己判断）:__
1. __50__,40,60 (在第一个位置，直接nums[idx]=nums[idx+1]即可)
2. 40,60,__50__ (在最后一个位置，直接nums[idx+1]=nums[idx]即可)
3. 40,__30__,60 (将idx+1的数字变大，nums[idx+1]=nums[idx])
4. __50__,10,40 (将idx的数字变小，nums[idx]=nums[idx+1])
思路没问题的，可是代码稀烂，去看看大佬的代码了。
v1.1:
- 最快范例，太精简了，可是不好想出来呀。
'''


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        if nums == sorted(nums):
            return True
        else:
            for idx in range(n-1):
                if nums[idx] > nums[idx+1]:
                    dif1 = nums[:]
                    dif1[idx] = dif1[idx+1]
                    dif2 = nums[:]
                    dif2[idx+1] =dif2[idx]
                    return dif1 == sorted(dif1) or dif2 == sorted(dif2)

class Solution_v1_1:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if i + 1 <len(nums) and i - 2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
                if count > 1:
                    return False
        return True