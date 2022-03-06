# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1) 时间复杂度；
列表 list 的 pop(0) 方法时间复杂度为 O(N) 。

"""
from collections import deque
class Solution:
    """
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)     # O(n)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
    """

    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()     # O(1)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
