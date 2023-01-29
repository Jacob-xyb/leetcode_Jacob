"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 16:06"
"""
from typing import *


# https://leetcode.cn/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        l_idx = 0
        r_idx = s.find("|")
        query = s[l_idx: r_idx]
        count = 1
        while True:
            tmp = r_idx
            r_idx = s.find("|", r_idx + 1)
            if r_idx == -1:
                query += s[tmp:]
                break
            l_idx = tmp
            count += 1
            if count % 2 != 0:
                query += s[l_idx: r_idx]
        return query.count('*')


class SolutionV2:
    def countAsterisks(self, s: str) -> int:
        idxs = [s.find('|')]
        res = s.count('*')
        if idxs == [-1]:
            return res
        while True:
            idxs.append(s.find('|', idxs[-1] + 1))
            if idxs[-1] == -1:
                idxs.pop()
                break
        for i in range(0, len(idxs), 2):
            res -= s[idxs[i]:idxs[i + 1]].count('*')
            i += 2
        return res


# 最优解
class SolutionV3:
    def countAsterisks(self, s: str) -> int:
        # 数学逻辑
        array = s.split('|')
        res = 0
        for i in range(0, len(array), 2):
            res += array[i].count('*')
        return res


if __name__ == '__main__':
    s = "l|*e*et|c**o|*de|"
    print(SolutionV2().countAsterisks(s))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 16:07"
"""
