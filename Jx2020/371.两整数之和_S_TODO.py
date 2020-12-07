"""题目描述"""
'''不使用运算符 + 和 -，计算两整数a 、b之和。'''

"""解题思路"""
'''
- 本人是用sum(list)的办法绕过去的啦，人生苦短嘛。
- 但是这样一个简单的问题放到python缺非常的让人头疼，因为python的整数类型为Unifying Long Integers。
解题过程见下面链接：
https://leetcode-cn.com/problems/sum-of-two-integers/solution/python-wei-yun-suan-yi-xie-keng-by-lih/
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
