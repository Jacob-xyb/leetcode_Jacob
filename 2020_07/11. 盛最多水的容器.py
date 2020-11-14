# 给你 n 个非负整数 a1，a2，...，an，
# 每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        S_area = []
        for i in range(0, n-1):
            for j in range(i+1, n):
                S_area.append((j-i)*min(height[j], height[i]))
        S_area.sort()
        return S_area[-1]

    def maxArea_1(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0  # 最小值
        while i < j:
            res = max(res, (j - i) * min(height[j], height[i]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return res


xyb = Solution().maxArea_1([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(xyb)












