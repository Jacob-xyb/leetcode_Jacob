"""题目描述"""
'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
'''

"""示例"""
'''
输入：s = "abcd", t = "abcde"
输出："e"
'''

"""解题思路"""
'''
v1.0:
- 先排序再挨个找不同
v1.1:
- 利用python利用```Counter```(在标准库的```collections```里)可以一句话实现
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl = list(s)
        sl.sort()
        tl = list(t)
        tl.sort()
        for i in range(len(sl)):
            if tl[i] != sl[i]:
                return tl[i]
        return tl[-1]

from collections import Counter

class Solution_v1_1:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

