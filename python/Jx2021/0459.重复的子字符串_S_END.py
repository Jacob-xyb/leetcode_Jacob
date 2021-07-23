from typing import *
"""题目描述"""
'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
'''

"""示例"""
'''
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
'''

"""解题思路"""
'''
v1.0:
- 从最大公约数开始找公约数。
v1.1:
- 最快范例,两行代码，服气了。
v1.2:
- find()函数，一行代码。
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        if N == 1:
            return False
        for i in range(N//2, 0, -1):
            if N % i == 0:
                if s[:i]*(N//i) == s:
                    return True
        return False

class Solution_v1_1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s+s)[1:-1]
        return s in ss

class Solution_v1_2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1
