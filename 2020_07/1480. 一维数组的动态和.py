from typing import List
# 给你一个数组 nums 。数组「动态和」的计算公式为：
# runningSum[i] = sum(nums[0]…nums[i]) 。
#
# 请返回 nums 的动态和。


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         runningsum = [0] * n
#         for i in range(1, n+1):  # range(n) 是从0~(n-1)遍历
#             for j in range(1, i+1):
#                 runningsum[i-1] += nums[j-1]
#         return runningsum


# 迭代
class Solution:
    def runningSum(self, nums):
        newnums = nums
        for i in range(1, len(nums)):
            newnums[i] = newnums[i-1] + nums[i]
        return newnums


xyb = Solution()
result = xyb.runningSum([1, 2, 3, 4])
print(result)

