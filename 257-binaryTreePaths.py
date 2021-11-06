"""
257. 二叉树的所有路径
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。


示例 1：


输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
示例 2：

输入：root = [1]
输出：["1"]
"""
from binary_tree import *
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        res = []
        if not root:
            return res
        if root and not root.left and not root.right:
            res.append(str(root.val))
            return res

        leftString = self.binaryTreePaths(root.left)
        for i in range(len(leftString)):
            res.append(str(root.val) + "->" + leftString[i])

        rightString = self.binaryTreePaths(root.right)
        for i in range(len(rightString)):
            res.append(str(root.val) + "->" + rightString[i])

        return res


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,None,5]
    targetSum = 22
    bt = BT(arr)
    print(s.binaryTreePaths(bt.root))
