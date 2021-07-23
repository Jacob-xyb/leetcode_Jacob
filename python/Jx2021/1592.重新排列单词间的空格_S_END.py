"""题目描述"""
'''
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。
题目测试用例保证 text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。
如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。

返回 重新排列空格后的字符串 。
'''

"""示例"""
'''
输入：text = "  this   is  a sentence "
输出："this   is   a   sentence"
解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。
'''

"""解题思路"""
'''
v1.0:
- 1.先统计空格数spacen，然后统计单词数量word。
- 2.如果只有一个单词的话，空格全部放在后面，需要单独讨论，不然会出现分母为0的情况。
v1.1:
- 速度最快范例。
'''


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spacen = text.count(' ')

        tl = text.split()
        word = len(tl)
        res = ''

        if word == 1:
            res = tl[0] + ' ' * spacen
            return res

        space = [' ' * (spacen // (word - 1))] * word
        space[-1] = ' ' * (spacen % (word - 1))

        for i in range(word):
            res = res + tl[i] + space[i]
        return res

class Solution_v1_1:
    def reorderSpaces(self, text: str) -> str:
        t = text.split()
        c = text.count(" ")
        if len(t) == 1:
            return t[0]+" "*c
        s,s1 = divmod(c, len(t)-1)
        return (" "*s).join(t)+" "*s1

