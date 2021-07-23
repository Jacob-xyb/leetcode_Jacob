"""题目描述"""
'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
'''

"""示例"""
'''
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
'''

"""解题思路"""
'''
v1.0:
- 利用Counter先数数字，因为Counter的结果顺序是不改变的。
- 然后dict(Counter(s))可以生成字典。
- 找到第一个value=1的key就行了。
'''

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        newlist = []
        from collections import Counter
        countdict = dict(Counter(s)).items()
        for key, value in countdict:
            newlist.append(key)
            newlist.append(value)
        if 1 not in newlist:
            return -1
        else:
            return s.index(newlist[newlist.index(1) - 1])
