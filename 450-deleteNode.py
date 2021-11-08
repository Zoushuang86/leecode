"""
450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。


示例 1:



输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。


示例 2:

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
示例 3:

输入: root = [], key = 0
输出: []


提示:

节点数的范围 [0, 104].
-105 <= Node.val <= 105
节点值唯一
root 是合法的二叉搜索树
-105 <= key <= 105


进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
"""
from binary_tree import *
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:   # 待删除节点无左子树
                return root.right
            if not root.right:  # 待删除节点无右子树
                return root.left
            node = root.right
            pre = root
            # 寻找右子树最小节点及其父节点进行替换
            while node.left:
                pre = node
                node = node.left
            root.val = node.val
            # 处理顶替节点右子树
            if pre.left.val == node.val:
                # 若顶替的节点是左子树，则替换到父节点的左子树上
                pre.left = node.right
            else:
                # 若顶替的节点是右子树，则替换到父节点的右子树上
                pre.right = node.right
        return root


if __name__ == "__main__":
    s = Solution()
    arr = [5,4,6,None,None,3,7]
    root = creatTree(arr)
    print(s.deleteNode(root))
