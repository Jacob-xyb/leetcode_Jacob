"""题目描述"""
'''
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
'''

"""示例"""
'''
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
'''

"""解题思路"""
'''
v1.0:
- 看看就行，加速冲！
v1.1:
- 最效率范例
'''


class Solution:
    def transpose(self, A: list) -> list:
        m, n = len(A), len(A[0])
        B = []
        for item in range(n):
            B.append([])
        for i in range(m):
            for j in range(n):
                B[j].append(A[i][j])
        return B

class Solution:
    def transpose(self, A: list) -> list:
        length_1 = len(A)
        length_2 = len(A[0])
        b= []
        for i in range(length_2):
            a=[]
            for j in range(length_1):
                a.append(A[j][i])
            b.append(a)
        return b
