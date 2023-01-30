"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 13:55"
"""

# https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        idxes = []
        for idx, item in enumerate(boxes):
            if item == '1':
                idxes.append(idx)
        for i in range(len(boxes)):
            for j in range(len(idxes)):
                res[i] += abs(i - idxes[j])
        return res

    def minOperationsV2(self, boxes: str) -> List[int]:
        bn = 0  # 球的总数
        n = len(boxes)
        bnl = [0] * n  # bnl[i]为 i 左侧球的数量
        ans = [0] * n
        for i, x in enumerate(boxes):
            bnl[i] = bn
            if x == '1':
                bn += 1
                ans[0] += i
        for i in range(1, n):
            ans[i] = ans[i - 1] + bnl[i] - (bn - bnl[i])
        return ans


if __name__ == '__main__':
    boxes = "001011"
    print(Solution().minOperations(boxes))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 14:32"
"""
