"""
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。


提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1
"""
from binary_tree import *
# 注意二叉树定义，是大于左子树的所有数，小于右子树的所有数
# 递归方法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), uper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= uper:
                return False

            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, uper):
                return False
            return True
        return helper(root)


if __name__ == "__main__":
    s = Solution()
    arr = [5,4,6,None,None,3,7]
    root = creatTree(arr)
    print(s.isValidBST(root))
