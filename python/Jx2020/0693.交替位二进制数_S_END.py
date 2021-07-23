"""题目描述"""
'''
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
'''

"""示例"""
'''
输入：n = 5
输出：true
解释：5 的二进制表示是：101
'''

"""解题思路"""
'''
v1.0:
- 比较简单，一行解决
v1.1:
- 最快
- 只用到异或符
v1.2:
- 也很快
'''


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return False if "00" in bin(n) or "11" in bin(n) else True

class Solution_v1_1:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            if (n & 1) ^ ((n >> 1) & 1) == 0 :
                return False
            n >>= 1
        return True


class Solution_v1_2:
    def hasAlternatingBits(self, n: int) -> bool:
        count = 0
        tmp = n
        while tmp:
            tmp >>= 1
            count += 1

        m = n >> 1
        if m ^ n == (1 << count) - 1:
            return True
        else:
            return False