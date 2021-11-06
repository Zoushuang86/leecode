"""
404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""
from binary_tree import *
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        midSum = 0
        if root.left and not root.left.right and not root.left.left:
            midSum = root.left.val

        return midSum + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)


if __name__ == "__main__":
    s = Solution()
    arr = [10,9,20,1,2,3,4]
    targetSum = 22
    bt = BT(arr)
    print(s.sumOfLeftLeaves(bt.root))
