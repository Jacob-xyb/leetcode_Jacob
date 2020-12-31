"""题目描述"""
'''
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
'''

"""示例"""
'''
输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
'''

"""解题思路"""
'''
v1.0:
- 用字典存放，然后先判定最大的有无重复。
1. 有重复就清除掉，剩下一个参与对比
2. 无重复就直接对比。
- 直到还剩最后一个数或者不剩。
    - 代码效率极低。
v1_1:
- 大神题解
- 使用heapq库，因为python只支持小顶堆，所以在入堆的时候我们要添加的是数据的相反数
v1_2:
- 大神手撕python大顶堆
(https://leetcode-cn.com/problems/last-stone-weight/solution/python-zui-da-dui-diao-ku-shou-xie-shi-x-utdj/)
'''


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        from collections import Counter
        p = dict(Counter(stones))
        l = sorted(p)
        n = len(l)
        while n:
            if n < 2:
                if p[l[-1]] % 2 != 0:
                    return l[-1]
                else:
                    return 0
            if p[l[-1]] % 2 != 0:
                p[l[-1]-l[-2]] = p.get(l[-1]-l[-2],0) + 1
                if p[l[-2]] == 1:
                    del p[l[-2]]
                else:
                    p[l[-2]] -= 1
            del p[l[-1]]
            l = sorted(p)
            n = len(l)

import heapq

class Solution_v1_1:
    def lastStoneWeight(self, stones: list) -> int:
        # 初始化
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # 模拟
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x-y)

        if heap: return -heap[0]
        return 0


class Heap:
    def __init__(self, desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):
        """
        添加元素
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0, self.size - 1)
        self.heap.pop()
        self._sift_down(0)
        return item

    def _smaller(self, lhs, rhs):
        return lhs > rhs if self.desc else lhs < rhs

    def _sift_up(self, index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系
        （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
        则持续将当前节点向上调整
        """
        while index:
            parent = (index - 1) // 2

            if self._smaller(self.heap[parent], self.heap[index]):
                break

            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系
        （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
        则持续将当前节点向下调整
        """
        # 若存在子节点
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class Solution_v1_2:
    def lastStoneWeight(self, stones: list) -> int:
        # 初始化大顶堆
        heap = Heap(desc=True)
        for stone in stones:
            heap.push(stone)

        # 模拟
        while heap.size > 1:
            x, y = heap.pop(), heap.pop()
            if x != y:
                heap.push(x - y)
        if heap.size: return heap.heap[0]
        return 0
