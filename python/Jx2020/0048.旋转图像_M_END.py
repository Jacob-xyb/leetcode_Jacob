"""题目说明"""
'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
- 说明
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像
'''

"""示例"""
'''
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

"""解题思路"""
'''
v1.0
-题目很简单，遇到的难点就是必须原地旋转，卡在了复制的问题那里。
'''

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        mt = zip(*matrix)
        for col in mt:
            # col = list(col)
            # col = col[::-1]
            res.append(list(col)[::-1])
        matrix[:] = res     # 不能是matrix = res ，这样是引用
