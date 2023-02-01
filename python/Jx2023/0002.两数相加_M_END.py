"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 15:17"
"""

#  https://leetcode.cn/problems/add-two-numbers/

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 执行用时： 80 ms , 在所有 Python3 提交中击败了 7.50% 的用户
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str = ""
        num2_str = ""
        node1 = l1
        node2 = l2
        while node1:
            num1_str = str(node1.val) + num1_str
            node1 = node1.next
        while node2:
            num2_str = str(node2.val) + num2_str
            node2 = node2.next
        num3_str = str(int(num1_str) + int(num2_str))
        res = node3 = ListNode()
        for c in num3_str[::-1]:
            node3.next = ListNode(int(c))
            node3 = node3.next
        return res.next

    # 执行用时: 60 ms , 在所有 Python3 提交中击败了 71.06% 的用户
    def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        res = node3 = ListNode(0)
        advance = 0
        while node1 or node2:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            node1 = node1.next if node1 else node1
            node2 = node2.next if node2 else node2
            val3 = val1 + val2 + advance
            node3.next = ListNode(val3 % 10)
            advance = val3 // 10
            node3 = node3.next
        if advance != 0:
            node3.next = ListNode(advance)
        return res.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    Solution().addTwoNumbersx(l1, l2)

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 15:48"
"""
