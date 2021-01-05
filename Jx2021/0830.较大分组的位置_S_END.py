"""题目描述"""
'''
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。
上例中的 "xxxx" 分组用区间表示为 [3,6] 。
我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
'''

"""示例"""
'''
输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
'''

"""解题思路"""
'''
v1.0:
- 比较简单，一次遍历
v1.1:
- 官方解答，思路相同，代码较简洁。
'''


class Solution:
    def largeGroupPositions(self, s: str) -> list:
        n = len(s)
        idx = 0
        count = 1
        res = []
        i = 1
        if n <= 2:
            return res
        while i < n:
            if s[i] == s[i-1]:
                count += 1
            else:
                if count >= 3:
                    res.append([idx, idx+count-1])
                idx += count
                count = 1
            i += 1
        if count >= 3:
            res.append([idx, idx+count-1])
        return res


class Solution_v1_1:
    def largeGroupPositions(self, s: str) -> list:
        ret = list()
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        return ret
