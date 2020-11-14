# 给定一个已按照升序排列 的有序数组，
# 找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，
# 其中 index1 必须小于 index2。
#
# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return False

# 双指针法
# 初始时两个指针分别指向第一个元素位置和最后一个元素的位置。
# 每次计算两个指针指向的两个元素之和，并和目标值比较。
# 如果两个元素之和等于目标值，则发现了唯一解。
# 如果两个元素之和小于目标值，则将左侧指针右移一位。
# 如果两个元素之和大于目标值，则将右侧指针左移一位。
# 移动指针之后，重复上述操作，直到找到答案。
    def twoSum_1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total < target:
                i += 1
            else:
                j -= 1
        return False


xyb = Solution().twoSum_1([2, 7, 11, 15], 9)
print(xyb)


