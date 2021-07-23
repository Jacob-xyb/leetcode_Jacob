from typing import *
"""题目描述"""
'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''

"""示例"""
'''
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
v1.1:
- 最快范例,快的一匹。
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        inP = prices[0]
        profit = 0
        idx = 0

        while idx < n - 1:
            idx += 1
            if prices[idx] > inP:
                profit = max(prices[idx] - inP, profit)
            elif prices[idx] < inP:
                inP = prices[idx]
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 1e8, -1e8
        ans = 0
        for p in prices:
            if p < buy:
                buy = p
                sell = 0
            elif p > sell:
                sell = p
                ans = max(ans, sell - buy)
        return ans

