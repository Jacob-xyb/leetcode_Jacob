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

# [0026. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

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

