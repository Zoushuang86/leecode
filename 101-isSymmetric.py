"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归方法
执行用时：40 ms, 在所有 Python3 提交中击败了88.14%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.12%的用户
复杂度分析：
假设树上一共 nn 个节点。
时间复杂度：这里遍历了这棵树，渐进时间复杂度为 O(n)。
空间复杂度：这里的空间复杂度和递归使用的栈空间有关，这里递归层数不超过 n，故渐进空间复杂度为 O(n。
"""
class Solution:
    def isSymmetricTree(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val != r.val:
            return False
        else:
            return self.isSymmetricTree(l.left, r.right) and self.isSymmetricTree(l.right, r.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isSymmetricTree(root.left, root.right)


"""
迭代法
执行用时：56 ms, 在所有 Python3 提交中击败了11.41%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了10.41%的用户
复杂度分析
时间复杂度：O(n)，同「方法一」。
空间复杂度：这里需要用一个队列来维护节点，每个节点最多进队一次，出队一次，队列中最多不会超过 n 个点，故渐进空间复杂度为 O(n)。
"""
class Solution:
    def isSymmetricTree(self, l: TreeNode, r: TreeNode) -> bool:
        queque = []
        queque.append(l)
        queque.append(r)
        while queque != []:
            a = queque.pop(-1)
            b = queque.pop(-1)
            if not a and not b:
                continue
            if (not a or not b) or a.val != b.val:
                return False
            queque.append(a.left)
            queque.append(b.right)
            queque.append(a.right)
            queque.append(b.left)
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isSymmetricTree(root.left, root.right)