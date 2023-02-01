"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/31 16:40"
"""

# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import *


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def calculate_diff(num):
            p = 1
            diff = 0
            quotient = num // 10
            while quotient:
                tmp = quotient % 10
                diff += tmp * 10 ** p - tmp
                quotient //= 10
                p += 1
            return diff

        res = 0
        for i in nums:
            res += calculate_diff(i)
        return res

    def differenceOfSumV1_1(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = 0
        for num in nums:
            while num:
                sum2 += num % 10
                num //= 10
        return sum1 - sum2

    def differenceOfSumV1_2(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for num in nums:
            sum1 += num
            while num >= 10:
                sum2 += num % 10
                num //= 10
            sum2 += num
        return sum1 - sum2


if __name__ == '__main__':
    nums = [12, 97, 48, 72, 31, 70, 1, 9, 78, 28, 1, 30, 82, 17, 43, 44, 53, 12, 73, 16, 74, 24, 79, 9, 51, 77, 36, 38,
            81, 38, 69, 60, 29, 21, 66, 6, 62, 55, 13, 90, 66, 7, 15, 15, 60, 76, 44, 30, 6, 86, 87, 59, 88, 36, 32, 35,
            67, 13, 79, 43, 27, 2, 97, 41, 4, 44, 91, 11, 5, 48, 38, 64, 9, 90, 39, 28, 50, 57, 60, 4, 99, 44, 39, 12,
            95, 32, 66, 100, 45, 42, 22, 35, 65, 7, 49, 43, 41, 40, 64, 78]
    print(Solution().differenceOfSumV1_2(nums))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/31 17:05"
"""
