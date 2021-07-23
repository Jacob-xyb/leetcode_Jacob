from typing import *
"""题目描述"""
'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。
若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
'''

"""示例"""
'''
 输入："aabcccccaaa"
 输出："a2b1c5a3"
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
v1.1:
- 最快范例,快的一匹。
- 启发：此种情形下的确可以不用列表
'''


class Solution:
    def compressString(self, S: str) -> str:
        if len(S) < 3:
            return S

        s = ''
        l = [S[0]]
        for i in S[1:]:
            if l[0] == i:
                l.append(i)
            else:
                s += l[0] + str(len(l))
                l = [i]
        s += l[0] + str(len(l))

        return S if len(S) <= len(s) else s


class Solution_v1_1:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        ch = S[0]
        ans = ''
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                ans += ch + str(cnt)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S
