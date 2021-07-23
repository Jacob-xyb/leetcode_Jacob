from typing import *
"""题目描述"""
'''
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。
'''

"""示例"""
'''
输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
- 其他版本都和我的差不多。
'''


from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        l = list(count)
        d = dict(count)
        n = len(s)
        l.sort()

        arrow = 0  # 0代表向右，1代表向左
        res = ''
        while n > 0:
            if arrow == 0:
                for i in l:
                    if d[i] > 0:
                        res += i
                        d[i] -= 1
                        n -= 1
                arrow = 1
            else:
                for i in l[::-1]:
                    if d[i] > 0:
                        res += i
                        d[i] -= 1
                        n -= 1
                arrow = 0
        return res
