"""题目描述"""
'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
'''

"""示例"""
'''
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
'''

"""解题思路"""
'''
v1.0:
- 双指针，但是效率并不高，960ms
v1.1:
- 最效率范例
- 单指针 784ms左右 
'''


class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        right = k - 1
        left = right - (k - 1)
        lrSum = sum(nums[left:right + 1])
        res = lrSum / k
        n = len(nums)

        while right < n - 1:
            lrSum = lrSum - nums[left]
            left += 1
            right += 1
            lrSum = lrSum + nums[right]
            res = max(res, lrSum / k)

        return res

class Solution_v1_1:
    def findMaxAverage(self, nums: list, k: int) -> float:
        size = len(nums)
        if k == 1:
            return max(nums)
        if k == size:
            return sum(nums) / k

        total = sum(nums[0:k])
        total_max = total
        for i in range(k, size):
            total = total - nums[i-k] + nums[i]
            if total > total_max:
                total_max = total

        return total_max / k