from typing import *
"""题目描述"""
'''
给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。
比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
'''

"""示例"""
'''
输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]
'''

"""解题思路"""
'''
v1.0:
- 测试案例通过，提交测试时超时。
v1.1:
- 还是超时。
v1.3:
- 看评论了解异或性质后写出来不超时的算法。
- 比较朴素的方法，d[0]^d[1]^....d[n1-1]=1^2^...^n1=d[0]^encoded[1]^encoded[3]^...encoded[n],
        求出d[0]，然后利用a^b=c=>a^c=b的特点求剩下的值。
v2.0:
- 最快范例：充分利用了n是奇数且n>=3的性质，强无敌。
'''


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        start = 0
        while 1:
            start += 1
            single = [1] * n
            res = [0] * n
            left = start
            single[0] = 0
            res[0] = left
            for i in range(n - 1):
                left = encoded[i] ^ left
                if left > n:
                    break
                elif single[left - 1] == 1:
                    single[left - 1] = 0
                else:
                    break
                res[i + 1] = left

            if res[-1] != 0:
                return res


class Solution_v1_1:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        start = 0
        while 1:
            start += 1
            res = [0] * n
            left = start
            res[0] = left
            for i in range(n - 1):
                left = encoded[i] ^ left
                if left > n or left in res:
                    break
                res[i + 1] = left

            if res[-1] != 0:
                return res


class Solution_v1_2:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        a = 0
        for i in range(1, n - 1, 2):
            a = a ^ encoded[i]
        b = 0
        for j in range(n + 1):
            b = b ^ j

        d = []

        d.append(a ^ b)

        for k in encoded:
            d.append(d[-1] ^ k)

        return d

class Solution_v2_0:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        x = 1 if n % 4 == 1 else 0
        for i in range(1, len(encoded), 2):
            x ^= encoded[i]
        return [x] + [x := r ^ x for r in encoded]

