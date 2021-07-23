"""题目描述"""
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''

"""示例"""
'''
输入: "()[]{}"
输出: true
'''

"""解题思路"""
'''
v1.0:
- 栈思想
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        judgein = {'(':0, '{':1, '[':2}
        judgeout = {')':0, '}':1, ']':2}
        for i in s:
            if i in judgein:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if judgein[stack.pop()] != judgeout[i]:
                        return False
        return stack == []