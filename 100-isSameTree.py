"""
100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""

"""
执行用时：40 ms, 在所有 Python3 提交中击败了73.74%的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了79.66%的用户

解题思路
标签：深度优先遍历

终止条件与返回值：
当两棵树的当前节点都为 null 时返回 true
当其中一个为 null 另一个不为 null 时返回 false
当两个都不为空但是值不相等时，返回 false

执行过程：当满足终止条件时进行返回，不满足时分别判断左子树和右子树是否相同，其中要注意代码中的短路效应

复杂度分析：
时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点数。
对两个二叉树同时进行深度优先搜索，只有当两个二叉树中的对应节点都不为空时才会访问到该节点，因此被访问到的节点数不会超过较小的二叉树的节点数。
空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点数。空
间复杂度取决于递归调用的层数，递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
