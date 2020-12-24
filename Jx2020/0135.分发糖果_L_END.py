"""题目描述"""
'''
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
- 每个孩子至少分配到 1 个糖果。
- 相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
'''

"""示例"""
'''
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
'''

"""解题思路"""
'''
v1.0:
- 采用遍历插值，但是时间复杂度太大，时间超时，不过能肯定是对的。
- 原本想用函数单调性写，但是不知怎么实现。
v2.0:
- 采用栈的思想实现了函数单调性
'''

class Solution:
    def candy(self, s: list) -> int:
        def level_up(numlist, index_front, index):
            numlist[index] = 1
            i = 0
            while index - i - 1 >= index_front:
                if numlist[index - i - 1] == numlist[index - i]:
                    numlist[index - i - 1] += 1
                i += 1

        index_front = 0
        numlist = [0] * len(s)

        # 默认第一个为起始
        numlist[0] = 1
        for index in range(1, len(s)):
            if s[index] > s[index - 1]:
                numlist[index] = numlist[index - 1] + 1
                index_front = index
            elif s[index] < s[index - 1]:
                if numlist[index - 1] == 1:
                    level_up(numlist,index_front,index)
                else:
                    numlist[index] = 1
            else:
                numlist[index] = 1
                index_front = index
        return sum(numlist)

class Solution_v2_0:
    def candy(self, s: list) -> int:
        # 分三种情况
        # 首先创建一个函数（使单减区间内的值累加上去）
        def level_up(numlist, stack):
            if stack:
                i = stack.pop()
                numlist[i] = 1
                while stack:
                    i = stack.pop()
                    numlist[i] = numlist[i+1] + 1
                numlist[i-1] = max(numlist[i-1],numlist[i]+1)
            else:
                pass

        numlist = [0] * len(s)
        numlist[0] = 1
        stack = []

        for i in range(1, len(s)):
            if s[i] > s[i - 1]:
                level_up(numlist,stack)
                numlist[i] = numlist[i - 1] + 1
            elif s[i] == s[i-1]:
                level_up(numlist,stack)
                numlist[i] = 1
            else:
                stack.append(i)
                if i == len(s)-1:
                    level_up(numlist,stack)
        # print(sum(numlist))
        return sum(numlist)