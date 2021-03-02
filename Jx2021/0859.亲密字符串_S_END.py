from typing import *
"""题目描述"""
'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 
'''

"""示例"""
'''
输入： A = "ab", B = "ba"
输出： true
解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
- 算是改进了一点，感觉还不错了。
v1.1:
- 最快范例试了几次并没有达到20ms的速度，思路是相同的，iter()可有可无。
'''

from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or A == '' or B == '':  # 1.长度不能或者一方为空
            return False
        elif A == B:  # 2.两者相等时，只要有重复元素即可
            if Counter(A).most_common()[0][1] >= 2:
                return True
            else:
                return False

        # 3.不相等时就要看交换两个元素后是否会相等了
        l = [0, 0]
        c = 0

        for i in range(len(A)):
            if A[i] != B[i]:
                if c == 2:
                    return False
                l[c] = i
                c += 1

        return (c == 2 and A[l[0]] == B[l[1]] and A[l[1]] == B[l[0]])


class Solution_v1_1:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(list(A))!=len(set(list(A)))
        temp = []
        for k, v in iter(enumerate(A)):
            if v != B[k]:
                if len(temp) == 2:
                    return False
                temp.append([v,B[k]])
        return (len(temp) == 2 and temp[0][0] == temp[1][1] and temp[0][1] == temp[1][0])
