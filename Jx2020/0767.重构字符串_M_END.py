"""题目说明"""
'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。
'''

"""解题思路"""
"""
v1.0 
- 纯粹自己的思路
我的题解：
https://leetcode-cn.com/problems/reorganize-string/solution/xiao-bai-de-jing-ji-zhi-lu-_767zhao-chu-zui-chang-/
v1.1
- 官方：基于最大堆的贪心算法
https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode-solution/
v1.2
- 官方：基于计数的贪心算法
https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode-solution/
"""

class Solution:
    def reorganizeString(self, S: str) -> str:
        AllStr = 'abcdefghijklmnopqrstuvwxyz'
        NumList = []
        for i in AllStr:
            NumList.append(S.count(i))
        MaxLenth = max(NumList)  # 找出最长的那个字母的个数
        MaxLenthIndex = NumList.index(MaxLenth)
        word = AllStr[MaxLenthIndex]  # 找出那个字母
        if MaxLenth * 2 - 1 <= sum(NumList):
            InserList = []
            ResList = []
            NumList[MaxLenthIndex] = 0
            for i in range(len(AllStr)):  # 将所有要被插的值平铺在列表中
                InserList.extend(AllStr[i] * NumList[i])
            for j in range(MaxLenth):  # 相当于插秧的过程
                ResList.extend(word)
                ResList.extend(InserList[j::MaxLenth])
            # print(ResList)
            Res = ''.join(ResList)
            return Res
        else:
            return ''


import collections
import heapq

class Solution_v1_1:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))

        if queue:
            ans.append(queue[0][1])

        return "".join(ans)


class Solution_v1_2:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        reorganizeArray = [""] * length
        evenIndex, oddIndex = 0, 1
        halfLength = length // 2

        for c, count in counts.items():
            while count > 0 and count <= halfLength and oddIndex < length:
                reorganizeArray[oddIndex] = c
                count -= 1
                oddIndex += 2
            while count > 0:
                reorganizeArray[evenIndex] = c
                count -= 1
                evenIndex += 2

        return "".join(reorganizeArray)


