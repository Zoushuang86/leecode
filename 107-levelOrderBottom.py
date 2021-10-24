"""
107. 二叉树的层序遍历 II
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        if root == None:
            return res

        queue = []
        # [node, level]
        queue.append([root, 0])
        while queue:
            node = queue[0][0]
            level = queue[0][1]
            queue.pop(0)

            # 数组中还没有该level的数组
            if level == len(res):
                res.append([])
            res[level].append(node.val)

            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return res[::-1]