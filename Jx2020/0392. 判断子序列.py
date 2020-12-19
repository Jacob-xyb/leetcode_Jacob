# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
# 你可以认为 s 和 t 中仅包含英文小写字母。
# 字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
# （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in range(len(s)):
            if s[i] in t[start:]:
                idx = t[start:].index(s[i])
                start = start + idx + 1
            else:
                return False
        return True

    def isSubsequence_1(self, s: str, t: str) -> bool:  # 双指针法
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    def isSubsequence_2(self, s: str, t: str) -> bool:  # 动态规划
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                # f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
                if ord(t[i]) == j + ord("a"):
                    f[i][j] = i
                else:
                    f[i][j] = f[i+1][j]
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


xyb = Solution()
print(xyb.isSubsequence_2("abc", "ahbgdc"))
