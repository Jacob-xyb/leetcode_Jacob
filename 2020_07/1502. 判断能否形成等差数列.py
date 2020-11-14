from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()  # 列表按顺序排列
        # 等差就是任意相邻两项的差相等
        b = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        if len(set(b)) == 1:  # set()函数创建一个无序不重复元素集
            return True
        return False


"""
import ast
lists = ast.literal_eval(input("请输入列表，使用逗号隔开: "))
print(lists)
"""
xyb = Solution().canMakeArithmeticProgression([1, 3, 7])
print(xyb)

# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr.sort()
#         for i in range(1, len(arr) - 1):
#             if arr[i] * 2 != arr[i - 1] + arr[i + 1]:
#                 return False
#         return True
#
#
# arr1 = [1, 3, 5]
# c = Solution().canMakeArithmeticProgression(arr1)
# print(c)
