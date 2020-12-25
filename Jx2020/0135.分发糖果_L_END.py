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
v2.1（官方解答）：
- 拆解问题，将规则拆分为两个规则分别处理：
- 具体过程代码中说明
v2.2（官方解答）：
- 思路与自己的v2.0一样，但是代码设计巧妙了许多
- 具体过程代码中说明
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


class Solution_v2_1:
    """
    - 拆解问题，将规则拆分为两个规则分别处理：
    >- 左规则：当 \textit{ratings}[i - 1] < \textit{ratings}[i]ratings[i−1]<ratings[i] 时，
            i 号学生的糖果数量将比 i−1 号孩子的糖果数量多。
    >- 右规则：当 \textit{ratings}[i] > \textit{ratings}[i + 1]ratings[i]>ratings[i+1] 时，
            i 号学生的糖果数量将比 i+1 号孩子的糖果数量多。

    我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要被分得的糖果数量。每个人最终分得的糖果数量即为这两个数量的最大值。

    具体地，以左规则为例：我们从左到右遍历该数组，假设当前遍历到位置 i，
    如果有 \textit{ratings}[i - 1] < \textit{ratings}[i]ratings[i−1]<ratings[i]
    那么 i 号学生的糖果数量将比 i−1 号孩子的糖果数量多，
    我们令 \textit{left}[i] = \textit{left}[i - 1] + 1left[i]=left[i−1]+1 即可，
    否则我们令 \textit{left}[i] = 1left[i]=1。

    在实际代码中，我们先计算出左规则 \textit{left}left 数组，在计算右规则的时候只需要用单个变量记录当前位置的右规则，同时计算答案即可。
    """
    def candy(self, ratings: list) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret


class Solution_v2_2:
    def candy(self, ratings: list) -> int:
        """
        依据前面总结的规律，我们可以提出本题的解法。我们从左到右枚举每一个同学，记前一个同学分得的糖果数量为 \textit{pre}pre：
            如果当前同学比上一个同学评分高，说明我们就在最近的递增序列中，直接分配给该同学 \textit{pre} + 1pre+1 个糖果即可。
        否则我们就在一个递减序列中，我们直接分配给当前同学一个糖果，
            并把该同学所在的递减序列中所有的同学都再多分配一个糖果，以保证糖果数量还是满足条件。
        我们无需显式地额外分配糖果，只需要记录当前的递减序列长度，即可知道需要额外分配的糖果数量。
        同时注意当当前的递减序列长度和上一个递增序列等长时，需要把最近的递增序列的最后一个同学也并进递减序列中。
        这样，我们只要记录当前递减序列的长度 dec，最近的递增序列的长度 inc 和前一个同学分得的糖果数量 pre 即可。
        """
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret

