"""题目说明"""
'''
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。
'''

"""示例"""
'''
输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
'''

"""解题思路"""
'''
v1.0:
- 首先保证每行的第一个数（权值最高的数）是1，因为无论如何都可以让第一列全是1，所以第一数不是1的行进行**行转换**
- 然后就是很简单的加法计算了，后面的操作就全部都是**列变换**，因为**行变换**会改变第一位的数字。
- 所以从高位到低位直接计算1最多的数量就可以了。
'''

class Solution:
    def matrixScore(self, A: list) -> int:
        def transfer(row):
            for item in range(len(row)):
                row[item] = 0 if row[item] == 1 else 1
            return row
        # A= [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        rowmax = len(A)
        colmax = len(A[0])
        if colmax == 1:
            return rowmax
        reslist = [rowmax]
        for i in range(rowmax):
            if A[i][0] == 0:
                A[i] = transfer(A[i])

        for col in range(1,colmax):
            counts = 0
            for row in range(rowmax):
                if A[row][col] == 1:
                    counts += 1
            if counts*2 >= rowmax:
                reslist.append(counts)
            else:
                reslist.append(rowmax-counts)

        res = 0
        for colindex in range(colmax):
            res += reslist[colindex] * (2**(colmax-colindex-1))
        return res