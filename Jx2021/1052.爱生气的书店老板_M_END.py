from typing import *
"""题目描述"""
'''
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 
当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
'''

"""示例"""
'''
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！效率很低
v1.1:
- 最快范例,滑动窗口。
v1.2:
- 也是滑动窗口，但是很精简，理解起来也比较晦涩。
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        angry = [0]*len(grumpy)
        count = 0
        res = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                angry[i] = customers[i]
            else:
                res += customers[i]
        for j in range(len(grumpy)-X):
            if grumpy[j] == 1:
                count = max(count,sum(angry[j:j+X]))
        count = max(count,sum(angry[-X:]))
        return res + count


#
class Solution_v1_1:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)

        alll = 0  # 不操作有的客户数
        mx = 0  # 能避免生气的客户数
        l = 0
        r = 0

        num = 0
        while r < N:
            while r < X:
                mx += grumpy[r] * customers[r]
                if grumpy[r] == 0:
                    alll += customers[r]
                else:
                    num += customers[r]
                r += 1
            l += 1

            if N == X:  # x
                mx = sum([grumpy[k] * customers[k] for k in range(N)])
                return alll + mx

            num = num + grumpy[r] * customers[r] - grumpy[l - 1] * customers[l - 1]
            mx = max(mx, num)

            if grumpy[r] == 0:
                alll += customers[r]

            r += 1

        return alll + mx

class Solution_v1_2:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n=len(customers)
        if X>=n:
            return sum(customers)
        res=0
        for c,g in zip(customers,grumpy):
            res+=c*(1-g)
        s=0
        for i in range(X):
            s+=customers[i]*grumpy[i]
        smax=s
        for i,j in zip(list(range(n-X)),list(range(X,n))):
            s+=customers[j]*grumpy[j]-customers[i]*grumpy[i]
            smax=max(smax,s)
        return res+smax







