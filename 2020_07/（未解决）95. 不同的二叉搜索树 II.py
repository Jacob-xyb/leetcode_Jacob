# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# Definition for a binary tree node.
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
    def return_res(self):
        res = self.left + self.right
        return res


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None]
            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []

    def generateTrees_1(self, n: int) -> List[TreeNode]:
        if (n == 0):
            return []

        def build_Trees(left, right):
            all_trees = []
            if (left > right):
                return [None]
            for i in range(left, right + 1):
                left_trees = build_Trees(left, i - 1)
                right_trees = build_Trees(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees

        res = build_Trees(1, n)
        return res

    def generateTrees_2(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 如果 为空树
        if not n:
            return []

        def new_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            # 针对(start,end)中的每一个i进行切分，也就是求G(i),判断左右是否有节点，通过start和end比较
            for i in range(start, end + 1):
                # 左子树
                left_trees = new_trees(start, i - 1)
                # 右子树
                right_trees = new_trees(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        tree = TreeNode(i)
                        tree.left = left
                        tree.right = right
                        all_trees.append(tree)
            # print(all_trees)
            # 注：每次递归进入的子树的all_trees都是不一样的。可以通过打印print()查看控制台的输出，这样更容易理解具体的思路。
            return all_trees

        return new_trees(1, n)


xyb = Solution().generateTrees_2(3)
print(xyb)
