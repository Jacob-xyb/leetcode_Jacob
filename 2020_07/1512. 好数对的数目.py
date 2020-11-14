# 给你一个整数数组 nums 。
#
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
#
# 返回好数对的数目。
from typing import List


# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         result = 0
#         for i in range(0, n-1):
#             for j in range(1, n-i):
#                 if nums[i] == nums[i+j]:
#                     result += 1
#         return result


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([nums[inx+1:].count(i) for inx, i in enumerate(nums)])


# # 哈希
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         ret, dct = 0, defaultdict(int)
#         for i in nums:
#             ret, dct[i] = ret+dct[i], dct[i]+1
#         return ret


xyb = Solution()
result = xyb.numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(result)

print(result)



