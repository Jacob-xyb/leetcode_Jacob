"""题目描述"""
'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''

"""示例"""
'''
输入: 1->1->2
输出: 1->2
'''

"""解题思路"""
'''
v1.0:
- 没有注意已经是排序列表，所以引用了字典。
v1.1:
- 基于排序列表的最效率代码。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: "ListNode") -> "ListNode":
        if head:
            dic = {}
            node = head
            dic[node.val] = 1
            while node.next:
                if node.next.val in dic:
                    node.next = node.next.next
                else:
                    dic[node.next.val] = 1
                    node = node.next
        return head

class Solution_v1_1:
    def deleteDuplicates(self, head: "ListNode") -> "ListNode":
        if head == None:
            return None
        else:
            cur = head
            while cur.next:
                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            return head
