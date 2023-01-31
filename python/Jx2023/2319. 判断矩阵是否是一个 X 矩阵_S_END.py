"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/31 10:41"
"""

# https://leetcode.cn/problems/check-if-matrix-is-x-matrix/
from typing import *


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        normal_mun = n * n - (n * 2 - (n % 2))
        count_num = 0
        for l in grid:
            count_num += l.count(0)
        if normal_mun != count_num:
            return False
        for row in range(n):
            if grid[row][row] == 0 or grid[row][n - 1 - row] == 0:
                return False
        return True

    def checkXMatrixV1_1(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):  # 也可写为range(n)
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


if __name__ == '__main__':
    grid = [[6, 0, 0, 0, 0, 0, 0, 18], [0, 17, 0, 0, 0, 0, 18, 0], [0, 0, 13, 0, 0, 17, 0, 0],
            [0, 0, 0, 9, 18, 0, 0, 0], [0, 0, 0, 2, 20, 0, 0, 0], [0, 0, 20, 0, 0, 3, 0, 0], [0, 14, 0, 0, 0, 0, 11, 0],
            [19, 0, 0, 0, 0, 0, 0, 9]]
    print(Solution().checkXMatrix(grid))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/31 10:56"
"""
