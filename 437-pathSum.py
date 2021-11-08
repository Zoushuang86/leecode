"""
437. 路径总和 III
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。



示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3


提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
from binary_tree import *
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        # 寻找包含root节点的路径
        res = self.findPath(root, targetSum)
        # 寻找不包含root节点的路径
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    # 以node为根节点的二叉树中，寻找包含node的路径，和为num
    def findPath(self, node, num):
        if not node:
            return 0

        res = 0
        # 当前存在一条路径，由于有负数后面加起来有可能为0
        if node.val == num:
            res += 1
        res += self.findPath(node.left, num - node.val)
        res += self.findPath(node.right, num - node.val)
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = creatTree(arr)
    targetSum = 8
    # inorder(root)
    print(s.pathSum(root, targetSum))
