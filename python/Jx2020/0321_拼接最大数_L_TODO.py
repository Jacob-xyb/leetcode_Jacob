"""题目说明"""
'''
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
'''

"""解题思路"""
'''
v1.0:
大佬思路以及代码：
题目要求我们用num1和 num2组成k位最大数字，我们可以取num1的可以形成i位最大数字，num2的k - i位最大数字，
他们再组成数字就是最大的。这里有个问题，如何求解一个数组的i位最大数字，例如如何找出[6, 0, 4]最大的两位数字？
方法，我们使用单调栈，维护一个单调减的数组即可！
'''

class Solution:
    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:

        # 求出单个数组可以组成i位的最大数组
        def getMaXArr(nums, i):
            if not i:
                return []
            # pop表示最多可以不要nums里几个数字，要不组成不了i位数字
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num:
                    pop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:i]

        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                # 取num1的i位, num2的k - i
                tmp1 = getMaXArr(nums1, i)
                tmp2 = getMaXArr(nums2, k - i)
                # 合并
                tmp = merge(tmp1, tmp2)
                if res < tmp:
                    res = tmp
        return res
        # 上面一个可以一句话写成
        # return max(merge(getMaXArr(nums1, i), getMaXArr(nums2, k - i))
        # for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2
