"""题目描述"""
'''
给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
'''

"""示例"""
'''
输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。

'''

"""解题思路"""
'''
v1.0:
- 三次通过。
- 第一次没注意需要对应长度，以为很简单就提交了，认真审题后立马想到双指针。
- 第二次出错是没有解决好distance在末尾的判定问题，几番尝试决定在循环里加入if判断。
- __大致思路：__
1. 先用`ord()`算出ASCII码的绝对值差。
2. 然后用双指针来确定最长区间。
3. 当区间和大于maxCost时，左边右移；反之右边右移。
4. 最后可以优化的是最大distance只会出现在区间增加的判别分支上。
v1.1:
- 最效率的范例明显是有问题的，没有考虑到要取最大长度，说明测试案例不够全面，最长的都放在最后面在。
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        resl = []
        for (i,j) in zip(s,t):
            resl.append(abs(ord(j)-ord(i)))

        left,right = 0,0
        distance = 0
        comb = 0
        while right<len(resl):
            if comb > maxCost:
                comb -= resl[left]
                left += 1
            else:
                comb += resl[right]
                right += 1
                if comb <= maxCost:
                    distance = max(distance, right - left)
        return distance

class Solution_v1_1:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        cost = 0
        for right in range(len(s)):
            cost += abs(ord(t[right]) - ord(s[right]))
            if cost > maxCost:
                cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1
        return right - left + 1