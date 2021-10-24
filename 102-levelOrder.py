"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
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
        return res
