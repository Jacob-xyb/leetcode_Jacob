# 给你一个数组 nums ，数组中有 2n 个元素，
# 按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
#
# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * n * 2
        for i in range(0, n):
            result[i+i] = nums[i]
            result[i+i+1] = nums[i+n]
        return result

# 双指针
    def shuffle_1(self, nums: List[int], n: int) -> List[int]:
        i, j = 0, n
        c = [0] * n * 2
        while i < n:
            c[i+i] = nums[i]
            c[i+i+1] = nums[j]
            i += 1
            j += 1
        return c

# in-place swap
# 1.通过in-place swap的方法做到O(1)空间O(n)时间。
# 2.每个"nums[i]"都有一个“目标”index。
    # 例如对于8个数的nums, "nums[0]"想去"0", "nums[4]"想去"1",
    # "nums[1]"想去"2", "nums[5]"想去"3", "nums[2]"想去"4"...
# 3.in-place把nums[i] swap到它想去的index，把swap走的数标记为负数，
    # 并把swap回来的数继续"原地"swap出去，直到swap回来的数的目标index就是“i”自己，然后才增加"i"并继续过下一个“i”。
# 4.遇到nums[i]是负数就说明nums[i]已经在之前的swap中到达了目前位置，因此跳过。
# 5.所有的i都过好后nums就是正确的顺序，
    # 别忘了最后再过一遍把所有的负数变回正数。
# 6.由于每个nums[i]只会被标记1次负数，因此时间复杂度是O(n)

    def shuffle_2(self, nums: List[int], n: int) -> List[int]:
        getDesireIdx = lambda i: i*2 if i < n else (i-n)*2+1
        for i in range(2*n):
            j = i
            while nums[i] >= 0:
                j = getDesireIdx(j)
                nums[i], nums[j] = nums[j], -nums[i]
        for i in range(2*n):
            nums[i] = -nums[i]
        return nums


xyb = Solution().shuffle([2, 5, 1, 3, 4, 7], 3)
print(xyb)
