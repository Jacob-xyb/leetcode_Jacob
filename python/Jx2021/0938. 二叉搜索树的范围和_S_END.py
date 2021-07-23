from typing import *
"""题目描述"""
'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''

"""示例"""
'''
输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
'''

"""解题思路"""
'''
v1.0:
- 最基础的遍历递归
- 需要注意的是要用两个if，而不能用elif，if执行后elif就不会执行了！
v1.1:
- 最快范例,快的一匹。
```
二叉搜索树的特点为：若左子树不为空, 则左子树的所有结点都小于根节点;
 若右子树不为空, 则右子树的所有结点都大于根节点。
 若该结点的值 val 处于 L 和 R 之间，则将该值加起来；
 若 val < L，根据二叉搜索树的特点，该结点的右边可能存在符号条件的值，继续搜寻该结点的右边；
 若 val > R，该结点的左边可能存在符号条件的值，继续搜寻该结点的左边。
```
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def to_sum(root, sumVal=0):
            if root.val == None:
                return 0
            else:
                if low <= root.val <= high:
                    sumVal += root.val

            if root.left != None:
                sumVal += to_sum(root.left)
            if root.right != None:
                sumVal += to_sum(root.right)
            return sumVal

        return to_sum(root)

class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif L > node.val:
                    dfs(node.right)
                else:
                    dfs(node.left)
        self.ans = 0
        dfs(root)
        return self.ans
