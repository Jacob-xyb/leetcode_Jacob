from typing import *
"""题目描述"""
'''
未知 整数数组 arr 由 n 个非负整数组成。
经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。
例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。
给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。
请解码返回原数组 arr 。可以证明答案存在并且是唯一的。
'''

"""示例"""
'''
输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
v1.1:
- 不用标签可能会快一点。
'''


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[i] ^ encoded[i])
        return res

class Solution_v1_1:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(i ^ res[-1])
        return res
