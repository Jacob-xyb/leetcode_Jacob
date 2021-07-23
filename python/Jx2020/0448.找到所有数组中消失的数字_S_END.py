"""题目描述"""
'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
'''

"""示例"""
'''
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
'''

"""解题思路"""
'''
v1.0:
- 比较简单
v1.1:
- 官方哈希表
v1.2:
- 官方原地修改
'''


class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        res = []
        nums.sort()
        if not nums:
            return []
        elif nums[0] != 1:
            res = list(range(1, nums[0]))
        for i in range(1, len(nums)):
            if nums[i] == nums[0]:
                continue
        #     elif nums[i] - nums[0] == 1:
        #         nums[0] = nums[i]
            else:
                res.extend(range(nums[0]+1, nums[i]))
                nums[0] = nums[i]
        res.extend(range(nums[-1]+1, len(nums)+1))
        return res


class Solution_v1_1(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not
        # really concerned with the frequency of numbers.
        hash_table = {}

        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table.
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)

        return result


class Solution_v1_2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Iterate over each of the elements in the original array
        for i in range(len(nums)):

            # Treat the value as the new index
            new_index = abs(nums[i]) - 1

            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result
