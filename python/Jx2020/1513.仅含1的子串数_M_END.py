"""题目描述"""
'''
给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
返回所有字符都为 1 的子字符串的数目。
由于答案可能很大，请你将它对 10^9 + 7 取模后返回。
'''

"""示例"""
'''
输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 '1' 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次
'''

"""解题思路"""
'''
v1.0:
1. 找出所有的"1"，然后返回他们每段的最大长度
2. 然后就用数列求和公式: S = 1/2(N+1)*N 就做完了。
v1.1:
- 官方解答思路相同，代码简洁许多但是速度慢了很多。
v1.2:
- 最快
'''


class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        numlist = [0]
        for i in s:
            if i == "1":
                count += 1
            else:
                if count != 0:
                    numlist.append(count)
                    count = 0
        numlist.append(count)

        for num in numlist:
            numlist[0] += (num*num+num)//2
        return numlist[0] % (10**9+7)


class Solutionv1_1:
    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == '0':
                total += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1

        total += consecutive * (consecutive + 1) // 2
        total %= (10 ** 9 + 7)
        return total


class Solutionv1_2:
    def numSub(self, s: str) -> int:
        count = 0
        s = s.split('0')

        for i in s:
            l = len(i)
            count += l*(l+1)//2
        return count % (10**9 + 7)
