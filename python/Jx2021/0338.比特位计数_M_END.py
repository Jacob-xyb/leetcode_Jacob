from typing import *
"""题目描述"""
'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
'''

"""示例"""
'''
输入: 2
输出: [0,1,1]
'''

"""解题思路"""
'''
v1.0:
- 把二进制数拆分，一个二进制数（除0外）第一个一定是1，因此就是1+多少个1的问题。
v1.1:
- 最快范例,快的一匹。
v1.2:
- 在v1.1基础上修改了一下，性能好坏不知，但是通俗易懂一些。
'''


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        n = 0  # n为次幂计数

        for i in range(1, num + 1):
            c = i - 2 ** n
            if i == 2 ** n:
                n += 1
            res.append(1 + res[c])
        return res

class Solution_v1_1:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] = result[i//2] + (i & 1)
        return result

class Solution_v1_2:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] = result[i//2] + (i % 2)
        return result