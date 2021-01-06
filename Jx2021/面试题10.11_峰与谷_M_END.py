"""题目描述"""
'''
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。
例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。
现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
'''

"""示例"""
'''
输入: [5, 3, 1, 2, 3]
输出: [5, 1, 3, 2, 3]
'''

"""解题思路"""
'''
v1.0:
- 排序然后依次输入，注意要深复制
v1.1
- 最快范例，O(n)复杂度且不用排序。
'''


class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            nums.sort()
            if n % 2 == 0:
                nums1 = nums[:n//2]
                nums2 = nums[n//2:]
                del nums[:]
                for i in range(n//2):
                    nums.append(nums2[-(i+1)])
                    nums.append(nums1[i])
            else:
                nums1 = nums[:n//2]
                nums2 = nums[n//2:]
                del nums[:-1]
                for i in range(n//2):
                    nums.append(nums1[i])
                    nums.append(nums2[-(i+2)])


class Solution_v1_2:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]


