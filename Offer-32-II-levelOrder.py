"""
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    """
    方法一：二元组，增加level进行标记
    """
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, level = queue.popleft()     # O(1)
            if len(res) != level+1:
                res.append([node.val])
            else:
                res[level].append(node.val)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return res

    """
    方法二：循环当前队列长度，即为一层数量
    
    def levelOrder(self, root: TreeNode) -> list:
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
    """