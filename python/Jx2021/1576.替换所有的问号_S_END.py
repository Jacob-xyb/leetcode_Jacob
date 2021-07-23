from typing import *
"""题目描述"""
'''
给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。
注意：你 不能 修改非 '?' 字符。
题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。
在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
'''

"""示例"""
'''
输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。
'''

"""解题思路"""
'''
v1.0:
- 先确认'?'的数量，再找到'?'的索引；
- 保证新的字符串与索引前后不同即可。
- 注意:唯一需要注意的就是当索引为最后一个字符时，+1会out of index range，第一个字符-1则变成最后一个字符，无伤大雅。
        因此多出一个逻辑判断即可。
v1.1:
- 最快范例,快的一匹。
'''


class Solution:
    def modifyString(self, s: str) -> str:
        nque = s.count("?")
        if nque == 0:
            return s

        dictionary = "abcdefghijklmnopqrstuvwxyz"

        while nque > 0:
            idx = s.index('?')
            for i in dictionary:
                if idx == len(s) - 1 and i != s[idx - 1]:
                    break
                elif i != s[idx - 1] and i != s[idx + 1]:
                    break
            s = s.replace('?', i, 1)
            nque -= 1

        return s

class Solution_v1_1:
    def modifyString(self, s: str) -> str:
        s1= 'abcdefghijklmnopqrstuvwxyz'
        res = list('0'+s+'0')
        i=1
        while i<len(res)-1:
            if res[i]=='?':
                j=0
                while j<len(s1):
                    if s1[j] not in [res[i-1],res[i+1]]:
                        res[i]=s1[j]
                        break
                    j+=1
            i+=1
        return ''.join(res[1:-1])