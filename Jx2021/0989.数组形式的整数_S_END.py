"""题目描述"""
'''
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
'''

"""示例"""
'''
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
'''

"""解题思路"""
'''
v1.0:
- 暴力遍历
v1.1:
- 最快范例
'''


class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        a = ''
        for i in A:
            a = a + str(i)
        res = int(a) + K
        res = str(res)
        rl = []
        for j in res:
            rl.append(j)
        return rl

class Solution_v1_1:
    def addToArrayForm(self, A: list, K: int) -> list:
        B = [int(i) for i in list(str(K))]
        if len(A) < len(B):
            A,B = B,A
        K = int("".join(str(i) for i in B))
        A = [0] + A
        n = len(A)-1
        while K:
            A[n] = A[n] + K
            K = A[n] // 10
            A[n] %= 10
            n -= 1
        return A if A[0] > 0 else A[1:]
