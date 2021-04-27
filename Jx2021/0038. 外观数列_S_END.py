from typing import *
"""题目描述"""
'''
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
'''

"""示例"""
'''
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
'''

"""解题思路"""
'''
v1.0:
- 递归；91.9%速度
v1.1:
- 用循环做，比较快。
v1.2:
- 递归，有点花哨~
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        cAS = self.countAndSay(n - 1)
        res = ''
        count = 0
        item = cAS[0]
        for i in cAS:
            if i == item:
                count += 1
            else:
                res += str(count) + item
                item = i
                count = 1
        res += str(count) + item

        return res


class Solution_v1_1:
    def countAndSay(self, n: int) -> str:
        start = '1'
        for i in range(n - 1):
            count = 0
            nex = ''
            pre = start[0]
            for j in start:
                if j == pre:
                    count += 1
                else:
                    nex += str(count)
                    nex += pre
                    pre = j
                    count = 1
            nex += str(count)
            nex += pre
            start = nex
        return start

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            pre_ans = self.countAndSay(n-1)
            count = 1
            ans = ''
            for i_idx, i in enumerate(pre_ans[:-1]):
                if i == pre_ans[i_idx+1]:
                    count += 1
                else:
                    ans += str(count)+i
                    count = 1
            ans += str(count)+pre_ans[-1]
            return ans

