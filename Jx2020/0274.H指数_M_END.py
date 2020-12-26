"""题目描述"""
'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
h 指数的定义：h 代表“高引用次数”（high citations），
        一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
        且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
'''

"""示例"""
'''
输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
'''

"""解题思路"""
'''
v1.0:
- 既然是**总共有h篇论文分别至少引用了h次**
- 那么换句话说就是**共有h篇论文均引用大于h次**
1. 先排序，首先看着和舒服，然后后续构想中无法绕过排序这一步。
2. 逻辑，`index=0`开始，现在由`n-index`篇论文，最小的就是`citations[index]`：意思就是每篇引用均`>= citations[index]`
- 题目要求 `n-index`篇都大于 `n-index`，那么**每篇引用 >= 篇数** 即`citations[index] >= n-index`
3. 其余的配合代码理解吧，代码还算比较精简。
'''


class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort()
        n = len(citations)
        index = 0
        while index < n:
            if n - index <= citations[index]:
                break
            index += 1
        return n - index
