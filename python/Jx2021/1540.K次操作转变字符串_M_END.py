"""题目描述"""
'''
给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。

在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：

选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
不进行任何操作。
切换 1 次字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。

请记住任意一个下标 j 最多只能被操作 1 次。

如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。
'''

"""示例"""
'''
输入：s = "input", t = "ouput", k = 9
输出：true
解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。
'''

"""解题思路"""
'''
v1.0:
- 注意1：s和t长度必须相等
- 注意2：需要相同操作次数时，次数要加26.
v1.1:
- 非常简洁效率的范例。
'''


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        word = "abcdefghijklmnopqrstuvwxyz"
        indexdict = {}
        resdict = {}
        m, n = len(s), len(t)
        if m != n:
            return False
        for i in range(26):
            indexdict[word[i]] = i
        for j in range(n):
            dif = indexdict[t[j]] - indexdict[s[j]]
            dif = dif if dif >= 0 else dif + 26
            if dif not in resdict and dif != 0:
                resdict[dif] = 1
                if dif > k:
                    return False
            elif dif != 0:
                resdict[dif] += 1
                if dif + 26 * (resdict[dif]-1) > k:
                    return False
        return True


class Solution_v1_1:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for si, ti in zip(s, t):
            difference = ord(ti) - ord(si)
            if difference < 0:
                difference += 26
            counts[difference] += 1

        for i, count in enumerate(counts[1:], 1):
            maxConvert = i + 26 * (counts[i] - 1)
            if maxConvert > k:
                return False

        return True
