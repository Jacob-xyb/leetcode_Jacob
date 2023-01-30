"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 9:49"
"""

# https://leetcode.cn/problems/merge-in-between-linked-lists/

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        tmp_node = list1
        while tmp_node.next:
            if idx == a - 1:
                node_aL = tmp_node
            elif idx == b:
                node_b = tmp_node
                break
            tmp_node = tmp_node.next
            idx += 1

        node_aL.next = list2
        tmp_node = list2
        while tmp_node.next:
            tmp_node = tmp_node.next
        tmp_node.next = node_b.next
        return list1

    def mergeInBetweenV1_1(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        for _ in range(a - 1):
            cur = cur.next
        cur.next, tail = list2, cur.next
        for _ in range(a, b + 1):
            tail = tail.next
        while cur.next:
            cur = cur.next
        cur.next = tail
        return list1


if __name__ == '__main__':
    list1 = [0, 1, 2, 3, 4, 5]
    node1 = ListNode()
    tmp_node = node1
    for i in list1[:-1]:
        tmp_node.val = i
        tmp_node.next = ListNode()
        tmp_node = tmp_node.next
    tmp_node.val = list1[-1]

    list2 = [1000000, 1000001, 1000002]
    node2 = ListNode()
    tmp_node = node2
    for i in list2[:-1]:
        tmp_node.val = i
        tmp_node.next = ListNode()
        tmp_node = tmp_node.next
    tmp_node.val = list2[-1]
    a = 3
    b = 4
    head = Solution().mergeInBetween(node1, a, b, node2)
    while node1:
        print(node1.val)
        node1 = node1.next

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 11:08"
"""
