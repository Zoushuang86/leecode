"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true


提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
"""
from binary_tree import *

"""
自底向上递归
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0

    def height(self, node):
        # 终止条件
        if node == None:
            return 0

        # 先判断该节点的左子树和右子树是否是平衡二叉树
        # 以及该节点为根的树是否是平衡二叉树
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        # 不是平衡二叉树，返回-1
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:   # 是平衡二叉树，返回该节点为根的树的高度
            return max(leftHeight, rightHeight) + 1


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,2,3,3,None,None,4,4]
    bt = BT(arr)
    print(s.isBalanced(bt.root))
