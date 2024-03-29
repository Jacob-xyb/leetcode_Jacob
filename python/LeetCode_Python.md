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

执行用时：3200 ms, 在所有 Python3 提交中击败了22.49%的用户

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

- **v1.1**

由于Python是解释性语言，因此语言本身的执行效率不高，调用内置函数，会有效提升效率

执行用时：444 ms, 在所有 Python3 提交中击败了46.41%的用户

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

- **v1.2**

在Python中，遇事不决用 Hash，暂时不明白原理，但是 Hash 就是很快。

思路就是，先建一个哈希表，如果需要寻找的目标数不在表中，那么就把当前 `num` 压入哈希表，以此反复。

缺陷：只适用于两数相加的场景，三个数相加需要进行改良。

执行用时：32 ms, 在所有 Python3 提交中击败了95.27%的用户

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

# [0002.两数相加_M_END](https://leetcode.cn/problems/add-two-numbers/)

- **v1.0**

  执行用时： 80 ms , 在所有 Python3 提交中击败了 7.50% 的用户

  先解析链表，提出数字，相加后再写入链表，发现效率很低

  ```python
      def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
          num1_str = ""
          num2_str = ""
          node1 = l1
          node2 = l2
          while node1:
              num1_str = str(node1.val) + num1_str
              node1 = node1.next
          while node2:
              num2_str = str(node2.val) + num2_str
              node2 = node2.next
          num3_str = str(int(num1_str) + int(num2_str))
          res = node3 = ListNode()
          for c in num3_str[::-1]:
              node3.next = ListNode(int(c))
              node3 = node3.next
          return res.next
  ```

- **v2.0**

  执行用时: 60 ms , 在所有 Python3 提交中击败了 71.06% 的用户

  直接在链表中进行计算，效率较高

  ```python
      def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
          node1 = l1
          node2 = l2
          res = node3 = ListNode(0)
          advance = 0
          while node1 or node2:
              val1 = node1.val if node1 else 0
              val2 = node2.val if node2 else 0
              node1 = node1.next if node1 else node1
              node2 = node2.next if node2 else node2
              val3 = val1 + val2 + advance
              node3.next = ListNode(val3 % 10)
              advance = val3 // 10
              node3 = node3.next
          if advance != 0:
              node3.next = ListNode(advance)
          return res.next
  ```

# [0011. 盛最多水的容器\_M_TODO](https://leetcode-cn.com/problems/container-with-most-water/)

- **v1.0**

已经没有全部遍历了，但还是超时，应该是没有bug的

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for l in range(len(height) - 1):
            if height[l]:
                step = max_area // height[l] + 1
                for r in range(l + step, len(height)):
                    area = (r - l) * min(height[l], height[r])
                    max_area = max(area, max_area)
        return max_area
```

- **v1.1**

让 **L** 变小的同时，尽可能的变大 **H**，好像效率还是不高。

执行用时：256 ms, 在所有 Python3 提交中击败了17.74%的用户

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, res = 0, len(height) - 1, 0  # 最小值
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
```

- **v1.2**

在 **v1.1** 的基础上，减少一次大小判断，提速不少。

执行用时：180 ms, 在所有 Python3 提交中击败了75.48%的用户

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0  # 最小值
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, (r - l) * height[l])
                l += 1
            else:
                max_area = max(max_area, (r - l) * height[r])
                r -= 1
        return res
```

- **v1.3**

在 **v1.2** 基础上增加一次最大高度的判断，希望能提前终止循环，应该是最佳方案了。

执行用时：48 ms, 在所有 Python3 提交中击败了99.98%的用户

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        max_h = max(height)
        while l < r:
            # 如果最大高度*当前L都小于最大面积，则停止
            if max_h * (r - l) < max_area:
                break
            if height[l] < height[r]:
                max_area = max(max_area, (r - l) * height[l])
                l += 1
            else:
                max_area = max(max_area, (r - l) * height[r])
                r -= 1
        return max_area
```



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

# [0053. 最大子数组和\_S_END*](https://leetcode-cn.com/problems/maximum-subarray/)

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

- **v1.1**

**贪心算法**：如果当前指针所指元素之前的和小于0，则丢弃当前元素之前的和

经过上面的教训，说明两次遍历是非常影响效率的方式，所以应该尝试一次遍历解决问题。

首先思考为什么会采用两次遍历，是怕一次遍历出现这样的子数组:

XXXXX`AAAAAABB`XXXXXXX

XXXXXXXXXXX`BBCCCCC`XX

其实并不会，因为舍弃A段的原因只能是A<0，不然ABC就会在一起，所以一次遍历能覆盖所有case。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tempSum = 0       # 暂时当前和
        for i in range(len(nums)):
            # 如果当前和小于等于0，就舍去，不然继续累加
            if tempSum <= 0:
                tempSum = nums[i]
            else:
                tempSum += nums[i]
            # 这里为什么省去了 res = max(res, nums[i])，因为保证了 tempSum >= nums[i].
            res = max(res, tempSum)
        return res
```

执行用时：148 ms, 在所有 Python3 提交中击败了75.92%的用户

- **v1.2**

在 **v1.1** 基础上更 Pythonic 的写法，但是效率并不高：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tempSum = 0 
        for i in range(len(nums)):
            tempSum = max(nums[i], tempSum + nums[i])
            res = max(res, tempSum)
        return res
```

执行用时：188 ms, 在所有 Python3 提交中击败了45.16%的用户

- **v1.3**

**动态规划：** 

假设 $\textit{nums}$ 数组的长度是 $n$，下标从 0 到 n-1。

我们用 $f(i)$ 代表以第 $i$ 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是：
$$
\max_{0\le i \le n−1} {\{f(i)\}}
$$
因此我们只需要求出每个位置的 $f(i)$，然后返回 $f$ 数组中的最大值即可。那么我们如何求 $f(i)$ 呢？我们可以考虑 $\textit{nums}[i]$ 单独成为一段还是加入 $f(i−1)$ 对应的那一段，这取决于 $\textit{nums}[i]$ 和 $f(i-1) + \textit{nums}[i]$ 的大小，我们希望获得一个比较大的，于是可以写出这样的动态规划转移方程：

$$
f(i)=max\{f(i−1)+nums[i],nums[i]\}
$$
不难给出一个时间复杂度 $O(n)$、空间复杂度 $O(n)$ 的实现，即用一个 $f$ 数组来保存 $f(i)$ 的值，用一个循环求出所有 $f(i)$。考虑到 $f(i)$ 只和 $f(i-1)$ 相关，于是我们可以只用一个变量 $\textit{pre}$ 来维护对于当前 $f(i)$ 的$f(i−1)$ 的值是多少，从而让空间复杂度降低到 $O(1)$，这有点类似「滚动数组」的思想。

但是实现的代码居然和 **v1.2** 完全一致，但是这是数学上严谨的推导，因为不会产生任何漏洞，思想上比 **v1.2** 更为严谨可靠。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        fi_1 = 0 
        for i in range(len(nums)):
            fi_1 = max(fi_1 + nums[i], nums[i])
            res = max(res, fi_1)
        return res
```

- **v1.4**

**分治**

**这个分治方法类似于「线段树求解最长公共上升子序列问题」的 `pushUp` 操作。**

我们定义一个操作 `get(a, l, r)` 表示查询 $a$ 序列 $[l,r]$ 区间内的最大子段和，那么最终我们要求的答案就是 `get(nums, 0, nums.size() - 1)`。如何分治实现这个操作呢？对于一个区间 $[l,r]$，我们取 $m = \lfloor \frac{l + r}{2} \rfloor$，对区间 $[l,m]$ 和 $[m+1,r]$ 分治求解。当递归逐层深入直到区间长度缩小为 1 的时候，递归「开始回升」。这个时候我们考虑如何通过 $[l,m]$区间的信息和 $[m+1,r]$ 区间的信息合并成区间 $[l,r]$ 的信息。最关键的两个问题是：

- 我们要维护区间的哪些信息呢？
- 我们如何合并这些信息呢？

对于一个区间 $[l,r]$，我们可以维护四个量：

- $\textit{lSum}$ 表示 $[l,r]$ 内以 $l$ 为左端点的最大子段和
- $\textit{rSum}$ 表示 $[l,r]$ 内以 $r$ 为右端点的最大子段和
- $\textit{mSum}$ 表示 $[l,r]$ 内的最大子段和
- $\textit{iSum}$ 表示 $[l,r]$ 的区间和

鉴于此，我们应该先搭建一个框架出来，不然后面很难理解。

```python
class Solution:
    class Status:
        def __init__(self, lSum, rSum, mSum, iSum):
            self.lSum = lSum
            self.rSum = rSum
            self.mSum = mSum
            self.iSum = iSum

    def pushUp(self, lSub: Optional[Status], rSub: Optional[Status]):
        # 暂时返回一个 lSub
        return lSub

    def get(self, nums, l, r):
        if l == r:
            return self.Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) // 2
        lSub = self.get(nums, l, m)
        rSub = self.get(nums, m+1, r)
        return self.pushUp(lSub, rSub)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.get(nums, 0, len(nums)-1).mSum
```

目前框架已经搭建完毕，最难的部分就是维护 `pushUp` 的区间了。

以下简称 $[l,m]$ 为 $[l,r]$ 的「左子区间」，$[m+1,r]$ 为 $[l,r]$ 的「右子区间」。我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 $[l,r]$ 的信息）？对于长度为 $1$ 的区间 $[i,i]$，四个量的值都和 $\textit{nums}[i]$ 相等。对于长度大于 $1$  的区间：

- 首先最好维护的是 $\textit{iSum}$，区间 $[l,r]$ 的 $\textit{iSum}$ 就等于「左子区间」的$ \textit{iSum}$ 加上「右子区间」的 $\textit{iSum}$。`iSum = lSub.iSum + rSub.iSum`
- 对于 $[l,r]$ 的 $\textit{lSum}$，存在两种可能，它要么等于「左子区间」的 $\textit{lSum}$，要么等于「左子区间」的 $\textit{iSum}$ 加上「右子区间」的 $\textit{lSum}$，二者取大。`lSum = max(lSub.lSum, lSub.iSum + rSub.lSum)`
- 对于 $ [l,r]$  的 $\textit{rSum}$，同理，它要么等于「右子区间」的 $\textit{rSum}$，要么等于「右子区间」的 $\textit{iSum}$ 加上「左子区间」的 $\textit{rSum}$，二者取大。`rSum = max(rSub.rSum, rSub.iSum + lSub.rSum)`
- 当计算好上面的三个量之后，就很好计算 $[l,r]$ 的 $\textit{mSum}$ 了。我们可以考虑 $[l,r]$ 的 $\textit{mSum}$ 对应的区间是否跨越 $m$——它可能不跨越 $m$，也就是说 $[l,r]$ 的 $\textit{mSum}$ 可能是「左子区间」的 $\textit{mSum}$ 和 「右子区间」的 $\textit{mSum}$ 中的一个；它也可能跨越 $m$，可能是「左子区间」的 $\textit{rSum}$ 和 「右子区间」的 $\textit{lSum}$ 求和。三者取大。这个应该是最难理解的。`mSum = max(lSub.mSum, rSub.mSum, lSub.rSum + rSub.lSum)`

```python
class Solution:
    class Status:
        def __init__(self, lSum, rSum, mSum, iSum):
            self.lSum = lSum
            self.rSum = rSum
            self.mSum = mSum
            self.iSum = iSum

    def pushUp(self, lSub: Optional[Status], rSub: Optional[Status]) -> Optional[Status]:
        iSum = lSub.iSum + rSub.iSum
        lSum = max(lSub.lSum, lSub.iSum + rSub.lSum)
        rSum = max(rSub.rSum, rSub.iSum + lSub.rSum)
        mSum = max(lSub.mSum, rSub.mSum, lSub.rSum + rSub.lSum)
        return self.Status(lSum, rSum, mSum, iSum)

    def get(self, nums, l, r) -> Optional[Status]:
        if l == r:
            return self.Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) // 2
        lSub = self.get(nums, l, m)
        rSub = self.get(nums, m+1, r)
        return self.pushUp(lSub, rSub)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.get(nums, 0, len(nums)-1).mSum
```

执行用时：1080 ms, 在所有 Python3 提交中击败了5.20%的用户

**Tips: **  **分治** 相较于 **动态规划** 来说，时间复杂度相同，但是因为使用了递归，并且维护了四个信息的结构体，运行的时间略长，空间复杂度也不如方法一优秀，而且难以理解。那么这种方法存在的意义是什么呢？

对于这道题而言，确实是如此的。但是仔细观察**分治**，它不仅可以解决区间 $[0, n-1]$，还可以用于解决任意的子区间 $[l,r]$ 的问题。如果我们把 $[0, n-1]$ 分治下去出现的所有子区间的信息都用堆式存储的方式记忆化下来，即建成一颗真正的树之后，我们就可以在 $O(log n)$ 的时间内求到任意区间内的答案，我们甚至可以修改序列中的值，做一些简单的维护，之后仍然可以在 $O(log n)$ 的时间内求到任意区间内的答案，对于大规模查询的情况下，这种方法的优势便体现了出来。这棵树就是上文提及的一种神奇的数据结构——线段树。

# [0066. 加一\_S_END](https://leetcode-cn.com/problems/plus-one/)

给定一个由 **整数** 组成的 **非空** 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储**单个**数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

- **示例：**

```python
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
```

- **v1.0**

很直接的思路，循环遍历一次，但执行效率好像不理想。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dLen = len(digits)
        for i in range(dLen-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        digits.insert(0, 1)
        return digits
    

nums = [9, 9, 9, 9]

target = 0
res = Solution().plusOne(nums)
```

执行用时：44 ms, 在所有 Python3 提交中击败了12.50%的用户

- **v1.1**

改进一下，如果遇到9，就减少一次加法，速度有所提升。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dLen = len(digits)
        for i in range(dLen-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits
```

执行用时：36 ms, 在所有 Python3 提交中击败了66.16%的用户

**Tips:** 和最快案例是一致的。

# [0108. 将有序数组转换为二叉搜索树\_S_END](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 **高度平衡** 二叉搜索树。

**高度平衡** 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

- **示例：**

![img](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```python
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
```

- **v1.0**

最先想到用递归来写，但是效率中等的样子。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        node = TreeNode()
        self.sortedArrayToBSTRecursion(nums, left, right, node)
        return node

    def sortedArrayToBSTRecursion(self, nums: List[int], left: int, right: int, node: TreeNode):
        mid = (left + right) // 2
        node.val = nums[mid]
        if left > mid-1:
            node.left = None
        else:
            node.left = TreeNode()
            self.sortedArrayToBSTRecursion(nums, left, mid-1, node.left)
        if mid+1 > right:
            node.right = None
        else:
            node.right = TreeNode()
            self.sortedArrayToBSTRecursion(nums, mid+1, right, node.right)
        return


nums = [-10, -3, 0, 5, 9]

res = Solution().sortedArrayToBST(nums)
```

执行用时：48 ms, 在所有 Python3 提交中击败了47.21%的用户

- **v1.1**

非常 pythonic 的风格，并且效率很高，代码简洁，完美运用python列表的特性。

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = (len(nums)-1) // 2
        node = TreeNode(val = nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
```

执行用时：40 ms, 在所有 Python3 提交中击败了89.13%的用户

**Tips:** 其实这是最快案例，LeetCode日常波动。

# [0118. 杨辉三角\_S_END](https://leetcode-cn.com/problems/pascals-triangle/)

给定一个非负整数 *`numRows`，*生成「杨辉三角」的前 *`numRows`* 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![img](https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

- **示例：**

```python
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

- **v1.0**

非常简单直接的思路，效率好像也还可以，就是每个数是它左上方和右上方的数的和。

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        row = 3
        while row <= numRows:
            tempList = [1] * row
            for i in range(row-2):      # 对上一行遍历
                tempList[i+1] = res[row-2][i] + res[row-2][i+1]
            res.append(tempList)
            row += 1
        return res
    

res = Solution().generate(5)
```

执行用时：36 ms, 在所有 Python3 提交中击败了63.41%的用户

- **v1.1**

v1.0方法还可以精简一些，但是效率几乎持平

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        row = 2
        while row <= numRows:
            tempList = [1] * row
            for i in range(row-2):      # 对上一行遍历
                tempList[i+1] = res[row-2][i] + res[row-2][i+1]
            res.append(tempList)
            row += 1
        return res
```

执行用时：36 ms, 在所有 Python3 提交中击败了63.63%的用户

- **v1.2**

最佳案例，感觉最大的差距在于, `for` 循环 和 `while` 循环。

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows + 1):
            row = [1]
            prev = res[-1]
            for j in range(1, len(prev)):
                row.append(prev[j] + prev[j - 1])
            row.append(1)
            res.append(row)
        return res
```

执行用时：28 ms, 在所有 Python3 提交中击败了94.45%的用户

- **v1.3**

由于上述案例，多产生了临时变量，明显拖慢速度，所以把自己的 `while` 改成 `for` 循环试试

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(2, numRows+1):
            tempList = [1] * row
            for i in range(row-2):      # 对上一行遍历
                tempList[i+1] = res[row-2][i] + res[row-2][i+1]
            res.append(tempList)
            row += 1
        return res
```

执行用时：24 ms, 在所有 Python3 提交中击败了99.29%的用户

**Tips:** 果然只有不断打磨代码，才有可能巅峰造极，只要肯深究，多尝试，就有无限可能。

# [0119. 杨辉三角 II\_S_END](https://leetcode-cn.com/problems/pascals-triangle-ii/)

给定一个非负索引 `rowIndex`，返回「杨辉三角」的第 `rowIndex` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

- **示例：**

```python
输入: rowIndex = 3
输出: [1,3,3,1]
输入: rowIndex = 0
输出: [1]
```

- **v1.0**

有了 杨辉三角 的构造经验，只需要从头开始构造，就能获得第 `rowIndex` 行，效率还算可以。

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        preList = [1, 1]
        for row in range(2, rowIndex + 1):
            tempList = [1] * (row + 1)
            for i in range(1, row):  # 对上一行遍历,最后一个1不算（len = row+1)
                tempList[i] = preList[i] + preList[i - 1]
            preList = tempList
        return preList


res = Solution().getRow(5)
```

执行用时：32 ms, 在所有 Python3 提交中击败了86.98%的用户

- **v1.1**

数学问题，杨辉三角的每行通项都是二项式定理展开的系数，第n行第m个数是C(n,m)，Pythonic写法

```python
from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex+1)]
```

执行用时：40 ms, 在所有 Python3 提交中击败了40.08%的用户

---

然后还有更优化的方法吗？再深入的话就需要深刻理解 `杨辉三角形` 了。

杨辉三角具有以下性质：

1. 每行数字左右对称，由 1 开始逐渐变大再变小，并最终回到 1。

2. 第 n 行（从 0 开始编号）的数字有 n+1 项，前 n 行共有 $\frac{n(n+1)}{2}$ 个数。

3. 第 n 行的第 m 个数（从 0 开始编号）可以被表示为组合数 $\mathcal{C}(n,m)$，记作 $\mathcal{C}_n^m$ 或 $\binom{n}{m}$ ，即为从 n 个不同元素中取 m 个元素的组合数。我们可以用公式来表示它：$\mathcal{C}_n^m=\dfrac{n!}{m!(n-m)!}$

4. 每个数字等于上一行的左右两个数字之和，可用此性质写出整个杨辉三角。即第 n 行的第 i 个数等于第 n−1 行的第 i−1 个数和第 i 个数之和。这也是组合数的性质之一，即 $\mathcal{C}_n^i=\mathcal{C}_{n-1}^i+\mathcal{C}_{n-1}^{i-1}$

5. $(a+b)^n$ 的展开式（二项式展开）中的各项系数依次对应杨辉三角的第 n 行中的每一项。

- **v1.2**

在 v1.0 中采用了滚动数组的方式计算出第i行，能否只用一个数组呢？

其实是可以的，由 $\mathcal{C}_n^i=\mathcal{C}_{n-1}^i+\mathcal{C}_{n-1}^{i-1}$ 可知，每次计算第 i 项后，下次计算就不与当前 i 产生关系，即每次计算当前的值，往前推进即可在一个数组里面计算完。

简单示例，以 rowIndex = 4 为例：

```python
res = [1, 0, 0, 0]		# 初始化数组
res = [1, 1, 0, 0]		# row = 2
res = [1, 2, 1, 0]		# row = 3
# 计算结束前，再细化一次计算
res = [1, 2, 1, 1]		# step 1, res[-1] = res[-1] + res[-2]
res = [1, 2, 3, 1]		# step 2, res[-2] = res[-2] + res[-3]
res = [1, 3, 3, 1]		# strp 3, res[-3] = res[-3] + res[-4]
```

code:

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        res = [0] * rowIndex
        res[0] = 1
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):       # 倒着计算
                # res[j] = res[j] + res[j - 1]
                res[j] += res[j - 1]
        return res
```

执行用时：36 ms, 在所有 Python3 提交中击败了67.29%的用户

- **v1.3**

由组合数公式 $\mathcal{C}_n^m=\dfrac{n!}{m!(n-m)!}$  可以推出后一项与前一项的关系:
$$
\mathcal{C}_n^m=\mathcal{C}_n^{m-1} \times \dfrac{n-m+1}{m}
$$
此时 `n = rowIndex` , m 就是 第 n 行的 第 i 个 元素。

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex+1):
            res[i] = res[i - 1] * (rowIndex - i + 1) // i
        return res
```

执行用时：28 ms, 在所有 Python3 提交中击败了96.31%的用户

**Tips:** 这应该是最优解了。

# [0121. 买卖股票的最佳时机\_S_END](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

- 示例：

```python
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

- **v1.0**

最先想到的是 **动态规划**

买卖两天所获取的利润就是这两天之类每一天利润的叠加，所以可以吧每天股价的数组 `prices` 转换为`diff`， `diff[i] = prices[i+1] - prices[i]`，这样问题就转换成 `最大子数组和`。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum, pre = 0, 0
        for i in range(1, len(prices)):
            temp_diff = prices[i] - prices[i-1]     # 当前利润
            pre = max(temp_diff, pre + temp_diff)
            maxSum = max(maxSum, pre)
        return maxSum
    
    
nums = [7, 1, 5, 3, 6, 4]

res = Solution().maxProfit(nums)
```

执行用时：316 ms, 在所有 Python3 提交中击败了27.08%的用户

- **v1.1**

总感觉自己写判断，比 `max()` 函数更快一些。。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum, pre = 0, 0
        for i in range(1, len(prices)):
            temp_diff = prices[i] - prices[i-1]     # 当前利润
            if pre <= 0:
                pre = temp_diff
            else:
                pre += temp_diff
            maxSum = max(maxSum, pre)
        return maxSum
```

执行用时：248 ms, 在所有 Python3 提交中击败了59.45%的用户

- **v1.2**

显然转换为 `最大子数和` 是把问题复杂化了，我们采用 `贪心算法` 来试一下。

在这个问题中如何使用 `贪心算法` 呢？我们肯定是希望在股票的最低价买入，最高价卖出，但是先有买才有卖，所以我们先考虑最低价买入，此时只需要一个变量记录最低价 `minPrice` ，然后考虑往后的日子分别卖出的利润，如果遇到最低价就更新它。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        for sold in prices[1:]:
            res = max(res, sold - minPrice)
            if sold < minPrice:
                minPrice = sold
        return res
```

执行用时：176 ms, 在所有 Python3 提交中击败了86.76%的用户

- **v1.3**

多次证明，`a = max(b, c)` 时，如果 `a = b or a = c` 时，推荐用 if 判断更加效率，少一次赋值操作。

执行用时：100 ms, 在所有 Python3 提交中击败了98.22%的用户

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        for sold in prices[1:]:
            if sold-minPrice > res:
                res = sold - minPrice
            if sold < minPrice:
                minPrice = sold
        return res
```

# [0807. 保持城市天际线\_M_END](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/)

- **v1.0**

傻瓜法：先算每行的最大高度，再算每列的最大高度，每个格子取当前行列的最大值的最小值，然后再算增加的高度

执行用时：60 ms, 在所有 Python3 提交中击败了25.00%的用户

```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        rowMaxList = [0] * row
        colMaxList = [0] * row
        res = 0
        for i in range(row):
            rowMaxList[i] = max(grid[i])
        for j in range(row):
            tempList = [0] * row
            for i in range(row):
                tempList[i] = grid[i][j]
            colMaxList[j] = max(tempList)
        for i in range(row):
            for j in range(row):
                res += min(rowMaxList[i], colMaxList[j]) - grid[i][j]
        return res
```

- **v1.1**

比较 Pythonic 的写法：

执行用时：40 ms, 在所有 Python3 提交中击败了92.54%的用户

```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        rowMaxList = list(map(max, grid))
        colMaxList = list(map(max, zip(*grid)))
        res = 0
        for i in range(row):
            for j in range(row):
                res += min(rowMaxList[i], colMaxList[j]) - grid[i][j]
        return res
```

- **v1.2**

精简到极致的写法：

执行用时：36 ms, 在所有 Python3 提交中击败了98.13%的用户

```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))
```

# [1476. 子矩形查询_M_END](https://leetcode.cn/problems/subrectangle-queries/)

- **v1.0**

这。。。也是给予自信题。

执行用时：88 ms, 在所有 Python3 提交中击败了84.09%的用户

```python
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
```

- **v1.1**

换一种思路，可以不直接改变数据，而是只记录改变过程，更具有效率，但是可能会暂用大量内存。

执行用时：52 ms, 在所有 Python3 提交中击败了97.73%的用户

```python
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle
        self.update = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        res = None
        for i in range(len(self.update)-1, -1, -1):
            row1,col1,row2,col2, val = self.update[i]
            if row1 <= row <= row2 and col1<= col <= col2:
                res = val
                break     
        return res if res else self.data[row][col]
```

# [1669. 合并两个链表_M_END](https://leetcode.cn/problems/merge-in-between-linked-lists/)

- **v1.0**

  执行用时：400 ms, 在所有 Python3 提交中击败了26.04%的用户

  常规思路，先找到a,b两个节点，然后重置list1的连接序列

  ```python
      def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
          idx = 0
          tmp_node = list1
          while tmp_node.next:
              if idx == a - 1:
                  node_aL = tmp_node
              elif idx == b:
                  node_b = tmp_node
                  break
              tmp_node = tmp_node.next
              idx += 1
  
          node_aL.next = list2
          tmp_node = list2
          while tmp_node.next:
              tmp_node = tmp_node.next
          tmp_node.next = node_b.next
          return list1
  ```

- **v1.1**

  执行用时：360 ms, 在所有 Python3 提交中击败了94.08%的用户

  改良版，少了中间变量，逻辑更清晰。

  ```python
      def mergeInBetweenV1_1(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
          cur = list1
          for _ in range(a - 1):
              cur = cur.next
          cur.next, tail = list2, cur.next
          for _ in range(a, b + 1):
              tail = tail.next
          while cur.next:
              cur = cur.next
          cur.next = tail
          return list1
  ```

# [1672. 最富有客户的资产总量\_S_END](https://leetcode-cn.com/problems/richest-customer-wealth/)

- **v1.0**

比较简单.

执行用时：32 ms, 在所有 Python3 提交中击败了91.09%的用户

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
```

# [1769. 移动所有球到每个盒子所需的最小操作数_M_END](https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)

- **v1.0**

  执行用时：3060 ms, 在所有 Python3 提交中击败了36.66%的用户

  暴力双循环

  ```python
      def minOperations(self, boxes: str) -> List[int]:
          res = [0] * len(boxes)
          idxes = []
          for idx, item in enumerate(boxes):
              if item == '1':
                  idxes.append(idx)
          for i in range(len(boxes)):
              for j in range(len(idxes)):
                  res[i] += abs(i - idxes[j])
          return res
  ```

- **v2.0**

  **根据前一个盒子的操作数得到下一个盒子的操作数**

  ![image-20230130143223579](https://s2.loli.net/2023/01/30/InBrFksgvHzat39.png)

  ```python
      def minOperationsV2(self, boxes: str) -> List[int]:
          bn = 0  # 球的总数
          n = len(boxes)
          bnl = [0] * n  # bnl[i]为 i 左侧球的数量
          ans = [0] * n
          for i, x in enumerate(boxes):
              bnl[i] = bn
              if x == '1':
                  bn += 1
                  ans[0] += i
          for i in range(1, n):
              ans[i] = ans[i - 1] + bnl[i] - (bn - bnl[i])
          return ans
  ```

# [1828. 统计一个圆中点的数目_M_END](https://leetcode.cn/problems/queries-on-number-of-points-inside-a-circle/)

- **v1.0**

最简单的思路，双循环 + 点与圆的距离关系。

双循环效率往往很低，并且这是一道中等题。

执行用时：2452 ms, 在所有 Python3 提交中击败了20.79%的用户

```python
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for idx, pq in enumerate(queries):
            for ii, pp in enumerate(points):
                if (pq[0] - pp[0]) ** 2 + (pq[1] - pp[1]) ** 2 <= pq[2] ** 2:
                    res[idx] += 1
        return res
```

- **v1.1**

基于 v1.0 的思想，用简单判断快速去除不符合条件的点。

执行用时：1892 ms, 在所有 Python3 提交中击败了69.89%的用户

```python
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for idx, pq in enumerate(queries):
            for ii, pp in enumerate(points):
                if (abs(pq[0] - pp[0]) > pq[2]) or (pq[1] - pp[1] > pq[2]):
                    continue
                elif (pq[0] - pp[0]) ** 2 + (pq[1] - pp[1]) ** 2 <= pq[2] ** 2:
                    res[idx] += 1
        return res
```

看了下很快的案例用了 numpy，这有啥意思。。

# [1920. 基于排列构建数组\_S_END](https://leetcode-cn.com/problems/build-array-from-permutation/)

- **v1.0**

比较简单，一行代码

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
```

# [1929. 数组串联\_S_END](https://leetcode-cn.com/problems/concatenation-of-array/)

- **v1.0**

这样的题多一些会给人增加自信

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        ans.extend(nums)
        return ans
```

# [2011. 执行操作后的变量值_S_END](https://leetcode.cn/problems/final-value-of-variable-after-performing-operations/)

- **v1.0**

执行用时：40 ms, 在所有 Python3 提交中击败了56.97%的用户

```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for item in operations:
            if "+" in item:
                X += 1
            else:
                X -= 1
        return X 
```

# [2235. 两整数相加\_S_END](https://leetcode-cn.com/problems/add-two-integers/)

- **v1.0**

我陷入了一分钟的思考，缓缓打出一行代码，它不会考我 `int` 的范围吧？两数范围在 `[-100, 100]` ，这...在侮辱我？

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

# [2315. 统计星号_S_END](https://leetcode.cn/problems/count-asterisks/)

- **v1.0**

  执行用时：52 ms, 在所有 Python3 提交中击败了6.49%的用户

  双指针，拼接字符串

  ```python
  class Solution:
      def countAsterisks(self, s: str) -> int:
          l_idx = 0
          r_idx = s.find("|")
          query = s[l_idx: r_idx]
          count = 1
          while True:
              tmp = r_idx
              r_idx = s.find("|", r_idx+1)
              if r_idx == -1:
                  query += s[tmp:]
                  break
              l_idx = tmp
              count += 1
              if count % 2 != 0:
                  query += s[l_idx: r_idx]
          return query.count('*')
  ```

- **v2.0**

  执行用时：40 ms, 在所有 Python3 提交中击败了56.62%的用户

  先记录每次 '|' 的index，然后用 * 的总和减去子字符串的和。

  ```python
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
  ```

- **v3.0**

  最优解，直接用 split 函数

  ```python
  class SolutionV3:
      def countAsterisks(self, s: str) -> int:
          # 数学逻辑
          array = s.split('|')
          res = 0
          for i in range(0, len(array), 2):
              res += array[i].count('*')
          return res
  ```

# [2319. 判断矩阵是否是一个 X 矩阵_S_END](https://leetcode.cn/problems/check-if-matrix-is-x-matrix/)

- **v1.0**

  执行用时：48 ms, 在所有 Python3 提交中击败了78.52%的用户

  先判断0的个数是否能对应上，再循环遍历判断每行是否符合条件

  ```python
      def checkXMatrix(self, grid: List[List[int]]) -> bool:
          n = len(grid)
          normal_mun = n * n - (n * 2 - (n % 2))
          count_num = 0
          for l in grid:
              count_num += l.count(0)
          if normal_mun != count_num:
              return False
          for row in range(n):
              if grid[row][row] == 0 or grid[row][n - 1 - row] == 0:
                  return False
          return True
  ```

- **v1.1**

  非常无脑的双循环遍历

  ```python
      def checkXMatrixV1_1(self, grid: List[List[int]]) -> bool:
          n = len(grid)
          for i in range(n):  # 也可写为range(n)
              for j in range(n):
                  if i == j or i + j == n - 1:
                      if grid[i][j] == 0:
                          return False
                  else:
                      if grid[i][j] != 0:
                          return False
          return True
  ```

# [2325. 解密消息_S_END](https://leetcode.cn/problems/decode-the-message/)

- **v1.0**

  非常常规的思路

  ```python
      def decodeMessage(self, key: str, message: str) -> str:
          text = key.replace(" ", "")
          table = {}
          chr_id = 0
          idx = 0
          while idx < len(text) and chr_id < 26:
              tmp = text[idx]
              if not table.get(tmp):
                  table[tmp] = chr(97 + chr_id)
                  chr_id += 1
              idx += 1
          res = ""
          for c in message:
              res += table.get(c, c)
          return res
  ```

- **v1.1**

  v1.0版本的精简版

  ```python
      def decodeMessageV1_1(self, key: str, message: str) -> str:
          import string
          mp, it = {}, iter(string.ascii_lowercase)
          for c in key:
              if c != ' ' and c not in mp:
                  mp[c] = next(it)
          return ''.join(mp.get(c, c) for c in message)
  ```

# [2396. 严格回文的数字_M_END](https://leetcode.cn/problems/strictly-palindromic-number/)

- **v1.0**

  执行用时：36 ms, 在所有 Python3 提交中击败了65.68%的用户

  从大到小开始判断

  ```python
  class Solution:
      def toStr(self, num, base):
          convertString = "0123456789ABCDEF"  # 最大转换为16进制
          if num < base:
              return convertString[num]
          else:
              return self.toStr(num // base, base) + convertString[num % base]
  
      def isStrictlyPalindromic(self, n: int) -> bool:
          if n > 16:
              return False
          for i in range(n - 2, 1, -1):
              context = self.toStr(n, i)
              if context != context[::-1]:
                  return False
          return True
  ```

# [2469. 温度转换_S_END](https://leetcode.cn/problems/convert-the-temperature/)

签到题

```python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]
```

# [2535. 数组元素和与数字和的绝对差_S_END](https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/submissions/)

- **v1.0**

  执行用时：88 ms, 在所有 Python3 提交中击败了14.20%的用户

  常规方法，辗转相除，不用计算个位数的差，然后逐一计算

  ```python
      def differenceOfSum(self, nums: List[int]) -> int:
          def calculate_diff(num):
              p = 1
              diff = 0
              quotient = num // 10
              while quotient:
                  tmp = quotient % 10
                  diff += tmp * 10 ** p - tmp
                  quotient //= 10
                  p += 1
              return diff
  
          res = 0
          for i in nums:
              res += calculate_diff(i)
          return res
  ```

- **v1.1**

  执行用时：48 ms, 在所有 Python3 提交中击败了95.89%的用户

  换种思路，让循环变的更简单，直接对列表求和，然后再逐位求和，少了很多变量的释放和开销。

  ```python
      def differenceOfSumV1_1(self, nums: List[int]) -> int:
          sum1 = sum(nums)
          sum2 = 0
          for num in nums:
              while num:
                  sum2 += num % 10
                  num //= 10
          return sum1 - sum2
  ```

- **v1.2**

  更简洁的版本，在for循环里计算sum1，然后改良while循环，每次都少一步num的计算

  ```python
      def differenceOfSumV1_2(self, nums: List[int]) -> int:
          sum1 = 0
          sum2 = 0
          for num in nums:
              sum1 += num
              while num >= 10:
                  sum2 += num % 10
                  num //= 10
              sum2 += num
          return sum1 - sum2
  ```

# [2545. 根据第 K 场考试的分数排序_M_END](https://leetcode.cn/problems/sort-the-students-by-their-kth-score/)

Pythonic

```python
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)
```

# [LCP 67. 装饰树_M_END](https://leetcode.cn/problems/KnLfVT/)

- **v1.0**

  执行用时：532 ms, 在所有 Python3 提交中击败了24.24%的用户

  广度优先搜索

  ```python
      def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
          if root.left:
              tmp = TreeNode(-1, left=root.left)
              root.left = tmp
              self.expandBinaryTree(root.left.left)
          if root.right:
              tmp = TreeNode(-1, right=root.right)
              root.right = tmp
              self.expandBinaryTree(root.right.right)
          return root
  ```

- **v1.1**

  精简版，但是效率我认为差不多

  ```python
      def expandBinaryTreeV1_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
          # 有父节点插入，问题换为，如果有孩子节点，则插入
          if root.left:
              root.left = TreeNode(-1, left=self.expandBinaryTree(root.left))
          if root.right:
              root.right = TreeNode(-1, right=self.expandBinaryTree(root.right))
          return root
  ```

# [剑指 Offer 58 - II. 左旋转字符串_S_END](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

- **v1.0**

Pythonic 的题目，一行代码

执行用时：40 ms, 在所有 Python3 提交中击败了56.93%的用户

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
```

