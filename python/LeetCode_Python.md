```python
# 所有代码的前置导入
from typing import *
```

# [0001. 两数之和\_S\_END](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 和为目标值 `target`  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

```python
# 输入：
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6

# 输出：
[0,1]
[1,2]
[0,1]
```

- **v1.0**

传统的双循环遍历，效率低下

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [0] * 2
        numsLen = len(nums)
        for i in range(numsLen - 1):
            for j in range(i + 1, numsLen):
                if nums[i] + nums[j] == target:
                    res = [i, j]
                    return res
        return res
    
nums = [2, 7, 11, 15]
target = 9

res = Solution().twoSum(nums, target)
```

执行用时：3200 ms, 在所有 Python3 提交中击败了22.49%的用户

- **v1.1**

由于Python是解释性语言，因此语言本身的执行效率不高，调用内置函数，会有效提升效率

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        for i in range(numsLen-1):
            y = target - nums[i]
            if y in nums[i+1:]:
                return [i, (nums[i+1:].index(y))+i+1]
            
nums = [2, 7, 11, 15]
target = 9

res = Solution().twoSum(nums, target)
```

执行用时：444 ms, 在所有 Python3 提交中击败了46.41%的用户

- **v1.2**

在Python中，遇事不决用 Hash，暂时不明白原理，但是 Hash 就是很快。

思路就是，先建一个哈希表，如果需要寻找的目标数不在表中，那么就把当前 `num` 压入哈希表，以此反复。

缺陷：只适用于两数相加的场景，三个数相加需要进行改良。

```python
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
      
        
nums = [2, 7, 11, 15]
target = 9

res = Solution().twoSum(nums, target)
```

执行用时：32 ms, 在所有 Python3 提交中击败了95.27%的用户

# [0026. 删除有序数组中的重复项\_S\_END](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

给你一个 升序排列 的数组 `nums`，请你 `原地` 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组 `nums` 的第一部分。更规范地说，如果在删除重复项之后有 `k` 个元素，那么 `nums` 的前 k 个元素应该保存最终结果。

将最终结果插入 `nums` 的前 `k` 个位置后返回 `k` 。

不要使用额外的空间，你必须在 `原地` **修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

- **v1.0**

传统遍历，由于不需要考虑超出长度的问题，所以直接遍历一次即可解决问题。

没有使用额外空间，`index` 为O(1)额外空间

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0   # 记录有效数字个数
        if nums:
            for i in range(1, len(nums)):
                if nums[i] != nums[index]:
                    index += 1
                    nums[index] = nums[i]
            return index + 1
        else:
            return 0


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

res = Solution().removeDuplicates(nums)
```

执行用时：36 ms, 在所有 Python3 提交中击败了90.71%的用户

- **v1.1**

非常 Pythonic 的风格，虽然不符合题意

```python
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
```

# [0027. 移除元素\_S_END](https://leetcode-cn.com/problems/remove-element/)

给你一个数组 `nums` 和一个值 `val`，你需要 **原地** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 `O(1)` 额外空间并 **原地 修改输入数组**。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

- **v1.0**

依旧是简单的遍历，将不等于`val` 的元素放置数组中。

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


nums = [3, 2, 2, 3]
val = 3

res = Solution().removeElement(nums, val)
```

执行用时：36 ms, 在所有 Python3 提交中击败了66.25%的用户

- **v1.1**

逆向写并不快多少

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valNum = 0
        index = 0
        numsLen = len(nums)
        while index < (numsLen - valNum):
            if nums[index] == val:
                valNum += 1
                nums[index] = nums[numsLen - valNum]
            else:
                index += 1
        return numsLen - valNum
```

执行用时：32 ms, 在所有 Python3 提交中击败了87.09%的用户

- **v1.2**

双指针，yyds。

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow,fast = 0,0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        return slow
```

执行用时：28 ms, 在所有 Python3 提交中击败了96.32%的用户

# [0035. 搜索插入位置\_S_END](https://leetcode-cn.com/problems/search-insert-position/)

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

- **v1.0**

要求时间复杂度较低，因此采用遍历就不合适了，直接上二分法。

吐槽：测试案例中居然遍历是最快的，测试案例没有覆盖完全呀。

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    
nums = [1, 3, 5, 6]
target = 0

res = Solution().searchInsert(nums, target)
```

执行用时：32 ms, 在所有 Python3 提交中击败了86.77%的用户

# [0053. 最大子数组和](https://leetcode-cn.com/problems/maximum-subarray/)

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

- **示例：**

```python
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

- **v1.0**

最基础的思路，双重遍历，遇大取大，如果当前值 < 0 则退出内部循环，外部循环继续向前，但效率极低。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        for i in range(len(nums)):
            tmpNum = nums[i]
            maxValue = max(maxValue, tmpNum)
			if nums[i] < 0:     # 如果遇到小于0的数，就没有必要在当前循环
                continue
            for j in range(i + 1, len(nums)):
                tmpNum += nums[j]
                maxValue = max(maxValue, tmpNum)
                if tmpNum <= 0:
                    break
        return maxValue


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]    # 6
target = 0
res = Solution().maxSubArray(nums)
```

`超出时间限制`

