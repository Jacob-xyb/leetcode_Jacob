"""题目描述"""
'''
数组 A 是 [0, 1, ..., N - 1] 的一种排列，N 是数组 A 的长度。全局倒置指的是 i,j 满足 0 <= i < j < N 并且 A[i] > A[j] ，
局部倒置指的是 i 满足 0 <= i < N 并且 A[i] > A[i+1] 。

当数组 A 中全局倒置的数量等于局部倒置的数量时，返回 true 。
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
- 递归
v1.1
- 官方之线性搜索，理想数组法。
对于 理想 排列，0 应该在哪里呢？ 如果 0 的下标大于等于 2，一定会有 A[0] > A[2] = 0，这是一个非局部倒置。
所以 0 只能出现在下标 0 或者下标 1。当 A[1] = 0，显然 A[0] = 1，否则就会有 A[0] > A[j] = 1，这也是一个非局部倒置。
当 A[0] = 0，这时候问题就转化成了一个子问题。
根据上述讨论，可以归纳出 理想 数组的充分必要条件为 Math.abs(A[i] - i) <= 1。
'''


class Solution:
    def isIdealPermutation(self, A: list) -> bool:
        n = len(A)
        if n <= 2:
            return True
        maxnum = A[0]
        i = 1

        while i+1 < n:
            if maxnum > A[i+1]:
                return False
            maxnum = max(maxnum,A[i])
            i += 1
        return True

class Solutionv1_1(object):
    def isIdealPermutation(self, A):
        return all(abs(i-x) <= 1 for i,x in enumerate(A))