"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 16:38"
"""


# https://leetcode.cn/problems/strictly-palindromic-number/

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


if __name__ == '__main__':
    n = 9
    print(Solution().isStrictlyPalindromic(n))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/29 17:16"
"""
