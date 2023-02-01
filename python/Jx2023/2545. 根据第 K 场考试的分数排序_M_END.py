"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 16:18"
"""

# https://leetcode.cn/problems/sort-the-students-by-their-kth-score/

from typing import *


class Solution:
    # 执行用时： 44 ms , 在所有 Python3 提交中击败了 88.50% 的用户
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


if __name__ == '__main__':
    pass

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 16:21"
"""
