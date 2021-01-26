"""题目描述"""
'''
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
'''

"""示例"""
'''
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
'''

"""解题思路"""
'''
v1.0:
- len(dominoes[i])==2，所以主动将其排序，然后用字典查表，最后遍历一遍就行了。
v1.1:
- 官方解答:二元组表示 + 计数
本题中我们需要统计所有等价的多米诺骨牌，其中多米诺骨牌使用二元对代表，
「等价」的定义是，在允许翻转两个二元对的的情况下，使它们的元素一一对应相等。

于是我们不妨直接让每一个二元对都变为指定的格式，即第一维必须不大于第二维。这样两个二元对「等价」当且仅当两个二元对完全相同。

注意到二元对中的元素均不大于 99，因此我们可以将每一个二元对拼接成一个两位的正整数，
即 (x,y)→10x+y。这样就无需使用哈希表统计元素数量，而直接使用长度为 100的数组即可。
v1.2:
- 最快范例
- 思路和我一样，可是用元组写会快很多，并且手动排序。
'''


class Solution:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        cdict = {}
        for i in dominoes:
            i = [min(i), max(i)]
            if str(i) in cdict:
                cdict[str(i)] += 1
            else:
                cdict[str(i)] = 0
        res = 0
        for item in cdict.values():
            res += (0+item)*(item+1)//2
        return res

class Solution_v1_1:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret

class Solution_v1_2:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        dic = dict()
        res = 0
        for dom in dominoes:
            if dom[1] < dom[0]:
                dom = (dom[1],dom[0])
            else:
                dom = (dom[0],dom[1])
            if dom not in dic:
                dic[dom] = 1
            else:
                dic[dom] += 1
        for key in dic:
            if dic[key] > 1:
                res += dic[key]*(dic[key]-1)//2
        return res
