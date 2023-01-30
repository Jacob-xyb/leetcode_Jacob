"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 15:10"
"""

# https://leetcode.cn/problems/KnLfVT/

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            tmp = TreeNode(-1, left=root.left)
            root.left = tmp
            self.expandBinaryTree(root.left.left)
        if root.right:
            tmp = TreeNode(-1, right=root.right)
            root.right = tmp
            self.expandBinaryTree(root.right.right)
        return root

    def expandBinaryTreeV1_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 有父节点插入，问题换为，如果有孩子节点，则插入
        if root.left:
            root.left = TreeNode(-1, left=self.expandBinaryTree(root.left))
        if root.right:
            root.right = TreeNode(-1, right=self.expandBinaryTree(root.right))
        return root


if __name__ == '__main__':
    r = TreeNode(1)
    tmp = TreeNode(-1)
    r.left = tmp
    tmp = TreeNode()
    print(r.left.val)

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/30 16:23"
"""
