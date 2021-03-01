from typing import *
"""题目描述"""
'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

"""示例"""
'''
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''

"""解题思路"""
'''
v1.0:
- 冲冲冲！
v1.1:
- 最快范例,快的一匹。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        node = res
        front = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            node.next = ListNode((l1.val + l2.val + front) % 10)
            front = (l1.val + l2.val + front) // 10
            l1, l2, node = l1.next, l2.next, node.next

        if front != 0:
            node.next = ListNode(front)
        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_v1_1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        c1 = l1
        c2 = l2
        c = ListNode()
        head = c
        while (c1 or c2 or carry != 0):
            n = carry
            n += c1.val if c1 else 0
            n += c2.val if c2 else 0
            carry = n // 10
            c.next = ListNode(n % 10)

            c = c.next
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return head.next